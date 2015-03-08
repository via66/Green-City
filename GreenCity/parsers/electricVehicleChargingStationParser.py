
def parseElectricVehicleChargingStation(url):
	import csv
	import urllib2
	import time
	from datetime import datetime
	from GreenCity.models import ElectricVehicleChargingStation
	f = urllib2.urlopen(url)
	reader = csv.reader(f)
	reader.next()
	for row in reader:
		newChargingStation = ElectricVehicleChargingStation(
			name = unicode(row[3],"ISO-8859-1"),
			longitude = unicode(row[1],"ISO-8859-1"),
			latitude = unicode(row[0],"ISO-8859-1"),
			lotOperator = unicode(row[2],"ISO-8859-1"),
			address = unicode(row[3],"ISO-8859-1")
		)
		try:
			newChargingStation.save()
		except:
			print "Could not save your data, check if you entered a valid list of charging stations."

# run from "manage.py shell"
# execfile('path to the file')
#

if __name__ == "__main__":
	
	import os
	import django
	import csv
	import urllib2
	import time
	from datetime import datetime

	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoUnchained.settings")
	django.setup()
	
	from django.conf import settings

	parseElectricVehicleChargingStation('ftp://webftp.vancouver.ca/OpenData/csv/electric_vehicle_charging_stations.csv')

