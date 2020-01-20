from django.contrib import admin
from django.urls import path
from .views import details

urlpatterns = [
    path('details/<slug:slug>', details, name='details')
]
