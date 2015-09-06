from django.shortcuts import render

# Create your views here.

def index(request):

    return render(
        request,
        "index.html",

    )

def about(request):


    return render(
        request,
        "about.html",

    )

def news_list(request):


    return render(
        request,
        "news_list.html",

    )

def travel_list(request):


    return render(
        request,
        "travels_list.html",

    )


def nongjiale_list(request):


    return render(
        request,
        "nongjiale_list.html",

    )