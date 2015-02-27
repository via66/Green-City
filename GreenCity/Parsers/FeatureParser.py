import csv
import urllib2
import codecs
from GreenCity.models import GreenProject, Park, FoodMarkets


def get_data(url):
    ftpstream = urllib2.urlopen(url)
    features = csv.DictReader(ftpstream)
    return features


def parse_park_data(url):
    data = get_data(url)
    for obj in data:
        print obj
        lati, longi = map(lambda x: float(x), obj['GoogleMapDest'].strip('"').split(','))
        # print lati
        # print longi
        # required for insertion
        # o, created = Park.objects.get_or_create(name=obj['Name'], lat=lati, lon=lngi, url=obj['NeighbourhoodURL'])



if __name__== '__main__':
    parse_park_data('ftp://webftp.vancouver.ca/OpenData/csv/parks.csv')