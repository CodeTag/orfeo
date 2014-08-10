from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def login(request):
    return HttpResponseRedirect(reverse('apps.playlist.views.index_view'))

