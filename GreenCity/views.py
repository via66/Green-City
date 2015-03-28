
from django.http import HttpResponse
from django.template import RequestContext, loader, Context
from GreenCity.models import Feature, GreenCityUserProfile, Park, CommunityGarden, CommunityFoodMarket, GreenCityProject, BikeRack
from django.core import serializers
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from GreenCity.forms import UserForm, UserProfileForm
from itertools import chain
from django.db.models import Q
import json

# Create your views here.

def home(request):
	features = Feature.objects.select_subclasses()
	return render(request, 'GreenCity/home.html', {'features': features})


def filter(request):
	# print 'Input Data: "%s"' % request.body 
	search = request.POST.get('searchBox', '')

	data = {}
	features = request.POST.getlist('feature')

	for f in features:
		new_data = []
		if f == "Park" :
			data = list(chain(data, Park.objects.filter( Q(name__icontains = search) | Q(neighbourhoodName__icontains = search) )))
		elif f == "BikeRack" :
			data = list(chain(data, BikeRack.objects.filter( Q(name__icontains = search) )))
		elif f == "CommunityMarket" :
			data = list(chain(data, CommunityFoodMarket.objects.filter( Q(name__icontains = search) | Q(marketType__icontains = search) | Q(operator__icontains = search) | Q(offerings__icontains = search) )))
		elif f == "CommunityGarden" :
			data = list(chain(data, CommunityGarden.objects.filter( Q(name__icontains = search) | Q(foodTreeVarieties__icontains = search) | Q(stewardsOrManagingOrganization__icontains = search) )))
		elif f == "GreenCityProject" :
			data = list(chain(data, GreenCityProject.objects.filter( Q(name__icontains = search) | Q(shortDescription__icontains = search) )))
		elif f == "ElectricVehicleChargingStation" :
			data = list(chain(data, ElectricVehicleChargingStation.objects.filter( Q(name__icontains = search) | Q(lotOperator__icontains = search) )))

	return render(request, 'GreenCity/filterData.json', { 'features': data } )

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
			
			authenticated_user = authenticate(username=request.POST['username'],password=request.POST['password'])
			login(request, authenticated_user)
			return render(request,
			'GreenCity/register.html',
			{'registered': registered} )
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