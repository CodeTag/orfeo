from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.search import views


urlpatterns = patterns('apps.search.views',

  url(r'^search$', 'search', name="search"),

)
