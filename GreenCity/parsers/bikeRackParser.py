import csv
import urllib2
from GreenCity.models import BikeRack
from geopy.geocoders import Nominatim
from decimal import *


def parseBikeRack(url):
	f = urllib2.urlopen(url)
	reader = csv.reader(f)
	reader.next()
	print "Parsing data from csv file."
	bikeRackList = parse_bike_rack_file(reader)
	f.close()
	print "Getting location coordinates from address."
	get_lat_lon_from_address(bikeRackList)

def parse_bike_rack_file(reader):
	newBikeRackList = []
	for row in reader:
		completeAddress = generateName(unicode(row[0], "ISO-8859-1"), unicode(row[1], "ISO-8859-1"))
		newName = completeAddress
		newLongitude = 0.0  # getGeoLocation(completeAddress,"longitude")
		newLatitude = 0.0  # getGeoLocation(completeAddress,"latitude")
		newStreetSide = unicode(row[2], "ISO-8859-1")
		newStreetNumber = unicode(row[0], "ISO-8859-1")
		newStreetName = unicode(row[1], "ISO-8859-1")
		newNumberOfRacks = int(unicode(row[5], "ISO-8859-1"))
		
		newBikeRack = BikeRack(
			name=newName,
			longitude=newLongitude,
			latitude=newLatitude,
			streetSide=newStreetSide,
			streetNumber=newStreetNumber,
			streetName=newStreetName,
			numberOfRacks=newNumberOfRacks
		)
		try:
			newBikeRack.save()
			newBikeRackList.append(newBikeRack)
		except:
			print "Could not save your data, check if you entered a valid list of bike racks."

	return newBikeRackList


def get_lat_lon_from_address(bikeRackList):
	for bikeRack in bikeRackList:
		bikeRack.latitude, bikeRack.longitude = getGeoLocation(bikeRack.completeAddress)
		bikeRack.save()


def generateName(streetNumber, streetName):
	return streetNumber + " " + streetName


def getGeoLocation(completeAddress):
	geolocator = Nominatim()
	completeAddress = completeAddress + " " + "Vancouver"
	location = geolocator.geocode(completeAddress, timeout=500)
	return Decimal(unicode(location.latitude)), Decimal(unicode(location.longitude))

# run from "manage.py shell"
# execfile('path to the file')
#

if __name__ == "__main__" or __name__ == '__builtin__':
	import os
	import django

	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoUnchained.settings")
	django.setup()

	parseBikeRack('ftp://webftp.vancouver.ca/opendata/bike_rack/BikeRackData.csv')

