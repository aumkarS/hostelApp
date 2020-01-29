from django.contrib.auth.models import User
from .models import Person
from phonenumber_field.modelfields import PhoneNumberField
from django import forms


class UserLogin(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password']


class RegForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100, widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    # retype_password = forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField(max_length=100)
    gender = forms.ChoiceField( choices=Person.GENDER)
    prn = forms.CharField(max_length=20)
    room_number = forms.IntegerField(max_value=10)
