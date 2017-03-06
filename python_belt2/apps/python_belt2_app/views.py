from django.shortcuts import render,redirect
from .models import *
from django.core.urlresolvers import reverse
from django.contrib import messages

def index (request):
	if 'logged_in_as' in request.session:
		trips=Trip.objects.all()
		context={'user_trips':Trip.objects.filter(user__id=request.session['logged_in_as']),'name':User.objects.filter(id=request.session['logged_in_as']),'all_trips':Trip.objects.all(), 'user_id':request.session['logged_in_as']}
		return render (request,'python_belt2_app/index.html',context)
	else:
		return redirect (reverse('login:logout'))

def view (request,id):
	if 'logged_in_as' in request.session:
		context={'data':Trip.objects.filter(id=id)}
		return render (request,'python_belt2_app/view.html',context)
	else:
		return redirect (reverse('login:logout'))

def add (request):
	if 'logged_in_as' in request.session:
		return render (request,'python_belt2_app/add.html')
	else:
		return redirect (reverse('login:logout'))

def join (request,id):
	if 'logged_in_as' in request.session:
		trip=Trip.objects.get(id=id)
		trip.save()
		current_user=User.objects.get(id=request.session['logged_in_as'])
		trip.user.add(current_user)
		return redirect (reverse('belt2:index'))
	else:
		return redirect (reverse('login:logout'))

def process (request):
	if 'logged_in_as' in request.session:
		if request.POST['destination']=='' or request.POST['plan']=='' or request.POST['start']=='' or request.POST['end']=='':
			messages.warning(request, 'No blank entries')
			return redirect (reverse ('belt2:add'))
		if request.POST['start']>request.POST['end']:
			messages.warning(request,"Start date must be before end date.")
			return redirect (reverse ('belt2:add'))
		else:

			trip=Trip(destination=request.POST['destination'],plan=request.POST['plan'],start=request.POST['start'],end=request.POST['end'])
			trip.save()
			current_user=User.objects.get(id=request.session['logged_in_as'])
			trip.user.add(current_user)
			return redirect (reverse('belt2:index'))
	else:
		return redirect (reverse('login:logout'))

