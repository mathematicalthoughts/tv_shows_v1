from django.shortcuts import render, redirect
from .models import TVShow

# Create your views here.

def root(request):
    return redirect('/shows')

def index(request):
    if request.method == "GET":
        context = {
            "tv_shows" : TVShow.objects.all()
        } 
    return render (request,'index.html',context)

def createShows(request):
    if request.method == "GET":   
        return render (request,'shows_new.html')

    elif request.method == "POST":

        tv_show = TVShow (
            title = request.POST["title"],
            network = request.POST["network"],
            released_date = request.POST["released_date"],
            description = request.POST["description"]
        )
    tv_show.save()
    print(request.POST)
    return redirect('/')

def readShows(request,id):    
    context = {
            "tv_shows" : TVShow.objects.all()
        }  
    return render (request,'shows_read.html', context)

def editShows(request, id):
    if request.method == "GET":
        return render (request,'shows_edit.html')

    elif request.method == "POST":
        return redirect ('/')

