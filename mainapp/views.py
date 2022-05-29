import json

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .models import *
from .forms import AdjectiveForm


def home(request):
    form = AdjectiveForm()
    synonyms = Synonym.objects.all()
    antonyms = Antonym.objects.all()
    hyponyms = Hyponym.objects.all()
    hyperonyms = Hyperonym.objects.all()
    infoAdjective = InfoAdjective.objects.all().order_by("-created_date")
    if request.GET:
        word = request.GET["word"]
        infoAdjective = list(InfoAdjective.objects.filter(Q(word__icontains=word)).order_by("-created_date").values())
        for adjective in infoAdjective:
            adjective["synonyms"] = InfoAdjective.objects.get(id=adjective["id"]).get_synonyms()
            adjective["antonyms"] = InfoAdjective.objects.get(id=adjective["id"]).get_antonyms()
            adjective["hyponyms"] = InfoAdjective.objects.get(id=adjective["id"]).get_hyponyms()
            adjective["hyperonyms"] = InfoAdjective.objects.get(id=adjective["id"]).get_hyperonyms()

        return JsonResponse({"adjectives": infoAdjective})
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
