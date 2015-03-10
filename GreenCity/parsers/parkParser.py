import csv
import urllib2
from GreenCity.models import Park


def parsePark(url):
    f = urllib2.urlopen(url)
    reader = csv.reader(f)
    reader.next()
    for row in reader:
        newPark = Park(
            name=unicode(row[1], "ISO-8859-1"),
            streetNumber=unicode(row[3], "ISO-8859-1"),
            streetName=unicode(row[4], "ISO-8859-1"),
            longitude=googleMapDest(unicode(row[7], "ISO-8859-1"), "longitude"),
            latitude=googleMapDest(unicode(row[7], "ISO-8859-1"), "latitude"),
            hectare=float(row[8]),
            neighbourhoodName=unicode(row[9], "ISO-8859-1"),
            neighbourhoodURL=unicode(row[10], "ISO-8859-1"),
            washrooms=stringToBoolean(unicode(row[14], "ISO-8859-1")),
            completeAddress=unicode(row[3], "ISO-8859-1") + " " + unicode(row[4], "ISO-8859-1")
        )
        try:
            newPark.save()
        except:
            print "Could not save your data, check if you entered a valid list of parks."


def googleMapDest(longitude_and_latitude, coordinate_type):
    separate_coordinates = longitude_and_latitude.split(",")
    if coordinate_type == "latitude":
        return separate_coordinates[0]
    elif coordinate_type == "longitude":
        return separate_coordinates[1]


def stringToBoolean(string):
    if "Y" in string:
        return True
    elif "N" in string:
        return False


# run from "manage.py shell"
# execfile('path to the file')
#

if __name__ == "__main__" or __name__ == '__builtin__':
    import os
    import django

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoUnchained.settings")
    django.setup()

    parsePark('ftp://webftp.vancouver.ca/OpenData/csv/parks.csv')

