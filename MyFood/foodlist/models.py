from django.db import models
import sqlite3
from django.db.backends.signals import connection_created
from django.core.signals import request_started



class Food(models.Model):
    name = models.CharField(max_length=30)
    info = models.TextField()
    img_link = models.TextField()
    type = models.ForeignKey('Type', null=True, on_delete=models.PROTECT)


class Type(models.Model):
    type = models.CharField(max_length=50)
#
    def __str__(self):
        return self.type


