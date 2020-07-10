from .models import Person
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db import IntegrityError, transaction
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import View
from django.views import generic
from .forms import UserLogin, RegForm


def welcome(request):
    return render(request, 'hostel/welcome.html', None)


def dash(request):
    return render(request, 'hostel/dash.html')


class Login(View):
    form_class = UserLogin
    template_name = 'hostel/login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'UserForm': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            # user = form.save(commit=False)
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(email=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('hostel:welcome')

        return render(request, self.template_name, {'form': form})


@transaction.atomic
def reg(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            phone = form.cleaned_data['phone']
            gender = form.cleaned_data['gender']
            prn = form.cleaned_data['prn']

            cu = User.objects.values_list('email')
            for em in cu:
                if email == em:
                    return redirect('hostel:reg')
            cu = User.objects.values_list('username')
            for em in cu:
                if email == em:
                    return redirect('hostel:reg')
            try:
                with transaction.atomic():
                    p = Person()
                    p.person_phone = phone
                    p.gender = gender
                    p.person_prn = prn

                    us = User()
                    us.first_name = first_name
                    us.last_name = last_name
                    us.email = email
                    us.username = email
                    us.set_password(password)
                    p.user = us
                    us.save()
                    p.save()
            except IntegrityError as e:
                return HttpResponse('Duplicate values')
            else:
                return redirect('hostel:dash')
    else:
        form = RegForm()

    return render(request, 'hostel/reg_student.html', {'form': form})


