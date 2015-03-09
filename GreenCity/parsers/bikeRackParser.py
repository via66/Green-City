
def parseBikeRack(url):
	from django.conf import settings
	import csv
	import urllib2
	import time
	from datetime import datetime
	from GreenCity.models import BikeRack
	from django.core.exceptions import ValidationError
	from geopy.geocoders import Nominatim
	# from decimal import *

	f = urllib2.urlopen(url)
	reader = csv.reader(f)
	reader.next()

	newBikeRackList = []
	for row in reader:
		completeAddress = generateName(unicode(row[0],"ISO-8859-1"),unicode(row[1],"ISO-8859-1"))
		newName = completeAddress
		newLongitude = 0.0 #getGeoLocation(completeAddress,"longitude")
		newLatitude = 0.0 #getGeoLocation(completeAddress,"latitude")
		newStreetSide = unicode(row[2],"ISO-8859-1")
		newStreetNumber = unicode(row[0],"ISO-8859-1")
		newStreetName = unicode(row[1],"ISO-8859-1")
		newNumberOfRacks = int(unicode(row[5],"ISO-8859-1"))

		newBikeRack = BikeRack(
			name = newName,
			longitude = newLongitude,
			latitude = newLatitude,
			streetSide = newStreetSide,
			streetNumber = newStreetNumber,
			streetName = newStreetName,
			numberOfRacks = newNumberOfRacks
		)
		
		try:
			newBikeRack.save()
			newBikeRackList.append(newBikeRack.id)
		except:
			print "Could not save your data, check if you entered a valid list of bike racks."
			pass
	f.close()
	print "Starting to get the geolocation of bike racks."
	for bikeRackID in newBikeRackList:
		bikeRack = BikeRack.objects.get(id=bikeRackID)
		print "Bike rack "+str(bikeRackID)+"."
		bikeRack.longitude = getGeoLocation(bikeRack.completeAddress,"longitude")
		bikeRack.latitude = getGeoLocation(bikeRack.completeAddress,"latitude")
		bikeRack.save()

def generateName(streetNumber,streetName):
	return streetNumber + " " + streetName

def getGeoLocation(completeAddress,longitude_and_latitude):
	geolocator = Nominatim()
	completeAddress = completeAddress+" "+"Vancouver"
	location = geolocator.geocode(completeAddress, timeout=500)

	if longitude_and_latitude == "latitude":
		# print Decimal(unicode(location.latitude))
		return Decimal(unicode(location.latitude))
	elif longitude_and_latitude == "longitude":
		# print Decimal(unicode(location.longitude))
		return Decimal(unicode(location.longitude))

# run from "manage.py shell"
# execfile('path to the file')
#

if __name__ == "__main__":
	
	import os
	import django

	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoUnchained.settings")
	django.setup()
	
	from django.conf import settings
	import csv
	import urllib2
	import time
	from datetime import datetime
	from GreenCity.models import BikeRack

	from geopy.geocoders import Nominatim
	from decimal import *

	parseBikeRack('ftp://webftp.vancouver.ca/opendata/bike_rack/BikeRackData.csv')

