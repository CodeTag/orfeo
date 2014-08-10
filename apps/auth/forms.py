from django import forms

class InviteFriendForm(forms.Form):
	email = forms.CharField(widget=forms.TextInput())