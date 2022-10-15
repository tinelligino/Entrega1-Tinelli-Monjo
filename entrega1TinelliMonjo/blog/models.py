from unittest.util import _MAX_LENGTH
from django.db import models


class User(models.Model):
    nombre=models.CharField(max_length=50)
    email=models.EmailField()
    telefono=models.CharField(max_length=50)

class Contact(models.Model):
    asunto=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)

class Historia(models.Model):
    resumen=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)
