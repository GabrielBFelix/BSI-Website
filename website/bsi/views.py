from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("HOME PAGE")

def professor(request, id):
    return HttpResponse("Olhando o professor com id %i" % id)

def aluno(request, id):
    return HttpResponse("Olhando o Aluno com id %i" % id)

def laboratorio(request, id):
    return HttpResponse("Olhando o Laboratorio com id %i" % id)

def noticia(request, id):
    return HttpResponse("Olhando o Noticia com id %i" % id)

def projeto(request, id):
    return HttpResponse("Olhando o Projeto com id %i" % id)