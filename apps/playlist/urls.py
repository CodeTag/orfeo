from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.playlist import views

urlpatterns = patterns('apps.playlist.views',

	url(r'^$', 'index_view',name="home"),
	url(r'^playlist/create$', 'createPlaylist',name="createPlaylistView"),
	url(r'^playlist/read$', 'readPlaylist',name="readPlaylist"),

	url(r'^playlist/addSong$', 'addSongToPlaylist',name="readPlaylistView"),
	url(r'^playlist/delete/(\d+)$', 'deletePlaylist',name="deletePlaylistView"),

)




