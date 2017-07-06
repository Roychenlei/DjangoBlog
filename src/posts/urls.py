from django.conf.urls import url

from . import views


app_name = 'posts'
urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^(?P<post_id>[0-9]+)$',views.detail,name='detail'),
	url(r'^(?P<post_id>[0-9]+)/results/$',views.results,name='result'),
	url(r'^(?P<post_id>[0-9]+)/vote/$',views.vote,name='vote'),
	]