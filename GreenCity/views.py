
from django.http import HttpResponse
from django.template import RequestContext, loader, Context
from GreenCity.models import Feature
from django.core import serializers
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
import json

# Create your views here.


def home(request):
    features = Feature.objects.select_subclasses()
    return render(request, '../templates/GreenCity/home.html', {'features': features})


def filter(request):
	# temporarily returning all Features
	data = serializers.serialize("json", Feature.objects.all())	
	return HttpResponse(data, content_type="application/json")

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    return render_to_response('loggedin.html', { 'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

