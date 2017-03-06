from django.shortcuts import render,redirect
from django.contrib import messages
from .models import User,UserManager
import bcrypt
from django.core.urlresolvers import reverse

def index(request):
	print User.objects.all
	return render(request,'login_app/index.html')

def registration(request):
	result=User.objects.validate_registration([request.POST['name'],request.POST['username'],request.POST['password'],request.POST['confirm_password'],])
	print result
	user_name=request.POST['name']
	user_username=request.POST['username']
	user_password=request.POST['password']
	user_confirm=request.POST['confirm_password']
	if len(result)>0:
		for error in result:
			messages.warning(request, error)
		return redirect(reverse('login:index'))
	else:
		pw_bytes = user_password.encode('utf-8')
		hash_pw=bcrypt.hashpw(pw_bytes,bcrypt.gensalt())
		messages.success(request, 'Registration Complete!')
		insert=User(name=user_name,username=user_username,hash_pw=hash_pw)
		insert.save()
		user_info=User.objects.get(username=request.POST['username'])
		request.session['logged_in_as']=user_info.id
		print request.session['logged_in_as']
		return redirect(reverse('belt2:index'))

def login (request):
	result=User.objects.validate_login(request.POST['username'],request.POST['password'])
	if type(result)==list:
		for error in result:
			messages.warning(request, error)
			return redirect(reverse('login:index'))
	else:
		user_info=User.objects.get(username=request.POST['username'])
		print user_info
		request.session['logged_in_as']=user_info.id
		return redirect(reverse('belt2:index'))
		

def logout(request):
	request.session.pop('logged_in_as')
	return redirect(reverse('login:index'))



# Create your views here.
