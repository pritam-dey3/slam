#users/admin.py

import sys
sys.path.insert(0,'..')
import questions_and_answers
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
import pprint

from .forms import CustomUserCreation, CustomUserChange
from .models import CustomUser
from slam.questions_and_answers import fields as f

tpl = ['email', 'count']
for key in f.keys():
    tpl.extend([key + '-Q', key + '-H'])


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreation
    form = CustomUserChange
    list_display = ['email', 'username', 'id']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': tuple(tpl)}),
    )
    model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)
''' fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('q1',)}),
    )'''
