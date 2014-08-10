from django.shortcuts import render, render_to_response
from apps.playlist.models import Playlist
from apps.playlist.forms import createPlaylistForm
from django.template import RequestContext

# Create your views here.
def createPlaylist(request):
	if request.method == 'POST':
		form = createPlaylistForm(request.POST)
	 	if form.is_valid():
	 		add = form.save(commit=False)
	 		add.save()
	else:
		form = createPlaylistForm()
	ctx = {'form':form}
	return render_to_response('playlist_create.html',ctx,context_instance=RequestContext(request))

	# if request.methos == 'GET':
	# 	pass


def index_view(request):
	ctx = {'user': request.user}
	return render_to_response('base.html', ctx, context_instance=RequestContext(request))
