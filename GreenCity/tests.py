from django.test import TestCase
from GreenCity.models import Feature, Park, GreenCityProject, ElectricVehicleChargingStation, BikeRack, CommunityFoodMarket, CommunityGarden, DatasetLink, NewUser
from datetime import datetime, date

class ParkTestCase(TestCase):
    def setUp(self):
        super(ParkTestCase, self).setUp()
        self.newPark = Park.objects.create(name="ParkName", longitude=12.1234531, latitude=12.1234531, streetNumber="123", streetName="Streen Name Blablabla", hectare=33.2,neighbourhoodName="Neighbourhood Name", neighbourhoodURL="", washrooms=True)

    def test_can_save_valid_park(self):
        """Test to see if the models is being saved when it has all right fields."""
        self.newPark.save()

def generateName(streetNumber, streetName):
    return streetNumber + " " + streetName

def getGeoLocation(geolocator, completeAddress):
    location = geolocator.geocode(completeAddress+" "+"Vancouver", timeout=500)
    if location is not None:
        return float(unicode(location.latitude)), float(unicode(location.longitude))
    else:
        return 0.0, 0.0

def setup_address_mapping():
    address_mapping = {}
    f = open("GreenCity/parsers/address_to_lat_long/address_to_lat_long.csv")
    for line in f:
        _, address, longitude, latitude = line.split(',')
        address_mapping[address.strip('"')] = { 'latitude': float(latitude), 'longitude': float(longitude)}
    return address_mapping

from geopy.geocoders import Nominatim
from decimal import *

class BikeRackTestCase(TestCase):
    def setUp(self):
        super(BikeRackTestCase, self).setUp()
        geolocator = Nominatim()
        address_to_pos = setup_address_mapping()
        
        streetName = "Cambie St"
        streetNumber = "891"
        completeAddress = generateName(streetNumber, streetName)
        newStreetSide = "East"
        newNumberOfRacks = int("2")

        if address_to_pos.get(completeAddress, None) is not None:
            newLatitude = address_to_pos[completeAddress]['latitude']
            newLongitude = address_to_pos[completeAddress]['longitude']
        else:
            #we only call the api if we have never seen this bike rack before
            newLatitude, newLongitude = getGeoLocation(geolocator, completeAddress)

        self.newBikeRack = BikeRack.objects.create(name=completeAddress,longitude=newLongitude,latitude=newLatitude,streetNumber=streetNumber, streetName=streetName, streetSide = newStreetSide,numberOfRacks=newNumberOfRacks)

    def test_can_save_valid_bikeRack(self):
        """ Test to see if the models is being saved when it has all right fields with the the necessary extra functions (to get the latitude and longitude). """
        self.newBikeRack.save()

# Park, GreenCityProject, ElectricVehicleChargingStation, BikeRack, CommunityFoodMarket, CommunityGarden, DatasetLink, NewUser
class GreenCityProjectTestCase(TestCase):
    def setUp(self):
        super(GreenCityProjectTestCase,self).setUp()
        self.newProject = GreenCityProject.objects.create(name="Local Garden Greenhouse", longitude=49.2610221, latitude=-123.0440375, category1="City projects", category2="Green Economy", address="666 Burrard St", shortDescription="Canada's first Living Building - generates all of its own power, and treats all of its own waste water.", url1="http://www.greenbuildingaudiotours.com/buildings/sefc_neighbourhood_energy_utility", url2="http://www.inteluma.com/", url3="http://www.langara.bc.ca/index.html")

    def test_can_save_valid_projet(self):
        """ Test if it is possible to save a valid instance of a project """
        self.newProject.save()

class ElectricVehicleChargingStationTestCase(TestCase):
    def setUp(self):
        super(ElectricVehicleChargingStationTestCase,self).setUp()
        self.newStation = ElectricVehicleChargingStation.objects.create(name="1055 Eveleigh St.",longitude=49.22249551,latitude=-123.1002624,lotOperator="Vancouver Aquarium",address="1055 Eveleigh St.")

    def test_can_save_valid_station(self):
        """ Test if it is possible to save a valid instance of a electric vehicle charging station """
        self.newStation.save()

class CommunityFoodMarketTestCase(TestCase):
    def setUp(self):
        super(CommunityFoodMarketTestCase,self).setUp()
        geolocator = Nominatim()
        complete_address = "3092  Garden Drive, Vancouver BC"
        new_lat, new_long = getGeoLocation(geolocator, complete_address)
        self.newMarket = CommunityFoodMarket.objects.create(name="Main St Station Farmers Market",latitude=new_lat, longitude=new_long,year=2014, marketType="Farmers Market", operator="Greater Vancouver Food Bank (Curbside Fresh)", streetNumber=1100, streetName="Comox", url="", day="Saturday", openHours="10am", closeHours="4pm", monthsOfOperations="May-October", numberOfVendors="15-25", offerings="produce, meat, seafood, cheese, organics, prepared foods", completeAddress="494 W 49th Av, Vancouver BC")

    def test_can_save_valid_market(self):
        """ Test if it is possible to save a valid instance of a market """
        self.newMarket.save()

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata

        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

def return_valid_value(value):
    if is_number(value):
        return int(value)
    else:
        if value == 'Y':
            return 1
        else:
            return 0

class CommunityGardenTestCase(TestCase):
    def setUp(self):
        super(CommunityGardenTestCase,self).setUp()

        newStreetNumber = "857"
        newStreetName = "6th"
        newNumberOfPlots = return_valid_value("45")
        newNumberOfFoodTrees = return_valid_value("33")
        new_lat = 49.2572409
        new_long = -123.1503918
        newFoodTreeVarieties = "Bramley's seedling apple; cannor select; cortland; golden delicious smoothee; jonafree; nova mac; shamrock; flemish beauty; hosui; golden spice (hardy); ure pear (hardy); italian plum; pembina plum (hardy); redglow plum (hardy); compact stella cherry; lapin cherry; schatten morello cherry; van cherry; conference dwarf pear; flemish beauty dwarf pear; highland dwarf pear; red sensation dwarf pear; sierra dwarf pear; persimmon fuju + more, Satsuma Plum, Jonamac Apple, Shamrock Apple, Northern Spy Apple, Meteor cherry"
        newJurisdiction = "Parks"
        newStewarsOrManagingOrganization = "Urban Diggers Society"
        newPublicEmail = ""
        newUrl = ""
        new_name = "Douglas Park"

        self.newGarden = CommunityGarden.objects.create(name=new_name,longitude=new_long,latitude=new_lat,streetNumber=newStreetNumber,streetName=newStreetName,numberOfPlots=newNumberOfPlots,numberOfFoodTrees=newNumberOfFoodTrees,foodTreeVarieties=newFoodTreeVarieties,jurisdiction=newJurisdiction,stewarsOrManagingOrganization=newStewarsOrManagingOrganization,publicEmail=newPublicEmail,url=newUrl)

    def test_can_save_valid_garden(self):
        """ Test if it is possible to save a valid instance of a garden """
        self.newGarden.save()

    def test_can_save_garden_without_int_in_necessary_fields(self):
        """ Test if it is possible to save an instance of garden with food number of trees and number of plots defined as string Y (this happens in some cases of the csv file) """
        self.newGarden.numberOfPlots = return_valid_value("Y")
        self.newGarden.numberOfFoodTrees = return_valid_value("Y")
        self.newGarden.save()

class NewUserTestCase(TestCase):
    def setUp(self):
        super(NewUserTestCase,self).setUp()
        self.newUser = NewUser.objects.create(username="Matthew1990",password="longanddifficultpassword",first_name="Matthew",last_name="Arbutus")

    def test_can_create_user(self):
        """ Test if it is possible to create new users """
        self.newUser.save()

    def test_user_has_profile(self):
        """ Test if the user has a facebook profile associated to his/her account """
        try:
            self.newUser.get_profile()
        except:
            print "User does not have a facebook profile linked to his/her account."

# class DatasetLinkTestCase(TestCase):
#     def setUp(self):
#         super(DatasetLinkTestCase,self).setUp()

#         self.newDataset = DatasetLink.objects.create(url_title="",url_link="")

#     def test_can_save_invalid_url_dataset(self):
#         self.newDataset.url_title = "Parks"
#         self.newDataset.url_link = "http://google.com"
#         self.newDataset.pub_date = date.strptime("2015-10-10","%Y-%M-%D")
#         self.newDataset.save()
