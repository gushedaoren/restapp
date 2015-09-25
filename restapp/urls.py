"""restapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
import os
from django.conf.urls import include, url,patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from chongming import views
from chongming.models import News, Nongjiale, Youji
from restapp import settings
from django.contrib.sitemaps import views as sitemaps_views, GenericSitemap
from django.views.decorators.cache import cache_page

news_dict = {
    'queryset': News.objects.all(),
    'pub_time': 'pub_time',
}

sitemaps = {
    'news': GenericSitemap(news_dict, priority=0.6),
}

urlpatterns =patterns('',
               url(r'^admin/', include(admin.site.urls)),


                url(r'chongming^', include('chongming.urls')),
                url(r'^$', views.index),
                url(r'^about/', views.about),
                url(r'^travel_list/', views.travel_list),
                url(r'^news_list/', views.news_list),
                url(r'food_list/', views.food_list),
                url(r'health_list/', views.health_list),
                url(r'^news_detial/(.+)/$', views.news_detial),
                url(r'^health_detial/(.+)/$', views.health_detial),
                url(r'^nongjiale_list/', views.nongjiale_list),
                url(r'^tinymce/', include('tinymce.urls')),
                url(r'^travel_detial/(.+)/$', views.travel_detial),
                url(r'^nongjiale_detial/(.+)/$', views.nongjiale_detial),
                url(r'^mce_filebrowser/', include('mce_filebrowser.urls')),
                url(r'^ad_detial/(.+)/$', views.ad_detial),
                url(r'^food_detial/(.+)/$', views.food_detial),



                      )

urlpatterns += staticfiles_urlpatterns()

urlpatterns += patterns("",

    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': "/restapp_media", 'show_indexes': False}),
   # (r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static/images'}),
    (r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static/css'}),
    (r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static/js'}),
    (r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static/images'}),


)

news_dict = {
    'queryset': News.objects.all(),

}

njl_dict = {
    'queryset': Nongjiale.objects.all(),

}

youji_dict = {
    'queryset': Youji.objects.all(),

}

sitemaps = {
# 'flatpages': FlatPageSitemap,

    'news': GenericSitemap(news_dict, priority=0.7),
    'njl': GenericSitemap(njl_dict, priority=0.6),
    'youji': GenericSitemap(youji_dict, priority=0.5),
}

urlpatterns += patterns('django.contrib.sitemaps.views', 
    (r'^sitemap\.xml$', 'index', {'sitemaps': sitemaps}),
    (r'^sitemap-(?P<section>.+)\.xml$', 'sitemap', {'sitemaps': sitemaps}),
)
