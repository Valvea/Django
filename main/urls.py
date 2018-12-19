from django.urls import path
from .views import (
    contacts_view, about_view, main_view
)

app_name='main'

urlpatterns = [
    path('contacts/', contacts_view,name='contacts'),
    path('about/', about_view,name='about'),
    path('', main_view,name='index'),
]