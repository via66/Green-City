from django.db import models

# List of models:
# Park, GreenCityProjects, ElectricVehicleChargingStation, BikeRack, CommunityFoodMarket, CommunityGarden

class Feature(models.Model):
	name = models.CharField(max_length=250)
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
	streetNumber = models.CharField(max_length=10)
	streetName = models.CharField(max_length=250)
	numberOfPlots = models.IntegerField()
	numberOfFoodTrees = models.IntegerField()
	foodTreeVarieties = models.CharField(max_length=250)
	jurisdiction = models.CharField(max_length=250)
	stewarsOrManagingOrganization = models.CharField(max_length=250)
	publicEmail = models.EmailField()
	url = models.URLField()


