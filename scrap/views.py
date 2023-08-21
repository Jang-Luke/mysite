from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from .models import Ranksite
import requests
from bs4 import BeautifulSoup
    
def scrap(request):
    context = {}
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
    sitelist = Ranksite.objects.all()
    for sl in sitelist:
        songlist = []
        if sl.name == "genie":
            for i in range(1,2):
                soup = BeautifulSoup(requests.get(sl.url.format(i), headers = headers).text, "lxml")
                for el in soup.select(sl.selector):
                    songlist.append(el.text)
        else:
            soup = BeautifulSoup(requests.get(sl.url, headers = headers).text, "lxml")
        if sl.name == "melon":
            for i in range(50,101, 50):
                for el in soup.select(sl.selector.format(i)):
                    songlist.append(el.get_text().strip())
        else:
            for el in soup.select(sl.selector):
                songlist.append(el.get_text().strip())
        context[sl.name] = songlist
    context["now"] = timezone.now()
    return render(request, "scrap/scrap.html", context)