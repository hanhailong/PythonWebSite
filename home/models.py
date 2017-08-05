# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class UserModel(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)

    def getName(self):
        return ""
