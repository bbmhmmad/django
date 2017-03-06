from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$',views.index,name='index'),
	url(r'^new$', views.new,name='new'),
	url(r'^create$', views.create,name='create'),
	url(r'^show/(?P<id>\d+)$',views.show,name='show'),
	url(r'^edit/(?P<id>\d+)$',views.edit,name='edit'),
	url(r'^update/(?P<id>\d+)$',views.update,name='update'),
	url(r'^destroy/(?P<id>\d+)$',views.destroy,name='destroy')
	# url(r'^delete/confirm/(?P<id>\d+)$',views.confirm,name='confirm'),
	# url(r'^management$',views.management,name='management'),
	# url(r'^management_update$',views.management_update,name='management_update')
]