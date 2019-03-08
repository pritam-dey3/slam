#response_form/models.py

import sys
sys.path.insert(0,'..')

from django.db import models
from django.conf import settings
from slam.questions_and_answers import fields as f 


class ResponseModel(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    submit_count = models.IntegerField(default=0)
    rpublic = models.BooleanField(default=False)
    final_res = models.TextField(blank=True)

    def __str__(self):
        return str(self.author) + str(self.submit_count)

for key, value in f.items():
    ResponseModel.add_to_class(key, models.TextField(value[0], blank=True))