from django.db import models

# Create your models here.
class Preguntas(models.Model):
    pregunta = models.CharField(max_length=200)
