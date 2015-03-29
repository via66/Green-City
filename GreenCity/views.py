from django.http import HttpResponse
from django.template import RequestContext, loader, Context
<<<<<<< HEAD
from GreenCity.models import Feature, GreenCityUserProfile, Park, CommunityGarden, CommunityFoodMarket, GreenCityProject, BikeRack, ElectricVehicleChargingStation
=======
from GreenCity.models import Feature, GreenCityUserProfile, Park, CommunityGarden, CommunityFoodMarket, \
    GreenCityProject, BikeRack, ElectricVehicleChargingStation
>>>>>>> 1f2c68c8b3c543ed22ab2a17e45703eab0b3b2ea
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
    latitude = request.POST.get('latitude', '')
    longitude = request.POST.get('longitude', '')
    proximity = request.POST.get('distance')
    print(proximity)

    data = {}
    features = request.POST.getlist('feature')

    for f in features:
        if f == "Park":
            if proximity == "":
                data = list(chain(data, Park.objects.filter(
                    Q(name__icontains=search) | Q(neighbourhoodName__icontains=search))))
            elif proximity != "":
                data = list(
                    chain(data, Park.objects.filter(Q(name__icontains=search) | Q(neighbourhoodName__icontains=search),
                                                    (Q(longitude__gte=(
                                                        float(longitude) - (float(proximity) / 111.321)))),
                                                    (Q(longitude__lte=(
                                                        float(longitude) + (float(proximity) / 111.321)))),
                                                    (Q(latitude__gte=(float(latitude) - (float(proximity) / 111)))),
                                                    (Q(latitude__lte=(float(latitude) + (float(proximity) / 111))))
                    )))

        elif f == "BikeRack":
            if proximity == "":
                data = list(chain(data, BikeRack.objects.filter(Q(name__icontains=search))))
            elif proximity != "":
                data = list(chain(data, BikeRack.objects.filter(Q(name__icontains=search),
                                                                (Q(longitude__gte=(
                                                                    float(longitude) - (float(proximity) / 111.321)))),
                                                                (Q(longitude__lte=(
                                                                    float(longitude) + (float(proximity) / 111.321)))),
                                                                (Q(latitude__gte=(
                                                                    float(latitude) - (float(proximity) / 111)))),
                                                                (Q(latitude__lte=(
                                                                    float(latitude) + (float(proximity) / 111))))
                )))
        elif f == "CommunityMarket":
            if proximity == "":
                data = list(chain(data, CommunityFoodMarket.objects.filter(
                    Q(name__icontains=search) | Q(marketType__icontains=search) | Q(operator__icontains=search) | Q(
                        offerings__icontains=search))))
            elif proximity != "":
                data = list(chain(data, CommunityFoodMarket.objects.filter((Q(name__icontains=search) | Q(
                    marketType__icontains=search) | Q(operator__icontains=search) | Q(offerings__icontains=search)),
                                                                           (Q(longitude__gte=(float(longitude) - (
                                                                               float(proximity) / 111.321)))),
                                                                           (Q(longitude__lte=(float(longitude) + (
                                                                               float(proximity) / 111.321)))),
                                                                           (Q(latitude__gte=(float(latitude) - (
                                                                               float(proximity) / 111)))),
                                                                           (Q(latitude__lte=(
                                                                               float(latitude) + (float(proximity) / 111))))
                )))
        elif f == "CommunityGarden":
            if proximity == "":
                data = list(chain(data, CommunityGarden.objects.filter(
                    Q(name__icontains=search) | Q(foodTreeVarieties__icontains=search) | Q(
                        stewarsOrManagingOrganization__icontains=search))))
            elif proximity != "":
                data = list(chain(data, CommunityGarden.objects.filter((Q(name__icontains=search) | Q(
                    foodTreeVarieties__icontains=search) | Q(stewarsOrManagingOrganization__icontains=search)),
                                                                       (Q(longitude__gte=(float(longitude) - (
                                                                           float(proximity) / 111.321)))),
                                                                       (Q(longitude__lte=(float(longitude) + (
                                                                           float(proximity) / 111.321)))),
                                                                       (Q(latitude__gte=(
                                                                           float(latitude) - (float(proximity) / 111)))),
                                                                       (Q(latitude__lte=(
                                                                           float(latitude) + (float(proximity) / 111))))
                )))
        elif f == "GreenCityProject":
            if proximity == "":
                data = list(chain(data, GreenCityProject.objects.filter(
                    Q(name__icontains=search) | Q(shortDescription__icontains=search))))
            elif proximity != "":
                data = list(chain(data, GreenCityProject.objects.filter(
                    (Q(name__icontains=search) | Q(shortDescription__icontains=search) ),
                    (Q(longitude__gte=(float(longitude) - (float(proximity) / 111.321)))),
                    (Q(longitude__lte=(float(longitude) + (float(proximity) / 111.321)))),
                    (Q(latitude__gte=(float(latitude) - (float(proximity) / 111)))),
                    (Q(latitude__lte=(float(latitude) + (float(proximity) / 111))))
                )))
        elif f == "ElectricVehicleChargingStation":
            if proximity == "":
                data = list(chain(data, ElectricVehicleChargingStation.objects.filter(
                    Q(name__icontains=search) | Q(lotOperator__icontains=search))))
            elif proximity != "":
                data = list(chain(data, ElectricVehicleChargingStation.objects.filter(
                    (Q(name__icontains=search) | Q(lotOperator__icontains=search) ),
                    (Q(longitude__gte=(float(longitude) - (float(proximity) / 111.321)))),
                    (Q(longitude__lte=(float(longitude) + (float(proximity) / 111.321)))),
                    (Q(latitude__gte=(float(latitude) - (float(proximity) / 111)))),
                    (Q(latitude__lte=(float(latitude) + (float(proximity) / 111))))
                )))

    return render(request, 'GreenCity/filterData.json', {'features': data})


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

            authenticated_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request, authenticated_user)
            return render(request,
                          'GreenCity/register.html',
                          {'registered': registered})
        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'GreenCity/register.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


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
            return render(request, 'GreenCity/login.html', {'user_not_found': user_not_found})
    else:
        return render(request, 'GreenCity/login.html', {})


@login_required
def restricted(request):
    return HttpResponse("Only logged in users can see this text!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
