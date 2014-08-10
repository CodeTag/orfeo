#!/usr/bin/env python
# encoding: utf-8

from django.contrib.auth.decorators import login_required
from forms import InviteFriendForm
from apps.auth.models import CustomUser
from apps.auth.models import Friends
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext

@login_required
def inviteFriendView(request):
	if request.method == 'POST':
		form = InviteFriendForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			try:
				user = User.objects.get(email=email)
				customUser = CustomUser.objects.get(user = user);
				friends = Friends()
				friends.receptor = customUser
				friends.sender = CustomUser.objects.get(user = request.user)
				friends.setState('pending')
				friends.save()
				ctx = {'form': InviteFriendForm(), 'msg': 'Invitación enviada'}
				return render_to_response('user_send_invitation.html', ctx, context_instance=RequestContext(request))
			except User.DoesNotExist:
				ctx = {'form': InviteFriendForm(), 'error': 'El usuario no se encuentra registrado'}
				return render_to_response('user_send_invitation.html', ctx, context_instance=RequestContext(request))
		return render_to_response('user_send_invitation.html', {}, context_instance=RequestContext(request))

	else:
		ctx = {'form': InviteFriendForm()}
		return render_to_response('user_send_invitation.html', ctx, context_instance=RequestContext(request))
