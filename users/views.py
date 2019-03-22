# users/view.py

from django.shortcuts import render

from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from django.forms.models import model_to_dict
from slam.questions_and_answers import intro1

from .forms import CustomUserCreation


class SignUp(generic.CreateView):
    form_class = CustomUserCreation
    success_url = reverse_lazy('home')
    template_name = 'signup.html'


class HomePage(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['intro'] = intro1
        return context

    def dispatch(self, request, *args, **kwargs):
        # print(model_to_dict(self.request.user))
        return super(HomePage, self).dispatch(request, *args, **kwargs)
