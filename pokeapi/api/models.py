from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, IntegerField


class Favoritos(models.Model):
    user = object(max_length=50)
    pok_id = IntegerField(max_length=50)