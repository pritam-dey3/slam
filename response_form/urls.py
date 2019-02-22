#response_form/urls.py

from django.urls import path
from . import views

urlpatterns = [
        path('', views.ResponseFormView, name='resForm'),
]
