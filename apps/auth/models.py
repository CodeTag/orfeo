from django.db import models

class CustomUser(models.Model):
  username   = CharField()
  last_login = DateTimeField(blank=True)
  is_active  = BooleanField()
