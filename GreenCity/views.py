from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader, Context
from GreenCity.models import Feature

# Create your views here.


def home(request):
    print "in home view"
    features = Feature.objects.select_subclasses()
    return render(request, 'GreenCity/home.html', {'features': features})


def map(request):
    features = Feature.objects.select_subclasses()
    template = loader.get_template('GreenCity/map.html')
    context = RequestContext(request, {'features': features})
    return HttpResponse(template.render(context))
