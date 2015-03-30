from django import forms
from GreenCity.models import NewUser

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = NewUser
        fields = ('username', 'email', 'password','first_name','last_name')
