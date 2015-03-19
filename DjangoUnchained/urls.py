from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', 'GreenCity.views.home', name='home'),
                       # url(r'^index/', 'GreenCity.views.map', name='map'),
                       # user auth urls
                       url(r'^accounts/login/$', 'GreenCity.views.login'),
                       url(r'^accounts/auth/$', 'GreenCity.views.auth_view'),
                       url(r'^accounts/logout/$', 'GreenCity.views.logout'),
                       url(r'^accounts/loggedin/$', 'GreenCity.views.loggedin'),
                       url(r'^accounts/invalid/$', 'GreenCity.views.invalid_login'),
)
