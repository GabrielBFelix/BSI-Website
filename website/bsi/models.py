from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    coordenador = models.ForeignKey(Professor, on_delete=models.SET("0"))
    numVagas = models.IntegerField(default=0)
    descricao = models.CharField(max_length=300)
    def __str__(self):
        return self.nome

class Noticia(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.ForeignKey(Professor, on_delete=models.SET("0"))
    descricao = models.CharField(max_length=300)
    def __str__(self):
        return self.nome

class Laboratorio(models.Model):
    nome = models.CharField(max_length=100)
    coordenador = models.ForeignKey(Professor, null=True, on_delete=models.SET_NULL)
    descricao = models.CharField(max_length=300)
    def __str__(self):
        return self.nome

class Estagio(models.Model):
    organizacao = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    profCoordenador = models.ForeignKey(Professor, on_delete=models.SET("0"))
    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    vagaEstagio = models.ForeignKey(Estagio, null = True, blank = True, on_delete=models.SET("0"))
    def __str__(self):
        return self.nome
