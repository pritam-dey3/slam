#users/models.py
import sys
sys.path.insert(0,'..')

from django.db import models
from django.contrib.auth.models import AbstractUser
import questions_and_answers

fields_ = questions_and_answers.fields
def apply_defaults(cls):
    for name, value in fields_.items():
        setattr(cls, name, models.CharField(default=value[1]))
    return cls

#@apply_defaults
class CustomUser(AbstractUser):
    q1 = models.CharField(max_length=200, default='0')
    q2 = models.CharField(max_length=200, default='0')
    count = models.IntegerField(default=0)

'''def apply_defaults(cls):
    defaults = {
        'default_value1':True,
        'default_value2':True,
        'default_value3':True,
    }
    for name, value in defaults.items():
        setattr(cls, name, some_complex_init_function(value, ...))
    return cls

@apply_defaults
class Settings(object):
    pass'''

