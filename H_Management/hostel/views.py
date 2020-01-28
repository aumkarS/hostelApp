from .models import Person, Complaint
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import View
from django.views import generic


def welcome(request):
    return render(request, 'hostel/welcome.html', None)
