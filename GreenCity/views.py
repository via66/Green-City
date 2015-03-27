
from django.http import HttpResponse
from django.template import RequestContext, loader, Context
from GreenCity.models import Feature, Park, CommunityGarden, CommunityFoodMarket, GreenCityProject, BikeRack, UserProfile
from django.core import serializers
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from GreenCity.forms import UserForm, UserProfileForm
from itertools import chain
import json

# Create your views here.


def home(request):
	features = Feature.objects.select_subclasses()
	return render(request, 'GreenCity/home.html', {'features': features})


def filter(request):
	print 'Raw Data: "%s"' % request.body 
	search = request.POST.get('searchBox', '')

	data = {}
	features = request.POST.getlist('feature')
	for f in features:
		new_data = []
		if f == "Park" :
			data = list(chain(data, Park.objects.filter(keywords__contains = search)))
		elif f == "BikeRack" :
			data = list((chain(data, BikeRack.objects.filter(keywords__contains = search))))
		elif f == "CommunityMarket" :
			data = list((chain(data, CommunityFoodMarket.objects.filter(keywords__contains = search))))
		elif f == "CommunityGarden" :
			data = list((chain(data, CommunityGarden.objects.filter(keywords__contains = search))))
		elif f == "GreenCityProject" :
			data = list((chain(data, GreenCityProject.objects.filter(keywords__contains = search))))
		elif f == "ElectricVehicleChargingStation" :
			data = list((chain(data, ElectricVehicleChargingStation.objects.filter(keywords__contains = search))))

	# temp return all features
	data = serializers.serialize("json", Feature.objects.all())	
	return HttpResponse(data, content_type="application/json")

def register(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()

			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			profile.save()

			registered = True
		else:
			print user_form.errors, profile_form.errors

	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request,
			'GreenCity/register.html',
			{'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

def user_login(request):
	context_dict = {}
	user_not_found = False
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/')
			else:
				return HttpResponse("Your account is disabled.")
		else:
			user_not_found = True
			return render(request, 'GreenCity/login.html', {'user_not_found':user_not_found})
	else:
		return render(request, 'GreenCity/login.html', {})

@login_required
def restricted(request):
	return HttpResponse("Only logged in users can see this text!")

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')