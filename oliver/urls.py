


from django.conf.urls import patterns, url

from oliver.views import LoginView, RegisterView

urlpatterns = patterns('',

    url(r'^rest/login$', LoginView.as_view()),
    url(r'^rest/register', RegisterView.as_view()),




)
