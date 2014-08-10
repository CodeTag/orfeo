from django.db import models

# Create your models here.
class Song(models.Model):
	
	youtubeId = models.CharField(max_length=50, unique=True)
	name = models.CharField(max_length = 50)
	thumbnail = models.CharField(max_length = 50)

	def __unicode__(self):
		return self.name