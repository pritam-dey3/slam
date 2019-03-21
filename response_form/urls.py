#response_form/urls.py

from django.urls import path
from . import views

urlpatterns = [
        path('', views.ResponseFormView, name='resForm'),
        path('allsubmissions/', views.EndView.as_view(), name='end'),
]
