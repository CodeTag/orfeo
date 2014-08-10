from django.shortcuts import render, render_to_response, get_object_or_404,redirect
from apps.playlist.models import Playlist
from apps.auth.models import CustomUser
from apps.songs.models import Song
from apps.playlist.forms import createPlaylistForm
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


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


def index_view(request):
	ctx = {'user': request.user}
	return render_to_response('base.html', ctx, context_instance=RequestContext(request))


def readPlaylist(request):
	playlist = Playlist.objects.all()
	ctx = {"playlists":playlist}
	return render_to_response('playlist.html',ctx,context_instance = RequestContext(request))


@csrf_exempt
def addSongToPlaylist(request):
	listName = request.POST.get('listName')

	songId = request.POST.get('songId')
	songThumbnail = request.POST.get('songThumbnail')
	songName = request.POST.get('songName')

	song = Song(youtubeId=songId,name=songName,thumbnail=songThumbnail)
	song.save()

	playlist = Playlist.objects.get(name=listName, user=CustomUser.objects.get(user=request.user))

	playlist.songs.add(song)

	return HttpResponse('ok')

def deletePlaylist(request, id_playlist):
    playlist = get_object_or_404(Playlist, id=id_playlist)    
    if request.method=='GET':
        playlist.delete()
    	return redirect('readPlaylistView')



