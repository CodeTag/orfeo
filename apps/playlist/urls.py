from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.playlist import views

urlpatterns = patterns('apps.playlist.views',
	
	url(r'^$', 'createPlaylist',name="home"),

)