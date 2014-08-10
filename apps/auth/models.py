from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class CustomUser(models.Model):
  	user = models.OneToOneField(User)
  	friends = models.ManyToManyField('self')

  	def __unicode__(self):
		return self.user.first_name

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        CustomUser.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
