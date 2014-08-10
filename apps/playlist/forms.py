#!/usr/bin/env python
# encoding: utf-8

from django import forms
from apps.playlist.models import Playlist

class createPlaylistForm(forms.Form):
	name = forms.CharField(label='Nombre', widget=forms.TextInput())
	genre = forms.CharField(label='Género', widget=forms.TextInput())