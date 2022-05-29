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
        print("{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}")
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
    obj = list(InfoAdjective.objects.filter(id=id).values())[0]
    obj["synonyms"] = InfoAdjective.objects.get(id=obj["id"]).get_synonyms()
    obj["antonyms"] = InfoAdjective.objects.get(id=obj["id"]).get_antonyms()
    obj["hyponyms"] = InfoAdjective.objects.get(id=obj["id"]).get_hyponyms()
    obj["hyperonyms"] = InfoAdjective.objects.get(id=obj["id"]).get_hyperonyms()
    return JsonResponse({"obj": obj})


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
