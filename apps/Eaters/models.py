from __future__ import unicode_literals
from ..loginreg.models import User
from django.db import models

# Create your models here.
class Eater(models.Model):
    restaurant = models.TextField(max_length = 50)
    address = models.TextField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User)
