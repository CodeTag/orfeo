from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from apiclient.discovery import build
from optparse import OptionParser
import json
# Create your views here.

DEVELOPER_KEY = "AIzaSyCchxKFBGhOmC-y7847rVbNjVep14nb2kk" # TODO move this to an env variable
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


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

  print type(search_response)

  return HttpResponse(json.dumps(search_response))
