from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, Http404

from .models import Professor, Aluno, Laboratorio, Projeto, Noticia

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from . import models

def index(request):
    noticia_list = Noticia.objects.order_by('nome')
    professor_list = Professor.objects.order_by('nome')
    aluno_list = Aluno.objects.order_by('nome')
    laboratorio_list = Laboratorio.objects.order_by('nome')
    projeto_list = Projeto.objects.order_by('nome')
    template = loader.get_template('bsi/index.html');
    context = {'professor_list': professor_list, 'noticia_list': noticia_list, 'aluno_list': aluno_list, 'laboratorio_list': laboratorio_list, 'projeto_list': projeto_list}
    return render(request, 'bsi/index.html', context)

class ProfessorList(ListView):
    model = models.Professor
    success_url = reverse_lazy('professor_list')
class ProfessorView(DetailView):
    model = models.Professor
    success_url = reverse_lazy('professor_list')

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