from django.db import models
from model_utils.managers import InheritanceManager
from django.contrib.auth.models import User,AbstractUser

from django.dispatch.dispatcher import receiver
from django_facebook.models import FacebookModel
from django.db.models.signals import post_save
from django_facebook.utils import get_user_model, get_profile_model
from django.conf import settings
import json
# List of models:
# Park, GreenCityProjects, ElectricVehicleChargingStation, BikeRack, CommunityFoodMarket, CommunityGarden


class Feature(models.Model):
    name = models.CharField(max_length=250)
    longitude = models.FloatField()
    latitude = models.FloatField()
    objects = InheritanceManager()

    def __unicode__(self):
        return self.name


class BikeRack(Feature):
    streetNumber = models.CharField(max_length=250)
    streetName = models.CharField(max_length=250)
    streetSide = models.CharField(max_length=250)
    numberOfRacks = models.IntegerField()
    completeAddress = models.CharField(max_length=250)

    class Meta:
        unique_together = ('streetSide', 'streetNumber', 'streetName')


class Park(Feature):
    streetNumber = models.CharField(max_length=250)
    streetName = models.CharField(max_length=250)
    hectare = models.DecimalField(max_digits=6, decimal_places=2)
    neighbourhoodName = models.CharField(max_length=250)
    neighbourhoodURL = models.URLField()
    washrooms = models.BooleanField(default=False)
    completeAddress = models.CharField(max_length=250, unique=True)


class GreenCityProject(Feature):
    category1 = models.CharField(max_length=250)
    category2 = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    shortDescription = models.TextField()
    url1 = models.URLField()
    url2 = models.URLField()
    url3 = models.URLField()

class ElectricVehicleChargingStation(Feature):
    lotOperator = models.CharField(max_length=250)
    address = models.CharField(max_length=250, unique=True)

class CommunityFoodMarket(Feature):
    year = models.CharField(max_length=10)  # saves year, month and day
    marketType = models.CharField(max_length=250)
    operator = models.CharField(max_length=250)
    streetNumber = models.CharField(max_length=250)
    streetName = models.CharField(max_length=250)
    url = models.URLField()
    day = models.CharField(max_length=10)
    openHours = models.CharField(max_length=10)
    closeHours = models.CharField(max_length=10)
    monthsOfOperations = models.CharField(max_length=250)
    numberOfVendors = models.CharField(max_length=250)
    offerings = models.CharField(max_length=250)
    completeAddress = models.CharField(max_length=250, unique=True)


class CommunityGarden(Feature):
    streetNumber = models.CharField(max_length=10, blank=True, null=True)
    streetName = models.CharField(max_length=250, blank=True, null=True)
    numberOfPlots = models.IntegerField(blank=True, null=True)
    numberOfFoodTrees = models.IntegerField(blank=True, null=True)
    foodTreeVarieties = models.CharField(max_length=250, blank=True, null=True)
    jurisdiction = models.CharField(max_length=250, blank=True, null=True)
    stewarsOrManagingOrganization = models.CharField(max_length=250, blank=True, null=True)
    publicEmail = models.EmailField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
  #  completeAddress = models.CharField(max_length=250, unique=True)


# UrlTitle, UrlLink, PubDate
class DatasetLink(models.Model):
    url_title = models.CharField(max_length=200)
    #pk = url_link
    url_link = models.URLField(max_length=200, unique=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.url_link




class FacebookUserProfile(FacebookModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    @receiver(post_save)
    def create_profile(sender, instance, created, **kwargs):
        """Create a matching profile whenever a user object is created."""
        profile_model = None
        if sender == get_user_model():
            user = instance
            profile_model = get_profile_model()
        if profile_model == FacebookUserProfile and created:
            profile, new = FacebookUserProfile.objects.get_or_create(user=instance)

from django.core.exceptions import ImproperlyConfigured
class NewUser(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.

    Username, password and email are required. Other fields are optional.
    """

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    def get_profile(self):
        """
        Returns site-specific profile for this user. Raises
        SiteProfileNotAvailable if this site does not allow profiles.
        """
        

        if not hasattr(self, '_profile_cache'):
            from django.conf import settings
            if not getattr(settings, 'AUTH_PROFILE_MODULE', False):
                raise SiteProfileNotAvailable(
                    'You need to set AUTH_PROFILE_MODULE in your project '
                    'settings')
            try:
                app_label, model_name = settings.AUTH_PROFILE_MODULE.split('.')
            except ValueError:
                raise SiteProfileNotAvailable(
                    'app_label and model_name should be separated by a dot in '
                    'the AUTH_PROFILE_MODULE setting')
            try:
                model = models.get_model(app_label, model_name)
                if model is None:
                    raise SiteProfileNotAvailable(
                        'Unable to load the profile model, check '
                        'AUTH_PROFILE_MODULE in your project settings')
                self._profile_cache = model._default_manager.using(
                                   self._state.db).get(user__id__exact=self.id)
                self._profile_cache.user = self
            except (ImportError, ImproperlyConfigured):
                raise SiteProfileNotAvailable
        return self._profile_cache

class Favorites(models.Model):
    newuser = models.ForeignKey(NewUser, related_name='favs')
    favorites = models.CharField(max_length=250)

    def __str__(self):
        return self.favorites