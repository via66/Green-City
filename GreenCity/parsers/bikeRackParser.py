import csv
import urllib2
from GreenCity.models import BikeRack
from geopy.geocoders import Nominatim
from django.db import transaction

def parseBikeRack(url):
    f = urllib2.urlopen(url)
    reader = csv.reader(f)
    reader.next()
    setup_address_mapping()
    parse_bike_rack_file(reader)
    # get_lat_lon_from_address()
    f.close()


@transaction.atomic()
def parse_bike_rack_file(reader):
    geolocator = Nominatim()
    address_to_pos = setup_address_mapping()
    for row in reader:
        completeAddress = generateName(unicode(row[0], "ISO-8859-1"), unicode(row[1], "ISO-8859-1"))
        newName = completeAddress
        if address_to_pos.get(completeAddress, None) is not None:
            newLatitude = address_to_pos[completeAddress]['latitude']
            newLongitude = address_to_pos[completeAddress]['longitude']
        else:
            #we only call the api if we have never seen this bike rack before
            newLatitude, newLongitude = getGeoLocation(geolocator, completeAddress)
        newStreetSide = unicode(row[2], "ISO-8859-1")
        newStreetNumber = unicode(row[0], "ISO-8859-1")
        newStreetName = unicode(row[1], "ISO-8859-1")
        newNumberOfRacks = int(unicode(row[5], "ISO-8859-1"))
        try:
            BikeRack.objects.get_or_create(
                name=newName,
                longitude=newLongitude,
                latitude=newLatitude,
                streetSide=newStreetSide,
                streetNumber=newStreetNumber,
                streetName=newStreetName,
                numberOfRacks=newNumberOfRacks,
                completeAddress=completeAddress
            )
        except:
            print "could not add duplicate;"


@transaction.atomic()
def get_lat_lon_from_address():
    geolocator = Nominatim()
    for bikeRack in BikeRack.objects.all():
        bikeRack.latitude, bikeRack.longitude = getGeoLocation(geolocator, bikeRack.completeAddress)
        bikeRack.save()


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
        address_mapping[address.strip('"')] = { 'latitude': float(latitude),
                                                'longitude': float(longitude)}
    return address_mapping

# run from "manage.py shell"
# execfile('path to the file')
#

if __name__ == "__main__" or __name__ == '__builtin__':
    import os
    import django

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoUnchained.settings")
    django.setup()

    parseBikeRack('ftp://webftp.vancouver.ca/opendata/bike_rack/BikeRackData.csv')

