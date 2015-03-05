from django.db import models

# List of models:
# Park, GreenCityProjects, ElectricVehicleChargingStation, BikeRack, CommunityFoodMarket, CommunityGarden

#Name, StreetNumber, StreetName, Longitude, Latitude, Hectare, NeighbourhoodName,
#NeighbourhoodURL, URL, Washrooms
class Park(models.Model):
	name = models.CharField(max_length=250)
	streetNumber = models.CharField(max_length=250)
	streetName = models.CharField(max_length=250)
	longitude = models.DecimalField(max_digits = 18, decimal_places = 15)
	latitude = models.DecimalField(max_digits = 18, decimal_places = 15)
	hectare = models.DecimalField(max_digits = 6, decimal_places = 2)
	neighbourhoodName = models.CharField(max_length=250)
	neighbourhoodURL = models.URLField()
	url = models.URLField()
	washrooms = models.BooleanField(default = False)

	def __str__(self):
		return self.name

#Name, Category1, Category2, Address, shortDescription, Url1, Url2, Url3, Longitude
#Latitude	
class GreenCityProject(models.Model):
	name = models.CharField(max_length=250)
	category1 = models.CharField(max_length=250)
	category2 = models.CharField(max_length=250)
	address = models.CharField(max_length=250)
	shortDescription = models.TextField()
	url1 = models.URLField()
	url2 = models.URLField()
	url3 = models.URLField() 
	longitude = models.DecimalField(max_digits = 18, decimal_places = 15)
	latitude = models.DecimalField(max_digits = 18, decimal_places = 15)
	
	def __str__(self):
		return self.name
	
#Longitude, Latitude, LotOperator, Address
class ElectricVehicleChargingStation(models.Model):
	longitude = models.DecimalField(max_digits = 18, decimal_places = 15)
	latitude = models.DecimalField(max_digits = 18, decimal_places = 15)
	lotOperator = models.CharField(max_length=250)
	address = models.CharField(max_length=250)
	
	def __str__(self):
		return self.address

#StreetNumber, StreetName, NumberOfRacks, Longitude, Latitude
class BikeRack(models.Model):
	streetNumber = models.CharField(max_length=250)
	streetName = models.CharField(max_length=250)
	numberOfRacks = models.IntegerField()
	longitude = models.DecimalField(max_digits = 18, decimal_places = 15)
	latitude = models.DecimalField(max_digits = 18, decimal_places = 15)
	
	def __str__(self):
		return self.streetNumber + " " + self.streetName

#Name, Year, MarketType, Operator, StreetNumber, StreetName, Url, Day, OpenHours, CloseHours
#MonthsOfOperation, NumberOfVendors, Offerings, Longitude, Latitude	
class CommunityFoodMarket(models.Model):
	name = models.CharField(max_length=250)
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
	longitude = models.DecimalField(max_digits = 18, decimal_places = 15)
	latitude = models.DecimalField(max_digits = 18, decimal_places = 15)

	def __str__(self):
		return self.name

#Name, StreetNumber, StreetName, Longitude, Latitude, NumberOfPlots, NumberOfFoodTrees
#FoodTreeVarieties, Jurisdiction,StewardsOrManagingOrganization, PublicEmail, Url	
class CommunityGarden(models.Model):
	name = models.CharField(max_length=250)
	streetNumber = models.CharField(max_length=10)
	streetName = models.CharField(max_length=250)
	longitude = models.DecimalField(max_digits = 18, decimal_places = 15)
	latitude = models.DecimalField(max_digits = 18, decimal_places = 15)
	numberOfPlots = models.IntegerField()
	numberOfFoodTrees = models.IntegerField()
	foodTreeVarieties = models.CharField(max_length=250)
	jurisdiction = models.CharField(max_length=250)
	stewarsOrManagingOrganization = models.CharField(max_length=250)
	publicEmail = models.EmailField()
	url = models.URLField()

	def __str__(self):
		return self.name


#UrlTitle, UrlLink, PubDate
class ParserUrl(models.Model):
    url_title = models.CharField(max_length=200)
    url_link = models.URLField()
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.url_link
