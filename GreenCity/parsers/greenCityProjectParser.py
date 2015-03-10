import csv
import urllib2
from GreenCity.models import GreenCityProject


def parseGreenCityProject(url):
    f = urllib2.urlopen(url)
    reader = csv.reader(f)
    reader.next()

    for row in reader:
        GreenCityProject.objects.update_or_create(
            name=unicode(row[1], "ISO-8859-1"),
            longitude=unicode(row[10], "ISO-8859-1"),
            latitude=unicode(row[9], "ISO-8859-1"),
            category1=unicode(row[2], "ISO-8859-1"),
            category2=unicode(row[3], "ISO-8859-1"),
            address=unicode(row[4], "ISO-8859-1"),
            shortDescription=unicode(row[5], "ISO-8859-1"),
            url1=unicode(row[6], "ISO-8859-1"),
            url2=unicode(row[7], "ISO-8859-1"),
            url3=unicode(row[8], "ISO-8859-1"),
        )




# run from "manage.py shell"
# execfile('path to the file')
#

if __name__ == "__main__" or __name__ == '__builtin__':
    import os
    import django

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoUnchained.settings")
    django.setup()
    parseGreenCityProject('ftp://webftp.vancouver.ca/OpenData/csv/greenest_city_projects.csv')

