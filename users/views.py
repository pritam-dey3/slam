#users/view.py

from django.shortcuts import render

from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

from .forms import CustomUserCreation

class SignUp(generic.CreateView):
    form_class = CustomUserCreation
    success_url = reverse_lazy('home')
    template_name = 'signup.html'

class HomePage(TemplateView):
    template_name = 'home.html'
    def dispatch(self, request, *args, **kwargs):
        print (self.request.user)
        return super(HomePage, self).dispatch(request, *args, **kwargs)
