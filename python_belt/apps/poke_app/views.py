from django.shortcuts import render,redirect
from django.db.models import Count
from django.core.urlresolvers import reverse
from ..login_app.models import User,UserManager
from .models import Poke

def index(request):
	if 'logged_in_as' in request.session:
		user_data=User.objects.get(id=request.session['logged_in_as'])
		name=user_data.name
		user_id=request.session['logged_in_as']
		a=User.objects.all().annotate(count=Count('user_poked')).values('id','name','email','alias','count')
		count=Poke.objects.filter(poked_id=request.session['logged_in_as']).values('poker__name').annotate(count=Count('id'))
		
		context={'data':a,'name':name,'your_poked':count,'user_id':user_id}
		return render (request,'poke_app/index.html',context)

	else:
		return redirect (reverse('login:logout'))

def poke(request,id):
	poker=User.objects.get(id=request.session['logged_in_as'])
	poked=User.objects.get(id=id)
	insert=Poke.objects.create(poker=poker,poked=poked)
	insert.save()
	return redirect (reverse('poke:index'))
