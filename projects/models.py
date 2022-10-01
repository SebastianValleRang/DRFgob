from django.db import models

# Create your models here.

class Project(models.Model):

    Titulo = models.CharField(max_length = 200)
    Calificacion = models.IntegerField()
    Pais = models.CharField(max_length = 200)
