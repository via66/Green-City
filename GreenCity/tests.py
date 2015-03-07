from django.test import TestCase
from GreenCity.models import Feature, Park, GreenCityProject, ElectricVehicleChargingStation, BikeRack, CommunityFoodMarket, CommunityGarden

class ParkTestCase(TestCase):
	def setUp(self):
		super(ParkTestCase, self).setUp()
		self.newPark = Park.objects.create(name="ParkName", longitude=12.1234531, latitude=12.1234531, streetNumber="123", streetName="Streen Name Blablabla", hectare=33.2, neighbourhoodName="Neighbourhood Name", neighbourhoodURL="", washrooms=True)

	def test_can_save_valid_park(self):
		"""Test to see if the models is being saved when it has all right fields."""
		self.newPark.save()

def generateName(streetNumber,streetName):
		return streetNumber + " " + streetName

def getGeoLocation(completeAddress,longitude_and_latitude):
	geolocator = Nominatim()
	completeAddress = completeAddress+" "+"Vancouver"
	location = geolocator.geocode(completeAddress)
	
	if longitude_and_latitude == "latitude":
		return location.latitude
	elif longitude_and_latitude == "longitude":
		return location.longitude

from geopy.geocoders import Nominatim
from decimal import *

class BikeRackTestCase(TestCase):
	def setUp(self):
		super(BikeRackTestCase, self).setUp()
		streetName = "Student Union Boulevard"
		streetNumber = "1234"
		completeAddress = generateName(streetNumber,streetName)
		self.newBikeRack = BikeRack.objects.create(name = completeAddress, longitude = getGeoLocation(completeAddress,"longitude"),latitude = getGeoLocation(completeAddress,"latitude"),streetNumber = streetNumber,streetName = streetName,numberOfRacks = 4)

	def test_can_save_valid_bikeRack(self):
		"""Test to see if the models is being saved when it has all right fields."""
		self.newBikeRack.save()

