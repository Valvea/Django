from django.urls import path
from .views import (
    list_view,detail_view)

urlpatterns= [
    path('<int:pk>/',detail_view),
    path('',list_view),
]