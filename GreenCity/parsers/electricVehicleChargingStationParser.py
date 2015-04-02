import csv
import urllib2
from GreenCity.models import ElectricVehicleChargingStation


def parseElectricVehicleChargingStation(url):
    f = urllib2.urlopen(url)
    reader = csv.reader(f)
    reader.next()
    count = 1
    for row in reader:
        newChargingStation = ElectricVehicleChargingStation(
            name=unicode(row[3] + ',' + str(count), "ISO-8859-1"),
            longitude=unicode(row[1], "ISO-8859-1"),
            latitude=unicode(row[0], "ISO-8859-1"),
            lotOperator=unicode(row[2], "ISO-8859-1"),
            address=unicode(row[3], "ISO-8859-1"),
        )
        try:
            newChargingStation.save()
            count = count + 1
        except:
            print "Could not save your data, check if you entered a valid list of charging stations."

# run from "manage.py shell"
# execfile('path to the file')
#

if __name__ == "__main__" or __name__ == '__builtin__':
    import os
    import django

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoUnchained.settings")
    django.setup()

    parseElectricVehicleChargingStation('ftp://webftp.vancouver.ca/OpenData/csv/electric_vehicle_charging_stations.csv')

