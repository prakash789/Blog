from django.conf.urls import include, url
from django.contrib import admin
from.views import(

	post_list,
	post_create,
	post_details,
	post_list,
	post_update,
	post_delete,
    register,
    test_cookie,
    track_user
	)
from posts import views 

urlpatterns = [
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   
    url	(r'^$',post_list),
    url(r'^cookie/$', views.test_cookie, name='cookie'),
    url(r'^track_user/$', views.track_user, name='track_user'),
    url(r'^register/$',register,name='register'),
    url	(r'^create/$',post_create,),
    url	(r'^(?P<id>\d+)/$',post_details,name='detail'),
    url	(r'^list/$',post_list,),
    url	(r'^(?P<id>\d+)/edit/$',post_update,name='update'),
    url	(r'^(?P<id>\d+)/delete/$',post_delete),

    

    
]