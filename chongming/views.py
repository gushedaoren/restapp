
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response

# Create your views here.
from django.template import Context, RequestContext
from django.template.loader import get_template
from chongming.models import News, Youji, Nongjiale, AD, Food, Health


def index(request):
    template = get_template('home.html')
    news= News.objects.all().order_by("-newsTime")[:10]
    youjis= Youji.objects.all().order_by("-created")[:3]

    nongjiales_newest=Nongjiale.objects.all().order_by("-created")[:3]
    nongjiales_hot=Nongjiale.objects.all().order_by("-hot")[:3]
    nongjiales_rank=Nongjiale.objects.all().order_by("-rank")[:3]
    ads=AD.objects.all().order_by("created")[:3]
    variables = Context({

        'news': news,
        'youjis': youjis,
        'ads': ads,
        "nongjiales_newest": nongjiales_newest,
        'nongjiales_hot': nongjiales_hot,
        'nongjiales_rank': nongjiales_rank,
    })

    output = template.render(variables)
    return HttpResponse(output)
def about(request):


    return render(
        request,
        "about.html",

    )

def news_list(request):


    news=News.objects.all().order_by("-newsTime")
    paginator = Paginator(news, 20) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        object_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        object_list = paginator.page(paginator.num_pages)

    return render_to_response('news_list.html', {'object_list': object_list})


def news_detial(request,pk):
    news = get_object_or_404(News, pk=pk)
    template = get_template('news_detial.html')
    variables = Context({

    'news': news
    })
    output = template.render(variables)
    return HttpResponse(output)



def travel_list(request):



    youjis=Youji.objects.all().order_by("-created")
    paginator = Paginator(youjis, 10) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        object_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        object_list = paginator.page(paginator.num_pages)

    return render_to_response('travels_list.html', {'object_list': object_list})


def travel_detial(request,pk):
    youji = get_object_or_404(Youji, pk=pk)
    template = get_template('travel_detial.html')
    variables = Context({

    'youji': youji
    })
    output = template.render(variables)
    return HttpResponse(output)

def nongjiale_list(request):



    nongjiales=Nongjiale.objects.all().order_by("-hot","-rank","-created")
    paginator = Paginator(nongjiales, 10) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        object_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        object_list = paginator.page(paginator.num_pages)

    return render_to_response('nongjiale_list.html', {'object_list': object_list})


def nongjiale_detial(request,pk):
    njl = get_object_or_404(Nongjiale, pk=pk)
    template = get_template('nongjiale_detial.html')

    imgs = []

    imgs.append(njl.img1)

    imgs.append(njl.img2)

    imgs.append(njl.img3)

    imgs.append(njl.img4)

    imgs.append(njl.img5)

    variables = Context({
       'imgs': imgs,
       'njl': njl,

    })
    output = template.render(variables)
    return HttpResponse(output)

def ad_detial(request,pk):
    ad = get_object_or_404(AD, pk=pk)
    template = get_template('ad_detial.html')
    imgs = []

    imgs.append(ad.img1)

    imgs.append(ad.img2)

    imgs.append(ad.img3)

    imgs.append(ad.img4)

    imgs.append(ad.img5)
    variables = Context({
        'imgs': imgs,
        'ad': ad
    })
    output = template.render(variables)
    return HttpResponse(output)


def food_list(request):



    foods=Food.objects.all().order_by("-created")
    paginator = Paginator(foods, 10) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        object_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        object_list = paginator.page(paginator.num_pages)

    return render_to_response('food_list.html', {'object_list': object_list})



def food_detial(request,pk):
    obj = get_object_or_404(Food, pk=pk)
    template = get_template('food_detial.html')
    variables = Context({

        'obj': obj
    })
    output = template.render(variables)
    return HttpResponse(output)

def health_list(request):



    objs=Health.objects.all().order_by("-created")
    paginator = Paginator(objs, 20) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        object_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        object_list = paginator.page(paginator.num_pages)

    return render_to_response('health_list.html', {'object_list': object_list})



def health_detial(request,pk):
    obj = get_object_or_404(Health, pk=pk)
    template = get_template('health_detial.html')
    variables = Context({

        'obj': obj
    })
    output = template.render(variables)
    return HttpResponse(output)