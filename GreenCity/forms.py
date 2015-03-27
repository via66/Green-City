from django import forms
from GreenCity.models import GreenCityUserProfile, NewUser

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = NewUser
        fields = ('username', 'email', 'password','first_name','last_name')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = GreenCityUserProfile
        fields = ('website',)