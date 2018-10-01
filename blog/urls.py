from django.conf.urls import include, url
from django.contrib import admin
from posts import urls
from django.conf import settings
from django.conf.urls.static import static
#import posts
urlpatterns = [
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^posts/', include("posts.urls",namespace='posts')),
    #url(r'^posts/', include(posts.urls)),

    

    
]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

