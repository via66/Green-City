import csv
import urllib2
from GreenCity.models import CommunityGarden


def parseCommunityGardens(url):
    f = urllib2.urlopen(url)
    reader = csv.reader(f)
    reader.next()
    for row in reader:
        newStreetNumber = unicode(row[2], "ISO-8859-1")
        newStreetName = unicode(row[4], "ISO-8859-1")

        newNumberOfPlots = unicode(row[9], "ISO-8859-1")

        if is_number(unicode(row[9], "ISO-8859-1")):
            newNumberOfPlots = int(unicode(row[9], "ISO-8859-1"))
        else:
            if newNumberOfPlots == 'Y':
                newNumberOfPlots = 1
            else:
                newNumberOfPlots = 0

        newNumberOfFoodTrees = unicode(row[10], "ISO-8859-1")
        if is_number(unicode(row[10], "ISO-8859-1")):
            newNumberOfFoodTrees = int(unicode(row[10], "ISO-8859-1"))
        else:
            if newNumberOfFoodTrees == 'Y':
                newNumberOfFoodTrees = 1
            else:
                newNumberOfFoodTrees = 0

        new_lat = unicode(row[8], "ISO-8859-1")
        new_long = unicode(row[7], "ISO-8859-1")
        newFoodTreeVarieties = unicode(row[12], "ISO-8859-1")
        newJurisdiction = unicode(row[14], "ISO-8859-1")
        newStewarsOrManagingOrganization = unicode(row[15], "ISO-8859-1")
        newPublicEmail = unicode(row[16], "ISO-8859-1")
        newUrl = unicode(row[17], "ISO-8859-1")
        new_name = unicode(row[1], "ISO-8859-1")
        # if is_number(new_lat) and is_number(new_long):
        try:
            CommunityGarden.objects.update_or_create(
                name=new_name,
                longitude=new_long,
                latitude=new_lat,
                streetNumber=newStreetNumber,
                streetName=newStreetName,
                numberOfPlots=newNumberOfPlots,
                numberOfFoodTrees=newNumberOfFoodTrees,
                foodTreeVarieties=newFoodTreeVarieties,
                jurisdiction=newJurisdiction,
                stewarsOrManagingOrganization=newStewarsOrManagingOrganization,
                publicEmail=newPublicEmail,
                url=newUrl
            )
        except:
            "could not add record"


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

# run from "manage.py shell"
# execfile('path to the file')
#

if __name__ == "__main__" or __name__ == '__builtin__':
    import os
    import django

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoUnchained.settings")
    django.setup()

    parseCommunityGardens('ftp://webftp.vancouver.ca/OpenData/csv/CommunityGardensandFoodTrees.csv')

