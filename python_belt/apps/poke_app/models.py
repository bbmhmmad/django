from __future__ import unicode_literals

from django.db import models
from ..login_app.models import User

class Poke(models.Model):
	poker=models.ForeignKey(User,related_name='user_poker',null=True)
	poked=models.ForeignKey(User,related_name='user_poked',null=True)
	created_at=models.DateField(auto_now_add=True)
	updated_at=models.DateField(auto_now=True)

# Create your models here.
