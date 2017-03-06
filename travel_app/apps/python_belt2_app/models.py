from __future__ import unicode_literals
from ..login_app.models import *
from django.db import models

class Trip(models.Model):
	destination=models.CharField(max_length=45)
	start=models.DateField(auto_now=False)
	end=models.DateField(auto_now=False)
	plan=models.TextField()
	user=models.ManyToManyField(User,related_name='trips')
	created_at=models.DateField(auto_now_add=True)
	updated_at=models.DateField(auto_now=True)
