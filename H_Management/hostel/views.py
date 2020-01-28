from .models import Person, Complaint
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import View
from django.views import generic
from .forms import UserReg, UserLogin, PersonReg


def welcome(request):
    return render(request, 'hostel/welcome.html', None)


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

"""class RegView(View):
    form_class = UserReg
    template_name = 'hostel/reg_student.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        forms = self.form_class(request.POST)
        if forms.is_valid():
            user = forms.save(commit=False)
            email = forms.cleaned_data['person_email']
            password = forms.cleaned_data['password']
            us = User()
            us.username = email
            us.set_password(password)
            us.save()
            user.save()

            user = authenticate(email=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('hostel:dashboard')

        return render(request, self.template_name, {'form': forms})

"""


def update_profile(request):
    if request.method == 'POST':
        user_form = UserReg(request.POST, instance=request.user)
        profile_form = PersonReg(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # messages.success(request, _('Your profile was successfully updated!'))
            return redirect('hostel:welcome')
        # else:
    else:
        user_form = UserReg(instance=request.user)
        profile_form = PersonReg(instance=request.user.profile)
    return render(request, '', {
        'user_form': user_form,
        'profile_form': profile_form
    })
