from django.db import models

# Create your models here.
class Tarefa(models.Model):
    nome = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    prazo = models.DateField(auto_now='')

