from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("HOME PAGE")

def professor(request, id, nome):
    return HttpResponse("Olhando o professor com id %s e com o nome %s." % id % nome)

def Aluno(request, id, nome):
    return HttpResponse("Olhando o Aluno com id %s e com o nome %s." % id % nome)

def Laboratorio(request, id, nome):
    return HttpResponse("Olhando o Laboratorio com id %s e com o nome %s." % id % nome)

def Noticia(request, id, nome):
    return HttpResponse("Olhando o Noticia com id %s e com o nome %s." % id % nome)

def Projeto(request, id, nome):
    return HttpResponse("Olhando o Projeto com id %s e com o nome %s." % id % nome)