from django.urls import path
from .views import (
    contacts_view, about_view, main_view,weather_view,
)

app_name='main'

urlpatterns = [
    path('contacts/', contacts_view,name='contacts'),
    path('about/', about_view,name='about'),
    path('', main_view,name='index'),
    path('weather/', weather_view, name='weather'),



]

#img = urllib.request.urlopen(f"http://openweathermap.org/img/w/{icon}.png")