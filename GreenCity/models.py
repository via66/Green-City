from django.db import models


class Feature(models.Model):
    name = models.CharField(max_length=100)
    lat = models.FloatField()
    lon = models.FloatField()


# Green Project Model: MAPID,NAME,CATEGORY1,CATEGORY2,ADDRESS,SHORT_DESCRIPTION,URL,URL2,URL3,LATITUDE,LONGITUDE
class GreenProject(Feature):
    map_id = models.CharField(max_length=6)
    cat_1 = models.CharField(max_length=50)
    cat_2 = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    url_1 = models.URLField()
    url_2 = models.URLField()
    url_3 = models.URLField()


class Park(Feature):
    url = models.URLField()


class FoodMarkets(Feature):
    # Year,MarketType,MarketName/Location/Host,Market Operator\
    #  ,StreetNumber,StreetDirection,StreetName,StreetType,MergedAddress,MarketDirection,\
    # Website,Day,Open,Close,Months,NumberOfVendors,Offerings
    year = models.IntegerField()
    market_type = models.CharField(max_length=100)
    operator = models.CharField(max_length=50)
    street_num = models.CharField(max_length=10)
    street_dir = models.CharField(max_length=10)
    street_name = models.CharField(max_length=10)
    street_type = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    market_dir = models.CharField(max_length=10)
    website = models.URLField()
    day = models.CharField(max_length=10)
    open = models.CharField(max_length=5)
    close = models.CharField(max_length=5)
    months = models.CharField(max_length=20)
    num_vendors = models.IntegerField()
    offerings = models.CharField(max_length=100)
