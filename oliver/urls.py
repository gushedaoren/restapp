


from django.conf.urls import patterns, url

from oliver.views import LoginView

urlpatterns = patterns('',

    url(r'^rest/login$', LoginView.as_view()),




)
