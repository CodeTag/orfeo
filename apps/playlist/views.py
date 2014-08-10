from django.shortcuts import render, render_to_response
from apps.playlist.models import Playlist
from apps.playlist.forms import createPlaylistForm

# Create your views here.
def createPlaylist(request):
	return render_to_response('home.html')
	if request.methos == 'POST':
		form = createPlaylistForm(request.POST)
	 	if form.is_valid():
	 		add = form.save(commit=False)
	 		add.save()
	else:
		form = createPlaylistForm()
	ctx = {'form':form}
	return render_to_response('index.html',ctx,context_instance=RequestContext(request))

	# if request.methos == 'GET':
	# 	pass


def index_view(request):
	return render_to_response('index.html')