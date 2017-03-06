from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$',views.index, name='index'),
	url(r'^view/(?P<id>\d+)$',views.view,name='view'),
	url(r'^add/',views.add,name='add'),
	url(r'^process/',views.process,name='process'),
	url(r'^join/(?P<id>\d+)$',views.join,name='join'),
# 	url(r'^login$', views.login,name='login'),
# 	url(r'^registration$', views.registration,name='registration'),
# 	# url(r'^delete/confirm/(?P<id>\d+)$',views.confirm)
]