from django.contrib import admin
from adminapp.models import Park, GreenCityProject, ElectricVehicleChargingStation, BikeRack, CommunityFoodMarket, CommunityGarden, DatasetLink
from django.contrib import admin
from django.shortcuts import render
from django.core.urlresolvers import reverse

class ParkAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name',               {'fields': ['name']}),
        ('Lat/Long', {'fields': ['longitude', 'latitude']}),
        ('Street', {'fields': ['streetNumber', 'streetName']}),
        ('Hectare', {'fields': ['hectare']}),
        ('Neighbourhood', {'fields': ['neighbourhoodName', 'neighbourhoodURL']}),
        ('Washrooms', {'fields': ['washrooms']}),
    ]
    list_display = ('name', 'longitude', 'latitude', 'streetNumber', 'streetName',
                    'hectare', 'neighbourhoodName', 'neighbourhoodURL',
                    'washrooms')
    
class BikeRackAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Street', {'fields': ['streetNumber', 'streetName']}),
        ('Lat/Long', {'fields': ['longitude', 'latitude']}),
        ('Number of racks', {'fields': ['numberOfRacks']}),
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
    ]
    list_display = ('name', 'longitude', 'latitude', 'address', 'category1',
                    'category2', 'shortDescription', 'url1', 'url2', 'url3')

class ChargingStationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name',               {'fields': ['name']}),
        ('Lat/Long', {'fields': ['longitude', 'latitude']}),
        ('Address ', {'fields': ['address']}),
        ('Lot Operator', {'fields': ['lotOperator']})
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
        ('Url', {'fields': ['url']})
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
        opts = obj._meta
        verbose_name = opts.verbose_name
        module_name = opts.module_name
        pk_value = obj._get_pk_val()
        url_to_parse = DatasetLink.objects.get(pk = pk_value)
        if '_update' in request.POST:
            print(url_to_parse)
            valid = DatasetLink.objects.filter(url_link__endswith='.csv')
            print(valid)
            if valid.exists():
                print('url valid')
            else:
                print('url not valid')
            return render(request, 'admin/success_display.html', {})

                 #  return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

admin.site.register(DatasetLink, DatasetLinkAdmin)
admin.site.register(Park, ParkAdmin)
admin.site.register(GreenCityProject, GreenCityProjectAdmin)
admin.site.register(ElectricVehicleChargingStation,ChargingStationAdmin)
admin.site.register(BikeRack, BikeRackAdmin)
admin.site.register(CommunityFoodMarket, FoodMarketAdmin)
admin.site.register(CommunityGarden, GardenAdmin)
