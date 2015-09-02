


from django.conf.urls import patterns, url
from chongming import views

from oliver.views import LoginView, RegisterView

urlpatterns = patterns('',

    url(r'$', views.index),





)
