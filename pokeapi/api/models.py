from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User


class Favoritos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pok_id = models.PositiveIntegerField(max_length=64)

