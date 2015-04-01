from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'GreenCity.views.home', name='home'),
	url(r'^filter/', 'GreenCity.views.filter', name='filter'),
	# url(r'^index/', 'GreenCity.views.map', name='map'),
	# user auth urls
	url(r'^login/$', 'GreenCity.views.user_login',name='login'),
	url(r'^register/$', 'GreenCity.views.register',name='register'),
	url(r'^restricted/$', 'GreenCity.views.restricted',name='restricted'),
	url(r'^logout/$', 'GreenCity.views.user_logout',name='logout'),
	url(r'^save/$', 'GreenCity.views.save', name='save'),
    url(r'^save_favorite/$', 'GreenCity.views.save_favorite', name='save_f'),

	#django-facebook integration
	(r'^facebook/', include('django_facebook.urls')),
	(r'^accounts/', include('django_facebook.auth_urls')), #Don't add this line if you use django registration or userena for registration and auth.
)
