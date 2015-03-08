from django.db import models

# List of models:
# Park, GreenCityProjects, ElectricVehicleChargingStation, BikeRack, CommunityFoodMarket, CommunityGarden

class Feature(models.Model):
	name = models.CharField(max_length=250, unique=True)
	longitude = models.DecimalField(max_digits = 18, decimal_places = 15)
	latitude = models.DecimalField(max_digits = 18, decimal_places = 15)

	def __str__(self):
		return self.name

class BikeRack(Feature):
	streetNumber = models.CharField(max_length=250)
	streetName = models.CharField(max_length=250)
	numberOfRacks = models.IntegerField()

class Park(Feature):
	streetNumber = models.CharField(max_length=250)
	streetName = models.CharField(max_length=250)
	hectare = models.DecimalField(max_digits = 6, decimal_places = 2)
	neighbourhoodName = models.CharField(max_length=250)
	neighbourhoodURL = models.URLField()
	washrooms = models.BooleanField(default = False)

class GreenCityProject(Feature):
	category1 = models.CharField(max_length=250)
	category2 = models.CharField(max_length=250)
	address = models.CharField(max_length=250)
	shortDescription = models.TextField()
	url1 = models.URLField()
	url2 = models.URLField()
	url3 = models.URLField() 

class ElectricVehicleChargingStation(Feature):
	lotOperator = models.CharField(max_length=250)
	address = models.CharField(max_length=250)

class CommunityFoodMarket(Feature):
	year = models.DateField() #saves year, month and day 
	marketType = models.CharField(max_length=250)
	operator = models.CharField(max_length=250)
	streetNumber = models.CharField(max_length=250)
	streetName = models.CharField(max_length=250)
	url = models.URLField()
	day = models.CharField(max_length=10)
	openHours = models.TimeField()
	closeHours = models.TimeField()
	monthsOfOperations = models.CharField(max_length=250)
	numberOfVendors = models.IntegerField()
	offerings = models.CharField(max_length=250)

class CommunityGarden(Feature):
	streetNumber = models.CharField(max_length=10, blank=True, null=True)
	streetName = models.CharField(max_length=250, blank=True, null=True)
	numberOfPlots = models.IntegerField(blank=True, null=True)
	numberOfFoodTrees = models.IntegerField(blank=True, null=True)
	foodTreeVarieties = models.CharField(max_length=250, blank=True, null=True)
	jurisdiction = models.CharField(max_length=250, blank=True, null=True)
	stewarsOrManagingOrganization = models.CharField(max_length=250, blank=True, null=True)
	publicEmail = models.EmailField(blank=True, null=True)
	url = models.URLField(blank=True, null=True)

#UrlTitle, UrlLink, PubDate
class DatasetLink(models.Model):
    url_title = models.CharField(max_length=200)
    #pk = url_link
    url_link = models.URLField(max_length=200, unique = True)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.url_link
