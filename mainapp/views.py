import json
import openpyxl
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .models import *
from .forms import AdjectiveForm, NounForm


def index(request):
    return render(request, "home.html")


def home(request):
    form = AdjectiveForm()
    synonyms = Synonym.objects.all()
    antonyms = Antonym.objects.all()
    hyponyms = Hyponym.objects.all()
    hyperonyms = Hyperonym.objects.all()
    infoAdjective = InfoAdjective.objects.all().order_by("-created_date")
    if request.GET:
        word = request.GET["word"]
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
            adjective["hyponyms"] = InfoAdjective.objects.get(id=adjective["id"]).get_hyponyms()
            adjective["hyperonyms"] = InfoAdjective.objects.get(id=adjective["id"]).get_hyperonyms()

            adjective["adjectives_two"] = InfoAdjective.objects.get(id=adjective["id"]).get_adjectives_two_display()
            adjective["adjective_type"] = InfoAdjective.objects.get(id=adjective["id"]).get_adjective_type_display()
            adjective["adjective_level"] = InfoAdjective.objects.get(id=adjective["id"]).get_adjective_level_display()
            adjective["adjective_type_structure"] = InfoAdjective.objects.get(id=adjective["id"]).get_adjective_type_structure_display()

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
        hyponym = request.POST.getlist("hyponym")
        hyperonym = request.POST.getlist("hyperonym")

        obj = InfoAdjective.objects.get(id=request.POST["id"])
        obj.word = word
        obj.adjectives_two = adjectives_two
        obj.adjective_type = adjective_type
        obj.adjective_level = adjective_level
        obj.adjective_type_structure = adjective_type_structure
        obj.review = review
        obj.synonym.set(synonym)
        obj.antonym.set(antonym)
        obj.hyponym.set(hyponym)
        obj.hyperonym.set(hyperonym)
        obj.save()

        return redirect("home")
    ctx = {
        "adjectives": infoAdjective,
        "form": form,
        "synonyms": synonyms,
        "antonyms": antonyms,
        "hyponyms": hyponyms,
        "hyperonyms": hyperonyms,
    }
    return render(request, "index.html", ctx)



def addAdjective(request):
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
        if request.POST["new_hyponym"] and request.POST["new_hyponym"] not in list(
                map(lambda dict: dict["word"], Hyponym.objects.all().values("word"))):
            new_hyponym = Hyponym.objects.create(word=request.POST["new_hyponym"])
            obj.hyponym.set(new_hyponym)
        if request.POST["new_hyperonym"] and request.POST["new_hyperonym"] not in list(
                map(lambda dict: dict["word"], Hyperonym.objects.all().values("word"))):
            new_hyperonym = Hyperonym.objects.create(word=request.POST["new_hyperonym"])
            obj.hyperonym.set(new_hyperonym)
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
    obj_hyponyms = InfoAdjective.objects.get(id=obj[0].id).get_hyponyms()
    obj_hyperonyms = InfoAdjective.objects.get(id=obj[0].id).get_hyperonyms()
    obj = list(obj.values())

    synonyms = list(Synonym.objects.all().order_by("-id").values())
    antonyms = list(Antonym.objects.all().order_by("-id").values())
    hyponyms = list(Hyponym.objects.all().order_by("-id").values())
    hyperonyms = list(Hyperonym.objects.all().order_by("-id").values())

    adjectives_types_two = list(map(list, InfoAdjective.ADJECTIVES_TYPES_TWO))
    adjective_types = list(map(list, InfoAdjective.ADJECTIVE_TYPES))
    adjective_levels = list(map(list, InfoAdjective.ADJECTIVE_LEVELS))
    adjective_type_structure = list(map(list, InfoAdjective.ADJECTIVE_TYPE_STRUCTURE))
    return JsonResponse({
        "obj": obj,
        "synonyms": synonyms,
        "antonyms": antonyms,
        "hyponyms": hyponyms,
        "hyperonyms": hyperonyms,
        "obj_synonyms": obj_synonyms,
        "obj_antonyms": obj_antonyms,
        "obj_hyponyms": obj_hyponyms,
        "obj_hyperonyms": obj_hyperonyms,
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
    elif check == "Hyponym":
        check = Hyponym
    else:
        check = Hyperonym

    status = 400
    if word and len(word) <= 100 and word not in list(
            map(lambda dict: dict["word"], check.objects.all().values("word"))):
        check.objects.create(word=word)
        status = 200
    objs = check.objects.all().order_by("-id")

    return JsonResponse({"objs": list(objs.values())}, status=status)
