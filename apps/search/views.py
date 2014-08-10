from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from apiclient.discovery import build
from optparse import OptionParser

from apps.playlist.models import Playlist
from apps.auth.models import CustomUser
# Create your views here.

DEVELOPER_KEY = "AIzaSyCchxKFBGhOmC-y7847rVbNjVep14nb2kk" # TODO move this to an env variable
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

@csrf_exempt
def search(request):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
  query = request.GET.get('q')
  if not query:
    return HttpResponse('Missing query')

  search_response = youtube.search().list(
    q=query,
    part="id,snippet",
    maxResults=request.GET.get('max') or 25
  ).execute()

  ctx = {}

  ctx['results'] = search_response.get('items')
  if request.user.is_authenticated():
    ctx['lists'] = Playlist.objects.filter(user=CustomUser.objects.get(user= request.user))

  return render_to_response('search.html', ctx, RequestContext(request))
