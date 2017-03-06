from __future__ import unicode_literals
import re
from datetime import datetime, timedelta
import bcrypt


from django.db import models
class UserManager(models.Manager):
	def validate_registration(self,user):
		EMAIL_REGEX=r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'
		# NAME_REGEX=r'^[A-Za-z0-9_-]*$'
		NAME_REGEX=r'^[a-zA-Z0-9_]+( [a-zA-Z0-9_]+)*$'
		

		# result = User.objects.validate_registration(request.POST)
		print user
		errors=[]
		if len(user[0])<3 or len(user[1])<3:
			errors.append('Name and Username must be at least 3 characters')
		if User.objects.filter(username=user[1]):
			errors.append('This username is taken.')
		if not re.match(NAME_REGEX,user[0]):
			errors.append('Please enter first and last name.')
		if len(user[2])==0:
			errors.append('Password is required')
		if len(user[3])>1 and len(user[3])<8:
			errors.append('Password must be greater than 8 characters')
		if user[2]!=user[3]:
			errors.append('Your passwords do not match.')
		

		return errors
	def validate_login(self,username,password):
		users=User.objects.filter(username=username)
		print users
		pw_bytes = password.encode('utf-8')
		errors=[]
		if len(users)<1:
			print 'if'
			errors.append('No user found. Incorrect username')
			return errors
		elif users[0].hash_pw!=bcrypt.hashpw(pw_bytes,users[0].hash_pw.encode('utf-8')):
			print 'elif'
			errors.append('No Password match')
			return errors
		else:
			return True
		
		
		


class User(models.Model):
	name=models.CharField(max_length=45)
	username=models.CharField(max_length=45)
	hash_pw=models.CharField(max_length=250)
	created_at=models.DateField(auto_now_add=True)
	updated_at=models.DateField(auto_now=True)
	objects=UserManager()
	def __unicode__(self):              # __unicode__ on Python 2
		return self.name

	# a=User.objects.create(name='Bill Bob', alias='jimbo', email='jimbo@yahoo.com',hash_pw=bcrypt.hashpw('billbob',bcrypt.gensalt()))
	# a.save()
	# b=User(name='Basim', alias='Muhammad', email='bbmhmmad@yahoo.com',hash_pw=bcrypt.hashpw('basimmuhammad',bcrypt.gensalt()))
	# b.save()