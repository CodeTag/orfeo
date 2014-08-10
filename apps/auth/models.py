from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class CustomUser(models.Model):
  	user = models.OneToOneField(User)
  	friends = models.ManyToManyField('self', through='Friends', symmetrical=False)

  	def __unicode__(self):
		return self.user.first_name

class Friends(models.Model):
	sender = models.ForeignKey(CustomUser, related_name='sender_friend')
	receptor = models.ForeignKey(CustomUser, related_name='receptor_friend')
	state = models.IntegerField(max_length=1)

	def setState(self, state):
		states = {"pending" : 1, "accepted" : 2, 'rejected': 3}
		self.state = states[state]

	def getState(self):
		states = { 1: "pending" , 2 :"accepted" , 3: 'rejected'}
		return states[self.state]

	class Meta:
		unique_together = ('sender', 'receptor',)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        CustomUser.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
