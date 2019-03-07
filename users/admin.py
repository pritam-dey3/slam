#users/admin.py

import sys
sys.path.insert(0,'..')
import questions_and_answers
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
import pprint

from .forms import CustomUserCreation, CustomUserChange
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreation
    form = CustomUserChange
    list_display = ['email', 'username', 'id']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('email', 'q1','q2','count',)}),
    )
    model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)
''' fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('q1',)}),
    )'''
