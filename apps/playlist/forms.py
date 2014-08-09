from django import forms
from apps.playlist.models import Playlist

class createPlaylistForm(forms.ModelForm):
	class Meta:
		model = Playlist