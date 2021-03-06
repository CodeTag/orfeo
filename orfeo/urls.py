from django.conf.urls import patterns, include, url
from views import *
from django.contrib.auth.views import logout

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'orfeo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^',include('apps.playlist.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social_auth.urls')),
    url(r'^',include('apps.search.urls')),
    url(r'^',include('apps.auth.urls')),
    url(r'^login/', login, name='login'),
    url(r'^logout/', 'django.contrib.auth.views.logout_then_login', name='logout'),

)
