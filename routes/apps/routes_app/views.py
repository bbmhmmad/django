from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from .models import Product

def index(request):
	context={'data':Product.objects.all()}
	return render(request,'index.html',context)

def new(request):
	return render(request,'new.html')

def create(request):
	insert=Product(name=request.POST['name'],description=request.POST['description'],price=request.POST['price'])
	insert.save()
	return redirect (reverse('products:index'))

def show(request,id):
	print Product.objects.get(id=id)
	context={'data':Product.objects.get(id=id)}
	print context
	return render (request,'show.html',context)

def edit(request,id):
	context={'data':Product.objects.get(id=id)}
	return render (request,'edit.html',context)

def update(request,id):
	instance=Product.objects.get(id=id)
	instance.name=request.POST['name']
	instance.save()
	instance.description=request.POST['description']
	instance.save()
	instance.price=request.POST['price']
	instance.save()
	return redirect (reverse('products:index'))

def destroy	(request,id):
	Product.objects.filter(id=id).delete()
	return redirect (reverse('products:index'))


# Create your views here.
