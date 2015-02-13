from django.db import models


# TODO: Green Project Model: MAPID,NAME,CATEGORY1,CATEGORY2,ADDRESS,SHORT_DESCRIPTION,URL,URL2,URL3,LATITUDE,LONGITUDE
class GreenProject(models.Model):
    map_id = models.CharField(max_length=6)
    name = models.CharField(max_length=100)
    cat_1 = models.CharField(max_length=50)
    cat_2 = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    url_1 = models.URLField()
    url_2 = models.URLField()
    url_3 = models.URLField()
    lat = models.FloatField()
    lon = models.FloatField()
