from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from . import models

def index(request):
    return HttpResponse("HOME PAGE")

class ProfessorList(ListView):
    model = models.Professor
class ProfessorView(DetailView):
    model = models.Professor

class ProfessorCreate(CreateView):
    model = models.Professor
    fields = ['nome', 'username', 'senha', 'email']
    success_url = reverse_lazy('professor_list')

class ProfessorUpdate(UpdateView):
    model = models.Professor
    fields = ['nome', 'username', 'senha', 'email']
    success_url = reverse_lazy('professor_list')

class ProfessorDelete(DeleteView):
    model = models.Professor
    success_url = reverse_lazy('professor_list')

def aluno(request, id):
    return HttpResponse("Olhando o Aluno com id %i" % id)

def laboratorio(request, id):
    return HttpResponse("Olhando o Laboratorio com id %i" % id)

def noticia(request, id):
    return HttpResponse("Olhando o Noticia com id %i" % id)

def projeto(request, id):
    return HttpResponse("Olhando o Projeto com id %i" % id)