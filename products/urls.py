from django.urls import path
from .views import (
    list_view,detail_view)

app_name='products'

urlpatterns= [
    path('<int:pk>/',detail_view,name="detail"),
    path('',list_view,name='index'),
]