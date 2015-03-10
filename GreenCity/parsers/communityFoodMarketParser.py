import csv
import urllib2
from GreenCity.models import CommunityFoodMarket
from django.core.exceptions import ValidationError
from decimal import Decimal
from geopy.geocoders import Nominatim


def parseCommunityFoodMarket(url):
    f = urllib2.urlopen(url)
    reader = csv.reader(f)
    reader.next()

    newFoodMarketList = []
    for row in reader:
        if (unicode(row[0], "ISO-8859-1")):
            newFoodMarket = CommunityFoodMarket(
                name=unicode(row[2], "ISO-8859-1"),
                longitude=0.0,
                latitude=0.0,
                year=unicode(row[0], "ISO-8859-1"),
                marketType=unicode(row[1], "ISO-8859-1"),
                operator=unicode(row[3], "ISO-8859-1"),
                streetNumber=unicode(row[4], "ISO-8859-1"),
                streetName=unicode(row[6], "ISO-8859-1"),
                url=unicode(row[10], "ISO-8859-1"),
                day=unicode(row[11], "ISO-8859-1"),
                openHours=unicode(row[12], "ISO-8859-1"),
                closeHours=unicode(row[13], "ISO-8859-1"),
                monthsOfOperations=unicode(row[14], "ISO-8859-1"),
                numberOfVendors=unicode(row[15], "ISO-8859-1"),
                offerings=unicode(row[16], "ISO-8859-1"),
                completeAddress=unicode(row[8], "ISO-8859-1")
            )
            try:
                newFoodMarket.save()
                newFoodMarketList.append(newFoodMarket.id)
            except ValidationError as e:
                print "Could not save your data, check if you entered a valid list of community food markets."
    f.close()
    print "Starting to get the geolocation of community food markets."
    print newFoodMarketList
    for foodMarketID in newFoodMarketList:
        foodMarket = CommunityFoodMarket.objects.get(pk=foodMarketID)
        print "Food Market " + str(foodMarket.name) + "."
        try:
            foodMarket.longitude = getGeoLocation(foodMarket.completeAddress, "longitude")
            foodMarket.latitude = getGeoLocation(foodMarket.completeAddress, "latitude")
            foodMarket.save()
        except:
            print foodMarket.completeAddress  # If the address present any error, we cannot get the lat/long!
            pass


def generateName(streetNumber, streetName):
    return streetNumber + " " + streetName


def getGeoLocation(completeAddress, longitude_and_latitude):
    geolocator = Nominatim()
    completeAddress = completeAddress + " " + "Vancouver"
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

if __name__ == "__main__" or __name__ == '__builtin__':
    import os
    import django

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoUnchained.settings")
    django.setup()

    from django.conf import settings

    parseCommunityFoodMarket('ftp://webftp.vancouver.ca/OpenData/csv/CommunityFoodMarketsandFarmersMarkets.csv')

