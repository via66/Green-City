from django.contrib import admin
from models import Park, GreenCityProject, ElectricVehicleChargingStation, BikeRack, CommunityFoodMarket, CommunityGarden, DatasetLink
from django.contrib import admin
from django.shortcuts import render
from django.core.urlresolvers import reverse



class PostAdmin(admin.ModelAdmin):
    def response_change(self, request, obj):
        opts = obj._meta
        verbose_name = opts.verbose_name
        module_name = opts.module_name
        pk_value = obj._get_pk_val()
        if '_update' in request.POST:
            return render(request, 'admin/app_index.html', {})

                 #  return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

admin.site.register(DatasetLink, PostAdmin)
admin.site.register(Park)
admin.site.register(GreenCityProject)
admin.site.register(ElectricVehicleChargingStation)
admin.site.register(BikeRack)
admin.site.register(CommunityFoodMarket)
admin.site.register(CommunityGarden)
