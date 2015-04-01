from django import forms
from GreenCity.models import NewUser
import json

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
 #   favorites = forms.CharField( required=False, max_length=250)

    class Meta:
        model = NewUser
        fields = ('username', 'email', 'password','first_name','last_name')
