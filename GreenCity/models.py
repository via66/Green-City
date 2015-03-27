from django.db import models
from model_utils.managers import InheritanceManager
from django.contrib.auth.models import User

# List of models:
# Park, GreenCityProjects, ElectricVehicleChargingStation, BikeRack, CommunityFoodMarket, CommunityGarden


class Feature(models.Model):
    name = models.CharField(max_length=250)
    longitude = models.FloatField()
    latitude = models.FloatField()
    keywords = models.CharField(max_length=250, default='')
    objects = InheritanceManager()

    def __unicode__(self):
        return self.name


class BikeRack(Feature):
    streetNumber = models.CharField(max_length=250)
    streetName = models.CharField(max_length=250)
    streetSide = models.CharField(max_length=250)
    numberOfRacks = models.IntegerField()
    completeAddress = models.CharField(max_length=250)
    #keywords = models.CharField(max_length=250)

    class Meta:
        unique_together = ('streetSide', 'streetNumber', 'streetName')


class Park(Feature):
    streetNumber = models.CharField(max_length=250)
    streetName = models.CharField(max_length=250)
    hectare = models.DecimalField(max_digits=6, decimal_places=2)
    neighbourhoodName = models.CharField(max_length=250)
    neighbourhoodURL = models.URLField()
    washrooms = models.BooleanField(default=False)
    completeAddress = models.CharField(max_length=250, unique=True)
    #keywords = models.CharField(max_length=250)


class GreenCityProject(Feature):
    category1 = models.CharField(max_length=250)
    category2 = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    shortDescription = models.TextField()
    url1 = models.URLField()
    url2 = models.URLField()
    url3 = models.URLField()
    #keywords = models.CharField(max_length=250)

class ElectricVehicleChargingStation(Feature):
    lotOperator = models.CharField(max_length=250)
    address = models.CharField(max_length=250, unique=True)
    #keywords = models.CharField(max_length=250)

class CommunityFoodMarket(Feature):
    year = models.CharField(max_length=10)  # saves year, month and day
    marketType = models.CharField(max_length=250)
    operator = models.CharField(max_length=250)
    streetNumber = models.CharField(max_length=250)
    streetName = models.CharField(max_length=250)
    url = models.URLField()
    day = models.CharField(max_length=10)
    openHours = models.CharField(max_length=10)
    closeHours = models.CharField(max_length=10)
    monthsOfOperations = models.CharField(max_length=250)
    numberOfVendors = models.CharField(max_length=250)
    offerings = models.CharField(max_length=250)
    completeAddress = models.CharField(max_length=250, unique=True)
    #keywords = models.CharField(max_length=250)


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
  #  completeAddress = models.CharField(max_length=250, unique=True)
    #keywords = models.CharField(max_length=250)
  
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True,null=True)

    def __unicode__(self):
        return self.user.username

# UrlTitle, UrlLink, PubDate
class DatasetLink(models.Model):
    url_title = models.CharField(max_length=200)
    #pk = url_link
    url_link = models.URLField(max_length=200, unique=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.url_link
