from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template import Context
from django.template.loader import get_template
from chongming.models import News, Youji, Nongjiale


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
    news=News.objects.all().order_by("-newsTime")
    variables = Context({

    'news': news
    })
    output = template.render(variables)
    return HttpResponse(output)


def news_detial(request,pk):
    news = get_object_or_404(News, pk=pk)
    template = get_template('news_detial.html')
    variables = Context({

    'news': news
    })
    output = template.render(variables)
    return HttpResponse(output)



def travel_list(request):


    template = get_template('travels_list.html')
    youjis=Youji.objects.all().order_by("-created")
    variables = Context({


    'youjis' : youjis
    })
    output = template.render(variables)
    return HttpResponse(output)

def travel_detial(request,pk):
    youji = get_object_or_404(Youji, pk=pk)
    template = get_template('travel_detial.html')
    variables = Context({

    'youji': youji
    })
    output = template.render(variables)
    return HttpResponse(output)

def nongjiale_list(request):


    template = get_template('nongjiale_list.html')
    nongjiales=Nongjiale.objects.all().order_by("-created")
    variables = Context({


    'nongjiales' : nongjiales
    })
    output = template.render(variables)
    return HttpResponse(output)

def nongjiale_detial(request,pk):
    njl = get_object_or_404(Nongjiale, pk=pk)
    template = get_template('nongjiale_detial.html')
    variables = Context({

    'njl': njl
    })
    output = template.render(variables)
    return HttpResponse(output)