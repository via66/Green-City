from django.http import HttpResponse
from django.template import RequestContext, loader, Context
from GreenCity.models import Feature, Park, CommunityGarden, CommunityFoodMarket, \
    GreenCityProject, BikeRack, ElectricVehicleChargingStation, NewUser, Favorites
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
from django.db import IntegrityError
import json

# Create your views here.
KM_PER_LAT = 111
KM_PER_LONG = 111.321


def home(request):
    features = Feature.objects.select_subclasses()
    request.session['zoom_level'] = 12
    request.session['lat'] = 49.2827
    request.session['long'] = -123.1207
    if 'uname' not in request.session:
        request.session['uname'] = request.user.username
    if 'uname1' not in request.session:
        request.session['uname1']= request.user.username + 'axdb34' # for cookies
    if request.user.__str__() != "AnonymousUser" and 'uname' in request.session:
        uname = request.session['uname']
        uname1 = request.session['uname1']
        zoomLevel = request.COOKIES.get(uname, '')
        ll = request.COOKIES.get(uname1, '')
        if zoomLevel != '' and zoomLevel is not None:
            request.session['zoom_level'] = zoomLevel
        if ll != '' and ll is not None:
            ll = ll.lstrip('[').rstrip(']').split(',')
            request.session['lat'] = float(ll[0])
            request.session['long'] = float(ll[1])
    return render(request, 'GreenCity/home.html', {'features': features})


def save(request):
    response = HttpResponseRedirect('/')
    if request.user.__str__() != "AnonymousUser":
        save_data = json.loads(request.body)
        # put all the request session stuff here. Save data is a python dictionary.
        # so save_data['zoom_level'] and save_data['lat_long']
        request.session['zoom_level'] = save_data['zoom_level']
        request.session['lat'] = save_data['lat_long']['k']
        request.session['long'] = save_data['lat_long']['D']
        lls = [request.session['lat'], request.session['long']]
        uname = request.session['uname']
        uname1 = request.session['uname1']
        logl = request.session['zoom_level']
        print uname
        print uname1
        print logl
        print lls
        print save_data
        response.set_cookie(uname, uname, max_age = 365*24*60*60)
        response.set_cookie(uname, logl, max_age = 365*24*60*60)
        response.set_cookie(uname1, uname1, max_age = 365*24*60*60)
        response.set_cookie(uname1, lls, max_age = 365*24*60*60)
    return response

@login_required()
def save_favorite(request):
    save_data = json.loads(request.body)
    try:
        feat_obj = Feature.objects.get(name=save_data['obj'])
        new, p = Favorites.objects.get_or_create(newuser=request.user, favorites=feat_obj)
        print p
    except:
        print "fail"
    return HttpResponse("worked")

@login_required()
def remove_favorite(request):
    save_data = json.loads(request.body)
    feat_obj = Feature.objects.get(name=save_data['obj'])
    toDel = Favorites.objects.filter(newuser=request.user, favorites=feat_obj)
    toDel.delete()
    return HttpResponse("worked")


def filter(request):
    search = latitude = longitude = proximity = features = ""
    if(request.method == "POST"):
        search = request.POST.get('searchBox', '')
        latitude = request.POST.get('latitude', '')
        longitude = request.POST.get('longitude', '')
        proximity = request.POST.get('distance')
        features = request.POST.getlist('feature')
    else:
        search = request.GET.get('searchBox', '')
        latitude = request.GET.get('latitude', '')
        longitude = request.GET.get('longitude', '')
        proximity = request.GET.get('distance')
        features = request.GET.getlist('feature')

    data = {}

    for f in features:
        if f == "Park":
            if (proximity == "" or longitude == "" or latitude == ""):
                data = list(chain(data, Park.objects.filter(
                    Q(name__icontains=search) | Q(neighbourhoodName__icontains=search))))
            elif proximity != "":
                data = list(
                    chain(data, Park.objects.filter(Q(name__icontains=search) | Q(neighbourhoodName__icontains=search),
                                                    (Q(longitude__gte=(
                                                        float(longitude) - (float(proximity) / KM_PER_LONG)))),
                                                    (Q(longitude__lte=(
                                                        float(longitude) + (float(proximity) / KM_PER_LONG)))),
                                                    (Q(latitude__gte=(
                                                        float(latitude) - (float(proximity) / KM_PER_LAT)))),
                                                    (Q(latitude__lte=(
                                                        float(latitude) + (float(proximity) / KM_PER_LAT))))
                    )))

        elif f == "BikeRack":
            if (proximity == "" or longitude == "" or latitude == ""):
                data = list(chain(data, BikeRack.objects.filter(Q(name__icontains=search))))
            elif proximity != "":
                data = list(chain(data, BikeRack.objects.filter(Q(name__icontains=search),
                                                                (Q(longitude__gte=(
                                                                    float(longitude) - (
                                                                        float(proximity) / KM_PER_LONG)))),
                                                                (Q(longitude__lte=(
                                                                    float(longitude) + (
                                                                        float(proximity) / KM_PER_LONG)))),
                                                                (Q(latitude__gte=(
                                                                    float(latitude) - (
                                                                        float(proximity) / KM_PER_LAT)))),
                                                                (Q(latitude__lte=(
                                                                    float(latitude) + (float(proximity) / KM_PER_LAT))))
                )))
        elif f == "CommunityMarket":
            if (proximity == "" or longitude == "" or latitude == ""):
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
                                                                               float(latitude) + (
                                                                                   float(proximity) / KM_PER_LAT))))
                )))
        elif f == "CommunityGarden":
            if (proximity == "" or longitude == "" or latitude == ""):
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
                                                                           float(latitude) - (
                                                                               float(proximity) / KM_PER_LAT)))),
                                                                       (Q(latitude__lte=(
                                                                           float(latitude) + (
                                                                               float(proximity) / KM_PER_LAT))))
                )))
        elif f == "GreenCityProject":
            if (proximity == "" or longitude == "" or latitude == ""):
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
            if (proximity == "" or longitude == "" or latitude == ""):
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

    if(request.method == "POST"):
        return render(request, 'GreenCity/filterData.json', {'features': data})
    else:
        return render(request, 'GreenCity/home.html', {'features': data})


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
            return HttpResponseRedirect('/')
        else:
            print user_form.errors

    else:
        user_form = UserForm()

    return render(request,
                  'GreenCity/register.html',
                  {'form': user_form, 'registered': registered})


def user_login(request):
    context_dict = {}
    user_not_found = False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        request.session['uname'] = username
        request.session['pass'] = password
        request.session['uname1'] = username + "zlkasdh3278" # this is for cookies, i cant map multiple values to one key...make as many as necessar
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
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')
        else:
            return render(request, 'GreenCity/login.html', {})


@login_required
def restricted(request):
    return HttpResponse("Only logged in users can see this text!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
