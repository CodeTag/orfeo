from django.shortcuts import render, render_to_response
from apps.playlist.models import Playlist
from apps.auth.models import CustomUser
from apps.playlist.forms import createPlaylistForm
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def createPlaylist(request):
	if request.method == 'POST':
		form = createPlaylistForm(request.POST)
	 	if form.is_valid():
	 		customUser = CustomUser.objects.get(user= request.user)
	 		playlist = Playlist()
	 		playlist.name = form.cleaned_data['name']
	 		playlist.genre = form.cleaned_data['genre']
	 		playlist.user = customUser
	 		playlist.save()
	 		ctx = {'form':createPlaylistForm(), 'msg':'Lista creada exitosamente'}
	 		return render_to_response('playlist_create.html', ctx, context_instance=RequestContext(request))
	 		
	else:
		form = createPlaylistForm()
	ctx = {'form':form}
	return render_to_response('playlist_create.html',ctx,context_instance=RequestContext(request))

	# if request.methos == 'GET':
	# 	pass


def index_view(request):
	ctx = {'user': request.user}
	return render_to_response('base.html', ctx, context_instance=RequestContext(request))


def readPlaylist(request):
	playlist = Playlist.objects.all()
	ctx = {"playlists":playlist}
	return render_to_response('playlist.html',ctx,context_instance = RequestContext(request))
