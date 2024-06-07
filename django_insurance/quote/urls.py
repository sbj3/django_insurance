# quote/urls.py -> app urls 
from django.urls import path 
from . import views

urlpatterns = [
    path("customerpage/", views.create, name="customerpage")
]
