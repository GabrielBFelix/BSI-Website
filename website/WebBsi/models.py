from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=40)
    matricula = models.IntegerField(4)
    username = models.CharField(max_length=40)
    senha = models.CharField(max_length=20)
    email = models.CharField(max_length=60)

class Evento(models.Model):
    codigo = models.IntegerField(4)
    nome = models.CharField(max_length=40)
    numeroVagas = models.IntegerField(4)
    local = models.CharField(max_length=40)

