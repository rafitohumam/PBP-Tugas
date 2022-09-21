from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_watchlist(request):

    data_watchlist = MyWatchList.objects.all()
    
    context = {
    "list_film": data_watchlist,
    "nama": "Rafito Humam",
    "npm" : "2106633626",
    "watched_count": 0,
    "not_watched_count": 0,
    "movie_count": ""
    }

    watch_count(context)

    return render(request, "mywatchlist.html", context)

def watch_count(content):

    for i in content.get("list_film"):
        if i.watched == True:
            content["watched_count"] += 1
        if i.watched == False:
            content["not_watched_count"] += 1

    if content["watched_count"] >= content["not_watched_count"]:
        content["movie_count"] = "Selamat, kamu sudah banyak menonton!"
        
    else:
        content["movie_count"] = "Wah, kamu masih sedikit menonton!"

def show_html(request):

    data_watchlist = MyWatchList.objects.all()

    return HttpResponse(serializers.serialize("html", data_watchlist), content_type="application/html")

def show_xml(request):

    data_watchlist = MyWatchList.objects.all()

    return HttpResponse(serializers.serialize("xml", data_watchlist), content_type="application/xml")

def show_json(request):

    data_watchlist = MyWatchList.objects.all()

    return HttpResponse(serializers.serialize("json", data_watchlist), content_type="application/json")

def show_xml_id(request, id):

    data_watchlist = MyWatchList.objects.filter(pk=id)

    return HttpResponse(serializers.serialize("xml", data_watchlist), content_type="application/xml")

def show_json_id(request, id):

    data_watchlist = MyWatchList.objects.filter(pk=id)

    return HttpResponse(serializers.serialize("json", data_watchlist), content_type="application/json")