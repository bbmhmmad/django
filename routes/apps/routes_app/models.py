from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
	name=models.CharField(max_length=45)
	description=models.TextField(max_length=750)
	price=models.CharField(max_length=10)

# Create your models here.
