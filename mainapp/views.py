from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from .models import *


def home(request):
    infoAdjective = InfoAdjective.objects.all()
    if request.GET:
        word = request.GET["word"]
        if word:
            infoAdjective = list(InfoAdjective.objects.filter(Q(word__icontains=word)).values())
            for adjective in infoAdjective:
                adjective["synonyms"] = list(InfoAdjective.objects.filter(word=adjective["word"]).values("synonym"))
                print(adjective["synonyms"])
        return JsonResponse({"adjectives": infoAdjective})
    return render(request, "index.html", {"adjectives": infoAdjective})