from django.db import models
from apps.songs.models import Song

# Create your models here.
class Playlist(models.Model):
	
	name = models.CharField(max_length = 50)
	genre = models.CharField(max_length=50)
	songs = models.ManyToManyField(Song) 

	def __unicode__(self):
		return self.name