from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$',views.index, name='index'),
	url(r'^poke/(?P<id>\d+)$',views.poke,name='poke')
	# url(r'^login$', views.login,name='login'),
	# url(r'^registration$', views.registration,name='registration')
	# url(r'^delete/(?P<id>\d+)$',views.delete),
	# url(r'^delete/confirm/(?P<id>\d+)$',views.confirm)
]