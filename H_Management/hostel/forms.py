from django.contrib.auth.models import User
from .models import Person
from django import forms


class UserLogin(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password']


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
