from django.urls import path
from . import views


app_name = 'hostel'


urlpatterns = [
    path('welcome', views.welcome, name='welcome'),
    path('login', views.Login.as_view(), name='login'),
    path('register', views.update_profile, name='reg'),
]