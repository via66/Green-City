import csv
import urllib2
from GreenCity.models import CommunityFoodMarket
from geopy.geocoders import Nominatim
from django.db import transaction


def parseCommunityFoodMarket(url):
    f = urllib2.urlopen(url)
    reader = csv.reader(f)
    reader.next()
    parse_market_file(reader)
    f.close()


@transaction.atomic
def parse_market_file(reader):
    geolocator = Nominatim()
    for row in reader:
        if (unicode(row[0], "ISO-8859-1")):
            complete_address = unicode(row[8], "ISO-8859-1")
            new_lat, new_long = getGeoLocation(geolocator, complete_address)
            try:
                CommunityFoodMarket.objects.update_or_create(
                    name=unicode(row[2], "ISO-8859-1"),
                    longitude=new_long,
                    latitude=new_lat,
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
                    #keywords include name, market type, streetname, offerings
                    #keywords=unicode(row[2], "ISO-8859-1" + ", " + row[1], "ISO-8859-1" + ", " + row[6], "ISO-8859-1" + ", " + row[16], "ISO-8859-1"),
                    completeAddress=complete_address
                )
            except:
                "could not add this item"



def generateName(streetNumber, streetName):
    return streetNumber + " " + streetName


def getGeoLocation(geolocator, completeAddress):
    location = geolocator.geocode(completeAddress+" "+"Vancouver", timeout=500)
    if location is not None:
        return float(unicode(location.latitude)), float(unicode(location.longitude))
    else:
        return 0.0, 0.0


# run from "manage.py shell"
# execfile('path to the file')
#

if __name__ == "__main__" or __name__ == '__builtin__':
    import os
    import django

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoUnchained.settings")
    django.setup()

    parseCommunityFoodMarket('ftp://webftp.vancouver.ca/OpenData/csv/CommunityFoodMarketsandFarmersMarkets.csv')

