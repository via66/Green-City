from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', 'GreenCity.views.home', name='home'),
                       # url(r'^index/', 'GreenCity.views.map', name='map'),
                       # user auth urls
                       url(r'^login/$', 'GreenCity.views.user_login',name='login'),
                       url(r'^register/$', 'GreenCity.views.register',name='register'),
                       url(r'^restricted/$', 'GreenCity.views.restricted',name='restricted'),
                       url(r'^logout/$', 'GreenCity.views.user_logout',name='logout'),
)
