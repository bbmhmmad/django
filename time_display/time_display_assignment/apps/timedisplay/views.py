from django.shortcuts import render
import time

def index (request):
	time_now={'current_time': time.ctime()}
	return render(request,'index.html',time_now)

