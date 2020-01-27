from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from enum import Enum


class Person(models.Model):
    """class Gender(Enum):
        Male = 'M'
        Female = 'F'
        Other = 'O'"""
    GENDER = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other'),
    )

    person_is_staff = models.BooleanField(default=False)
    person_first_name = models.CharField(max_length=50)
    person_last_name = models.CharField(max_length=50)
    person_email = models.CharField(max_length=150)
    person_phone = PhoneNumberField(null=False, blank=False, unique=True)
    person_is_chief = models.BooleanField(default=False)
    person_gender = models.CharField(
        max_length=2,
        choices=GENDER,
    )

    def __str__(self):
        if self.person_gender == 'M':
            gen = "Mr."
        elif self.person_gender == 'F':
            gen = "Miss "
        else:
            gen = ' '

        return gen + self.person_first_name + ' ' + self.person_last_name


class Complaint(models.Model):
    TYPE = (
        ('room', 'Room'),
        ('wifi', 'WiFi'),
        ('water', 'Water'),
        ('other', 'Other'),
    )

    class Status(Enum):
        Registered = 'reg'
        In_Process = 'in_process'
        Solved = 'solved'

    STATUS = (
        ('reg', 'Registered'),
        ('ip', 'In process'),
        ('s', 'Solved'),
    )

    complaint = models.CharField(max_length=200)
    reg_by = models.ForeignKey(Person, on_delete=models.CASCADE)
    complaint_type = models.CharField(
        max_length=10,
        choices=TYPE,
    )
    complaint_status = models.CharField(
        max_length=10,
        choices=STATUS,
    )

    def __str__(self):
        return 'Complaint number' + str(self.id) + ' by ' + self.reg_by.person_last_name
