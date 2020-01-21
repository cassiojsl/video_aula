from django.contrib import admin
from django.urls import path
from .views import details, enrollment

urlpatterns = [
    path('details/<slug:slug>', details, name='details'),
    path('inscricao/<slug:slug>', enrollment, name='enrollment'),
]
