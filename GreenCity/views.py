from django.http import HttpResponse
from django.template import RequestContext, loader, Context
from GreenCity.models import Feature, Park, CommunityGarden, CommunityFoodMarket, \
    GreenCityProject, BikeRack, ElectricVehicleChargingStation 
from django.core import serializers
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from GreenCity.forms import UserForm
from itertools import chain
from django.db.models import Q
import json

# Create your views here.
KM_PER_LAT = 111
KM_PER_LONG = 111.321

def home(request):
    features = Feature.objects.select_subclasses()
    return render(request, 'GreenCity/home.html', {'features': features})

def save(request):
    features = Feature.objects.select_subclasses()
    uname = request.session['uname']
    uname1 = request.session['uname1']
    zoomLevel = request.COOKIES.get(uname, '')
    ll = request.COOKIES.get(uname1, '')
    print zoomLevel
    print ll
    if zoomLevel == '' or zoomLevel == 'None':
        request.session['logl'] = 12 # default zoom at 12, upon first login
    else:
        request.session['logl'] = zoomLevel
    if ll == '' or ll == 'None':
        request.session['lls'] = (49.2827, -123.1207)
    else:
        request.session['lls'] = ll
    print "session key:"
    print request.session.session_key
    # print "Hello " + request.session['uname'] + " I notice this is your session"
    return render(request, 'GreenCity/home_save.html', {'features': features})


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
                                                        float(longitude) - (float(proximity) / KM_PER_LONG)))),
                                                    (Q(longitude__lte=(
                                                        float(longitude) + (float(proximity) / KM_PER_LONG)))),
                                                    (Q(latitude__gte=(float(latitude) - (float(proximity) / KM_PER_LAT)))),
                                                    (Q(latitude__lte=(float(latitude) + (float(proximity) / KM_PER_LAT))))
                    )))

        elif f == "BikeRack":
            if proximity == "":
                data = list(chain(data, BikeRack.objects.filter(Q(name__icontains=search))))
            elif proximity != "":
                data = list(chain(data, BikeRack.objects.filter(Q(name__icontains=search),
                                                                (Q(longitude__gte=(
                                                                    float(longitude) - (float(proximity) / KM_PER_LONG)))),
                                                                (Q(longitude__lte=(
                                                                    float(longitude) + (float(proximity) / KM_PER_LONG)))),
                                                                (Q(latitude__gte=(
                                                                    float(latitude) - (float(proximity) / KM_PER_LAT)))),
                                                                (Q(latitude__lte=(
                                                                    float(latitude) + (float(proximity) / KM_PER_LAT))))
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
                                                                               float(proximity) / KM_PER_LONG)))),
                                                                           (Q(longitude__lte=(float(longitude) + (
                                                                               float(proximity) / KM_PER_LONG)))),
                                                                           (Q(latitude__gte=(float(latitude) - (
                                                                               float(proximity) / KM_PER_LAT)))),
                                                                           (Q(latitude__lte=(
                                                                               float(latitude) + (float(proximity) / KM_PER_LAT))))
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
                                                                           float(proximity) / KM_PER_LONG)))),
                                                                       (Q(longitude__lte=(float(longitude) + (
                                                                           float(proximity) / KM_PER_LONG)))),
                                                                       (Q(latitude__gte=(
                                                                           float(latitude) - (float(proximity) / KM_PER_LAT)))),
                                                                       (Q(latitude__lte=(
                                                                           float(latitude) + (float(proximity) / KM_PER_LAT))))
                )))
        elif f == "GreenCityProject":
            if proximity == "":
                data = list(chain(data, GreenCityProject.objects.filter(
                    Q(name__icontains=search) | Q(shortDescription__icontains=search))))
            elif proximity != "":
                data = list(chain(data, GreenCityProject.objects.filter(
                    (Q(name__icontains=search) | Q(shortDescription__icontains=search) ),
                    (Q(longitude__gte=(float(longitude) - (float(proximity) / KM_PER_LONG)))),
                    (Q(longitude__lte=(float(longitude) + (float(proximity) / KM_PER_LONG)))),
                    (Q(latitude__gte=(float(latitude) - (float(proximity) / KM_PER_LAT)))),
                    (Q(latitude__lte=(float(latitude) + (float(proximity) / KM_PER_LAT))))
                )))
        elif f == "ElectricVehicleChargingStation":
            if proximity == "":
                data = list(chain(data, ElectricVehicleChargingStation.objects.filter(
                    Q(name__icontains=search) | Q(lotOperator__icontains=search))))
            elif proximity != "":
                data = list(chain(data, ElectricVehicleChargingStation.objects.filter(
                    (Q(name__icontains=search) | Q(lotOperator__icontains=search) ),
                    (Q(longitude__gte=(float(longitude) - (float(proximity) / KM_PER_LONG)))),
                    (Q(longitude__lte=(float(longitude) + (float(proximity) / KM_PER_LONG)))),
                    (Q(latitude__gte=(float(latitude) - (float(proximity) / KM_PER_LAT)))),
                    (Q(latitude__lte=(float(latitude) + (float(proximity) / KM_PER_LAT))))
                )))

    return render(request, 'GreenCity/filterData.json', {'features': data})


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            registered = True

            authenticated_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request, authenticated_user)
            return render(request,
                          'GreenCity/login.html',
                          {'registered': registered})
        else:
            print user_form.errors

    else:
        user_form = UserForm()

    return render(request,
                  'GreenCity/register.html',
                  {'form': user_form.as_p, 'registered': registered})


def user_login(request):
    context_dict = {}
    user_not_found = False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        request.session['uname'] = username;
        request.session['uname1'] = username + "zlkasdh3278"; # this is for cookies, i cant map multiple values to one key...make as many as necessar
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                uname_get = request.session['uname']
                print "Hello " + uname_get + " I notice this is your session."
                return HttpResponseRedirect('/saved/')
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
    request.session['logl'] = request.POST.get('lll')
    request.session['lls'] = request.POST.get('latlng')
    print request.session['lls']
    print request.session['logl']
    lls = request.session['lls']
    uname = request.session['uname']
    uname1 = request.session['uname1']
    logl = request.session['logl']
    response = HttpResponseRedirect('/')
    response.set_cookie(uname, uname, max_age = 365*24*60*60) # cookie set for one year
    response.set_cookie(uname, logl, max_age = 365*24*60*60)
    response.set_cookie(uname1, uname1, max_age = 365*24*60*60)
    response.set_cookie(uname1, lls, max_age = 365*24*60*60)
    logout(request)
    return response