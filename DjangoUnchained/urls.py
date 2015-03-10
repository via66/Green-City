from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'GreenCity.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^index/', 'GreenCity.views.map', name='map'),
                       url(r'^admin/', include(admin.site.urls)),
)
