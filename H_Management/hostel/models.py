from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from enum import Enum


class Person(models.Model):

    GENDER = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    person_is_warden = models.BooleanField(default=False)
    person_phone = PhoneNumberField(null=False, blank=False, unique=True)
    person_prn = models.CharField(max_length=150, unique=True, null=False, default='0')
    person_room_number = models.CharField(max_length=15, null=False, default='0')
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

        return gen + self.user.get_full_name()


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
        return 'Complaint number' + str(self.id) + ' by ' + self.reg_by.user.last_name


class MessMenu(models.Model):
    DAY = (
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
    )

    day_day = models.CharField(
        max_length=10,
        choices=DAY,
        unique=True
    )

    soup = models.CharField(max_length=50)
    main_course = models.CharField(max_length=100)
    dessert = models.CharField(max_length=50)

    def __str__(self):
        return self.get_day_day_display()
