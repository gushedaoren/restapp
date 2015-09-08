from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import Context
from django.template.loader import get_template
from chongming.models import News


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

    template = get_template('news_list.html')
    news=News.objects.all().order_by("newsTime")
    variables = Context({

    'news': news
    })
    output = template.render(variables)
    return HttpResponse(output)


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