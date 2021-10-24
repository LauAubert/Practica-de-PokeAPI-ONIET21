from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField

class Favoritos(models.Model):
    pokemon_name = CharField(max_length=50)
