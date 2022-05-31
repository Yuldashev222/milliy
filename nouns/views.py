import json

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .models import *
from .forms import NounForm


def home(request):
    form = NounForm()
    synonyms = Synonym.objects.all()
    antonyms = Antonym.objects.all()
    hyponyms = Hyponym.objects.all()
    hyperonyms = Hyperonym.objects.all()
    infoNoun = InfoNoun.objects.all().order_by("-created_date")
    if request.GET:
        word = request.GET["word"]
        if word == InfoNoun.NOUN_TYPES[0][0]:
            word = InfoNoun.NOUN_TYPES[0][1]
        if word == InfoNoun.NOUN_TYPES_STRUCTURE[0][0]:
            word = InfoNoun.NOUN_TYPES_STRUCTURE[0][1]
        if word == InfoNoun.NOUN_MAKING[0][0]:
            word = InfoNoun.NOUN_MAKING[0][1]
        infoNoun = list(InfoNoun.objects.filter(
            Q(word__icontains=word) |
            Q(noun_types__icontains=word) |
            Q(noun_types_structure__icontains=word) |
            Q(noun_making__icontains=word)
        ).order_by("-created_date").values())
        for noun in infoNoun:
            noun["synonyms"] = InfoNoun.objects.get(id=noun["id"]).get_synonyms()
            noun["antonyms"] = InfoNoun.objects.get(id=noun["id"]).get_antonyms()
            noun["hyponyms"] = InfoNoun.objects.get(id=noun["id"]).get_hyponyms()
            noun["hyperonyms"] = InfoNoun.objects.get(id=noun["id"]).get_hyperonyms()

            noun["noun_types"] = InfoNoun.objects.get(id=noun["id"]).get_noun_types_display()
            noun["noun_types_structure"] = InfoNoun.objects.get(id=noun["id"]).get_noun_types_structure_display()
            noun["noun_making"] = InfoNoun.objects.get(id=noun["id"]).get_noun_making_display()

        return JsonResponse({"nouns": infoNoun})

    if request.POST:
        word = request.POST["word"]
        noun_types = request.POST["noun_types"]
        noun_types_structure = request.POST["noun_types_structure"]
        noun_making = request.POST["noun_making"]
        review = request.POST["review"]
        synonym = request.POST.getlist("synonym")
        antonym = request.POST.getlist("antonym")
        hyponym = request.POST.getlist("hyponym")
        hyperonym = request.POST.getlist("hyperonym")

        obj = InfoNoun.objects.get(id=request.POST["id"])
        obj.word = word
        obj.noun_types = noun_types
        obj.noun_types_structure = noun_types_structure
        obj.noun_making = noun_making
        obj.review = review
        obj.synonym.set(synonym)
        obj.antonym.set(antonym)
        obj.hyponym.set(hyponym)
        obj.hyperonym.set(hyperonym)
        obj.save()

        return redirect("nouns")
    ctx = {
        "nouns": infoNoun,
        "form": form,
        "synonyms": synonyms,
        "antonyms": antonyms,
        "hyponyms": hyponyms,
        "hyperonyms": hyperonyms,
    }
    return render(request, "second.html", ctx)


def addNoun(request):
    form = NounForm(request.POST)
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

    return redirect("nouns")


def deleteNoun(request, id):
    obj = InfoNoun.objects.get(id=id)
    obj.delete()

    return redirect("nouns")


def editNoun(request, id):
    obj = InfoNoun.objects.filter(id=id)
    obj_synonyms = InfoNoun.objects.get(id=obj[0].id).get_synonyms()
    obj_antonyms = InfoNoun.objects.get(id=obj[0].id).get_antonyms()
    obj_hyponyms = InfoNoun.objects.get(id=obj[0].id).get_hyponyms()
    obj_hyperonyms = InfoNoun.objects.get(id=obj[0].id).get_hyperonyms()
    obj = list(obj.values())

    synonyms = list(Synonym.objects.all().order_by("-id").values())
    antonyms = list(Antonym.objects.all().order_by("-id").values())
    hyponyms = list(Hyponym.objects.all().order_by("-id").values())
    hyperonyms = list(Hyperonym.objects.all().order_by("-id").values())

    noun_types = list(map(list, InfoNoun.NOUN_TYPES))
    noun_types_structure = list(map(list, InfoNoun.NOUN_TYPES_STRUCTURE))
    noun_making = list(map(list, InfoNoun.NOUN_MAKING))
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
        "noun_types": noun_types,
        "noun_types_structure": noun_types_structure,
        "noun_making": noun_making,
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
