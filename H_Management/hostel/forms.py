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

"""
class UserReg(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
        ]


class PersonReg(forms.ModelForm):

    class Meta:
        model = Person
        fields = [
            'person_phone',
            'person_gender',
            'person_is_warden',
            'person_prn',
            'person_room_number',
        ]
"""