from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader, Context
from GreenCity.models import Feature
from django.core import serializers
import json

# Create your views here.


def home(request):
    features = Feature.objects.select_subclasses()
    return render(request, '../templates/GreenCity/home.html', {'features': features})


def filter(request):
	# temporarily returning all Features
	data = serializers.serialize("json", Feature.objects.all())	
	return HttpResponse(data, content_type="application/json")