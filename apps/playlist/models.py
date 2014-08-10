from django.db import models
from apps.songs.models import Song
from apps.auth.models import CustomUser

# Create your models here.
class Playlist(models.Model):
	
	name = models.CharField(max_length = 50)
	genre = models.CharField(max_length=50)
	songs = models.ManyToManyField(Song) 
	user = models.ForeignKey(CustomUser)

	def __unicode__(self):
		return self.name