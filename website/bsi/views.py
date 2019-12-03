from django.shortcuts import render
from django.http import HttpResponse
from .models import Aluno
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

def index(request):
    return HttpResponse("HOME PAGE")

def professor(request, id):
    return HttpResponse("Olhando o professor com id %i" % id)

def aluno(request, id):
    return HttpResponse("Olhando o Aluno com id %i" % id)

class AlunoCreate(CreateView):
    model = Aluno

class AlunoUpdate(UpdateView):
    model = Aluno

class AlunoDelete(DeleteView):
    model = Aluno

class AlunoList(ListView):
    model = Aluno

class AlunoDetail(DetailView):
    model = Aluno

def laboratorio(request, id):
    return HttpResponse("Olhando o Laboratorio com id %i" % id)

def noticia(request, id):
    return HttpResponse("Olhando o Noticia com id %i" % id)

def projeto(request, id):
    return HttpResponse("Olhando o Projeto com id %i" % id)