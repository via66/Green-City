from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader, Context
from GreenCity.models import Feature

# Create your views here.


def home(request):
    features = Feature.objects.select_subclasses()
    return render(request, '../templates/GreenCity/home.html', {'features': features})
