from django.conf.urls import patterns, include, url
from apps.auth import views

urlpatterns = patterns('apps.auth.views',
	url(r'^users/invite$', 'inviteFriendView',name="iviteFriendView"),
)