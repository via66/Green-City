
def parseCommunityGardens(url):
	import csv
	import urllib2
	import time
	from datetime import datetime
	from GreenCity.models import CommunityGarden
	import unicodedata
	f = urllib2.urlopen(url)
	reader = csv.reader(f)
	reader.next()
	for row in reader:
		newName = unicode(row[1],"ISO-8859-1")
		newLongitude = unicode(row[7],"ISO-8859-1")
		newLatitude = unicode(row[8],"ISO-8859-1")
		newStreetNumber = unicode(row[2],"ISO-8859-1")
		newStreetName = unicode(row[4],"ISO-8859-1")
		
		newNumberOfPlots = unicode(row[9],"ISO-8859-1")

		if is_number(unicode(row[9],"ISO-8859-1")):
			newNumberOfPlots = int(unicode(row[9],"ISO-8859-1"))
		else:
			if newNumberOfPlots == 'Y':
				newNumberOfPlots = 1
			else:
				newNumberOfPlots = 0
		
		newNumberOfFoodTrees = unicode(row[10],"ISO-8859-1")
		if is_number(unicode(row[10],"ISO-8859-1")):
			newNumberOfFoodTrees = int(unicode(row[10],"ISO-8859-1"))
		else:
			if newNumberOfFoodTrees == 'Y':
				newNumberOfFoodTrees = 1
			else:
				newNumberOfFoodTrees = 0

		newFoodTreeVarieties = unicode(row[12],"ISO-8859-1")
		newJurisdiction = unicode(row[14],"ISO-8859-1")
		newStewarsOrManagingOrganization = unicode(row[15],"ISO-8859-1")
		newPublicEmail = unicode(row[16],"ISO-8859-1")
		newUrl = unicode(row[17],"ISO-8859-1")

		if newStreetNumber:
			newCommunityGarden = CommunityGarden(
				name = newName,
				longitude = newLongitude,
				latitude = newLatitude,
				streetNumber = newStreetNumber,
				streetName = newStreetName,
				numberOfPlots = newNumberOfPlots,
				numberOfFoodTrees = newNumberOfFoodTrees,
				foodTreeVarieties = newFoodTreeVarieties,
				jurisdiction = newJurisdiction,
				stewarsOrManagingOrganization = newStewarsOrManagingOrganization,
				publicEmail = newPublicEmail,
				url = newUrl,
			)
			
			try:
				newCommunityGarden.save()
			except:
				print "Could not save your data, check if you entered a valid list of community gardens."

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

if __name__ == "__main__":
	
	import os
	import django
	import csv
	import urllib2
	import time
	

	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoUnchained.settings")
	django.setup()
	
	from django.conf import settings

	parseCommunityGardens('ftp://webftp.vancouver.ca/OpenData/csv/CommunityGardensandFoodTrees.csv')

