#users/models.py
import sys
sys.path.insert(0,'..')

from django.db import models
from django.contrib.auth.models import AbstractUser
import questions_and_answers
from django.utils.translation import gettext as _
from slam.questions_and_answers import fields as f
from slam.questions_and_answers import intro2, outro


#@apply_defaults
class CustomUser(AbstractUser):
    count = models.IntegerField(default=0)
    intro = models.TextField(default=intro2)
    out = models.TextField(default=outro)
    

for key, value in f.items():
    CustomUser.add_to_class(key + '-Q', models.CharField(default=value[0], max_length=400))
    CustomUser.add_to_class(key + '-H', models.TextField(default=value[1]))
   
'''
class MyModel(models.Model):
    pass

for label in labels:
    MyModel.add_to_class(label, models.CharField(max_length=255))
'''

