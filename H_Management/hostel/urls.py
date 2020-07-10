from django.urls import path
from . import views


app_name = 'hostel'


urlpatterns = [
    path('welcome/', views.welcome, name='welcome'),
    path('login', views.Login.as_view(), name='login'),
    path('register', views.reg, name='reg'),
    path('dash', views.dash,name='dash')
]