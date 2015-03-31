from django.contrib import admin
from models import Feature, Park, GreenCityProject, ElectricVehicleChargingStation, BikeRack, CommunityFoodMarket, CommunityGarden, DatasetLink, NewUser
from django.contrib import admin
from django.shortcuts import render, HttpResponseRedirect
from parsers.parkParser import parsePark
from parsers.communityGardenParser import parseCommunityGardens
from parsers.bikeRackParser import parseBikeRack
from parsers.communityFoodMarketParser import parseCommunityFoodMarket
from parsers.electricVehicleChargingStationParser import parseElectricVehicleChargingStation
from parsers.greenCityProjectParser import parseGreenCityProject




admin.site.register(Feature)

class ParkAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name',               {'fields': ['name']}),
        ('Lat/Long', {'fields': ['longitude', 'latitude']}),
        ('Street', {'fields': ['streetNumber', 'streetName']}),
        ('Hectare', {'fields': ['hectare']}),
        ('Neighbourhood', {'fields': ['neighbourhoodName', 'neighbourhoodURL']}),
        ('Washrooms', {'fields': ['washrooms']}),
        #('Keywords', {'fields': ['keywords']}),
    ]
    list_display = ('name', 'longitude', 'latitude', 'streetNumber', 'streetName',
                    'hectare', 'neighbourhoodName', 'neighbourhoodURL',
                    'washrooms')
    

class BikeRackAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Street', {'fields': ['streetNumber', 'streetName', 'streetSide']}),
        ('Lat/Long', {'fields': ['longitude', 'latitude']}),
        ('Number of racks', {'fields': ['numberOfRacks']}),
        #('Keywords', {'fields': ['keywords']}),
    ]
    list_display = ('streetNumber', 'streetName', 'numberOfRacks')
    

class GreenCityProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name',               {'fields': ['name']}),
        ('Lat/Long', {'fields': ['longitude', 'latitude']}),
        ('Address', {'fields': ['address']}),
        ('Categories', {'fields': ['category1', 'category2']}),
        ('Description', {'fields': ['shortDescription']}),
        ('URLs', {'fields': ['url1', 'url2', 'url3']}),
        #('Keywords', {'fields': ['keywords']}),
    ]
    list_display = ('name', 'longitude', 'latitude', 'address', 'category1',
                    'category2', 'shortDescription', 'url1', 'url2', 'url3')


class ChargingStationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name',               {'fields': ['name']}),
        ('Lat/Long', {'fields': ['longitude', 'latitude']}),
        ('Address ', {'fields': ['address']}),
        ('Lot Operator', {'fields': ['lotOperator']}),
        #('Keywords', {'fields': ['keywords']}),
        ]
    list_display = ('name', 'longitude', 'latitude', 'address', 'lotOperator')


class FoodMarketAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name',               {'fields': ['name']}),
        ('Lat/Long', {'fields': ['longitude', 'latitude']}),
        ('Street', {'fields': ['streetNumber', 'streetName']}),
        ('Market Type', {'fields': ['marketType']}),
        ('Year', {'fields': ['year']}),
        ('Operator', {'fields': ['operator']}),
        ('Day', {'fields': ['day']}),
        ('Hours', {'fields': ['openHours', 'closeHours']}),
        ('Months of Operation', {'fields': ['monthsOfOperations']}),
        ('Number of Vendors', {'fields': ['numberOfVendors']}),
        ('Offerings', {'fields': ['offerings']}),
        #('Keywords', {'fields': ['keywords']}),
    ]
    list_display = ('name', 'longitude', 'latitude', 'year', 'marketType', 'operator',
                    'streetNumber', 'streetName', 'url', 'day', 'openHours', 'closeHours',
                    'monthsOfOperations', 'numberOfVendors', 'offerings')


class GardenAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name',               {'fields': ['name']}),
        ('Lat/Long', {'fields': ['longitude', 'latitude']}),
        ('Street', {'fields': ['streetNumber', 'streetName']}),
        ('Number of Plots', {'fields': ['numberOfPlots']}),
        ('Food Trees', {'fields': ['numberOfFoodTrees', 'foodTreeVarieties']}),
        ('Jurisdiction', {'fields': ['jurisdiction']}),
        ('Managing Organization', {'fields': ['stewarsOrManagingOrganization']}),
        ('Email', {'fields': ['publicEmail']}),
        ('Url', {'fields': ['url']}),
        #('Keywords', {'fields': ['keywords']}),
    ]
    list_display = ('name', 'longitude', 'latitude', 'streetNumber', 'streetName', 'numberOfPlots',
                    'numberOfFoodTrees', 'foodTreeVarieties', 'jurisdiction', 'stewarsOrManagingOrganization',
                    'publicEmail', 'url')
    

class DatasetLinkAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title',               {'fields': ['url_title']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ('Link', {'fields': ['url_link']}),
    ]
    list_display = ('url_title', 'url_link', 'pub_date')

    def response_change(self, request, obj):
        if '_update' in request.POST:
            opts = obj._meta
            verbose_name = opts.verbose_name
            module_name = opts.module_name
            pk_value = obj._get_pk_val()
            #pass url_to_parse to the correct parser
            url_to_parse = DatasetLink.objects.get(pk = pk_value).url_link
            print(url_to_parse) 
            validGarden = DatasetLink.objects.filter(url_link__endswith='ftp://webftp.vancouver.ca/OpenData/csv/CommunityGardensandFoodTrees.csv' , pk = pk_value)
            validMarket = DatasetLink.objects.filter(url_link__endswith='ftp://webftp.vancouver.ca/OpenData/csv/CommunityFoodMarketsandFarmersMarkets.csv' , pk = pk_value)
            validPark = DatasetLink.objects.filter(url_link__endswith= 'ftp://webftp.vancouver.ca/OpenData/csv/parks.csv', pk = pk_value)
            validCharge = DatasetLink.objects.filter(url_link__endswith='ftp://webftp.vancouver.ca/OpenData/csv/electric_vehicle_charging_stations.csv' , pk = pk_value)
            validProject = DatasetLink.objects.filter(url_link__endswith='ftp://webftp.vancouver.ca/OpenData/csv/greenest_city_projects.csv' , pk = pk_value)
            validBike = DatasetLink.objects.filter(url_link__endswith='ftp://webftp.vancouver.ca/opendata/bike_rack/BikeRackData.csv' , pk = pk_value)

            if validGarden.exists():
                print('Valid Garden Url')
                try:
                    parseCommunityGardens(url_to_parse)
                    return render(request, 'admin/success_display.html', {})
                except:
                    return render(request, 'admin/duplicate_display.html', {})
            elif validMarket.exists():
                print('Valid Market Url')
                try:
                    parseCommunityFoodMarket(url_to_parse)
                    return render(request, 'admin/success_display.html', {})
                except:
                    return render(request, 'admin/duplicate_display.html', {})
            elif validPark.exists():
                print('Valid Park Url')
                try:
                    parsePark(url_to_parse)
                    return render(request, 'admin/success_display.html', {})
                except:
                    return render(request, 'admin/duplicate_display.html', {})
            elif validBike.exists():
                print('Valid Bike Url')
                try:
                    parseBikeRack(url_to_parse)
                    return render(request, 'admin/success_display.html', {})
                except:
                    return render(request, 'admin/duplicate_display.html', {})
            elif validCharge.exists():
                print('Valid Charge Url')
                try:
                    parseElectricVehicleChargingStation(url_to_parse)
                    return render(request, 'admin/success_display.html', {})
                except:
                    return render(request, 'admin/duplicate_display.html', {})
            elif validProject.exists():
                print('Valid Project Url')
                try:
                    print(request)
                    parseGreenCityProject(url_to_parse)
                    return render(request, 'admin/success_display.html', {})
                except:
                    print(request)
                    return render(request, 'admin/duplicate_display.html', {})
            else :
                return render(request, 'admin/failure_display.html', {})
        else:
            return HttpResponseRedirect('/admin/GreenCity/datasetlink/')

admin.site.register(DatasetLink, DatasetLinkAdmin)
admin.site.register(Park, ParkAdmin)
admin.site.register(GreenCityProject, GreenCityProjectAdmin)
admin.site.register(ElectricVehicleChargingStation,ChargingStationAdmin)
admin.site.register(BikeRack, BikeRackAdmin)
admin.site.register(CommunityFoodMarket, FoodMarketAdmin)
admin.site.register(CommunityGarden, GardenAdmin)
admin.site.register(NewUser)

