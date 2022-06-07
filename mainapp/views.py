import json
import openpyxl
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .models import *
from .forms import AdjectiveForm, FileForm


def index(request):
    return render(request, "home.html")


def home(request):
    form = AdjectiveForm()
    synonyms = Synonym.objects.all()
    antonyms = Antonym.objects.all()
    infoAdjective = InfoAdjective.objects.all().order_by("-created_date")
    if request.GET:
        word = request.GET["word"]
        if word == InfoAdjective.ADJECTIVES_TYPES_TWO[0][0]:
            word = InfoAdjective.ADJECTIVES_TYPES_TWO[0][1]
        if word == InfoAdjective.ADJECTIVE_TYPES[0][0]:
            word = InfoAdjective.ADJECTIVE_TYPES[0][1]
        if word == InfoAdjective.ADJECTIVE_LEVELS[0][0]:
            word = InfoAdjective.ADJECTIVE_LEVELS[0][1]
        if word == InfoAdjective.ADJECTIVE_TYPE_STRUCTURE[0][0]:
            word = InfoAdjective.ADJECTIVE_TYPE_STRUCTURE[0][1]
        infoAdjective = list(InfoAdjective.objects.filter(
            Q(word__icontains=word) |
            Q(adjectives_two__icontains=word) |
            Q(adjective_type__icontains=word) |
            Q(adjective_level__icontains=word) |
            Q(adjective_type_structure__icontains=word)
        ).order_by("-created_date").values())
        for adjective in infoAdjective:
            adjective["synonyms"] = InfoAdjective.objects.get(id=adjective["id"]).get_synonyms()
            adjective["antonyms"] = InfoAdjective.objects.get(id=adjective["id"]).get_antonyms()

            adjective["adjectives_two"] = InfoAdjective.objects.get(id=adjective["id"]).get_adjectives_two_display()
            adjective["adjective_type"] = InfoAdjective.objects.get(id=adjective["id"]).get_adjective_type_display()
            adjective["adjective_level"] = InfoAdjective.objects.get(id=adjective["id"]).get_adjective_level_display()
            adjective["adjective_type_structure"] = InfoAdjective.objects.get(
                id=adjective["id"]).get_adjective_type_structure_display()

        return JsonResponse({"adjectives": infoAdjective})

    if request.POST:
        word = request.POST["word"]
        adjectives_two = request.POST["adjectives_two"]
        adjective_type = request.POST["adjective_type"]
        adjective_level = request.POST["adjective_level"]
        adjective_type_structure = request.POST["adjective_type_structure"]
        review = request.POST["review"]
        synonym = request.POST.getlist("synonym")
        antonym = request.POST.getlist("antonym")

        obj = InfoAdjective.objects.get(id=request.POST["id"])
        obj.word = word
        obj.adjectives_two = adjectives_two
        obj.adjective_type = adjective_type
        obj.adjective_level = adjective_level
        obj.adjective_type_structure = adjective_type_structure
        obj.review = review
        obj.synonym.set(synonym)
        obj.antonym.set(antonym)
        obj.save()

        return redirect("home")
    ctx = {
        "adjectives": infoAdjective,
        "form": form,
        "synonyms": synonyms,
        "antonyms": antonyms,
    }
    return render(request, "index.html", ctx)


def addAdjective(request):
    if request.FILES:
        file_form = FileForm(request.POST, request.FILES)
        if file_form.is_valid():
            file = file_form.save(commit=False)
            name = file.file
            file.save()
            sheet = openpyxl.open(f"media/{name}").active
            word = sheet["A1"].value.strip()
            adjectives_two = sheet["B1"].value
            adjective_type = sheet["C1"].value
            adjective_level = sheet["D1"].value
            adjective_type_structure = sheet["E1"].value
            synonyms = list(map(lambda elem: elem.strip().replace(",", "").replace(".", ""), sheet["F1"].value.split()))
            antonyms = list(map(lambda elem: elem.strip().replace(",", "").replace(".", ""), sheet["G1"].value.split()))
            print(synonyms, antonyms, sep="\n")
            review = sheet["H1"].value.strip()
            new_adjective = InfoAdjective.objects.create(
                word=word,
                adjectives_two=InfoAdjective.ADJECTIVES_TYPES_TWO[adjectives_two - 1][0],
                adjective_type=InfoAdjective.ADJECTIVE_TYPES[adjective_type - 1][0],
                adjective_level=InfoAdjective.ADJECTIVE_LEVELS[adjective_level - 1][0],
                adjective_type_structure=InfoAdjective.ADJECTIVE_TYPE_STRUCTURE[adjective_type_structure - 1][0],
                # synonym=synonym,
                # antonym=antonym,
                review=review
            )
            new_adjective.save()
            return redirect("home")

    form = AdjectiveForm(request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        if request.POST["new_synonym"] and request.POST["new_synonym"] not in list(
                map(lambda dict: dict["word"], Synonym.objects.all().values("word"))):
            new_synonym = Synonym.objects.create(word=request.POST["new_synonym"])
            obj.synonym.set(new_synonym)
        if request.POST["new_antonym"] and request.POST["new_antonym"] not in list(
                map(lambda dict: dict["word"], Antonym.objects.all().values("word"))):
            new_antonym = Antonym.objects.create(word=request.POST["new_antonym"])
            obj.antonym.set(new_antonym)
        obj.save()
        form.save_m2m()

    return redirect("home")


def deleteAdjective(request, id):
    obj = InfoAdjective.objects.get(id=id)
    obj.delete()

    return redirect("home")


def editAdjective(request, id):
    obj = InfoAdjective.objects.filter(id=id)
    obj_synonyms = InfoAdjective.objects.get(id=obj[0].id).get_synonyms()
    obj_antonyms = InfoAdjective.objects.get(id=obj[0].id).get_antonyms()
    obj = list(obj.values())

    synonyms = list(Synonym.objects.all().order_by("-id").values())
    antonyms = list(Antonym.objects.all().order_by("-id").values())

    adjectives_types_two = list(map(list, InfoAdjective.ADJECTIVES_TYPES_TWO))
    adjective_types = list(map(list, InfoAdjective.ADJECTIVE_TYPES))
    adjective_levels = list(map(list, InfoAdjective.ADJECTIVE_LEVELS))
    adjective_type_structure = list(map(list, InfoAdjective.ADJECTIVE_TYPE_STRUCTURE))
    return JsonResponse({
        "obj": obj,
        "synonyms": synonyms,
        "antonyms": antonyms,
        "obj_synonyms": obj_synonyms,
        "obj_antonyms": obj_antonyms,
        "adjectives_types_two": adjectives_types_two,
        "adjective_types": adjective_types,
        "adjective_levels": adjective_levels,
        "adjective_type_structure": adjective_type_structure,
    })


def add_objs(request):
    word = request.GET["word"]
    check = request.GET["check"]

    if check == "Synonym":
        check = Synonym
    elif check == "Antonym":
        check = Antonym

    status = 400
    if word and len(word) <= 100 and word not in list(
            map(lambda dict: dict["word"], check.objects.all().values("word"))):
        check.objects.create(word=word)
        status = 200
    objs = check.objects.all().order_by("-id")

    return JsonResponse({"objs": list(objs.values())}, status=status)
