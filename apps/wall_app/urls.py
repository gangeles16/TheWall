#MY APP URLS
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^register$',views.register),
    url(r'^login$',views.login),
    url(r'^dashboard$',views.dashboard),
    url(r'^posting$',views.posting),
    url(r'^Comments$', views.Comments),
    url(r'^(?P<id>[0-9]+)/delete_comment$', views.delete_comment),
    url(r'^logout$', views.logout)
]

