from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.template import loader

from . import models

from .models import Professor, Aluno, Laboratorio, Projeto, Noticia

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

class ProjetoList(ListView):
    model = models.Projeto
class ProjetoView(DetailView):
    model = models.Projeto
class ProjetoCreate(CreateView):
    model = models.Projeto
    fields = ['nome', 'coordenador', 'numVagas', 'descricao']
    success_url = reverse_lazy('projeto_list')
class ProjetoUpdate(UpdateView):
    model = models.Projeto
    fields = ['nome', 'coordenador', 'numVagas', 'descricao']
    success_url = reverse_lazy('projeto_list')
class ProjetoDelete(DeleteView):
    model = models.Projeto
    success_url = reverse_lazy('projeto_list')

class LaboratorioList(ListView):
    model = models.Laboratorio

class LaboratorioView(DetailView):
    model = models.Laboratorio

class LaboratorioCreate(CreateView):
    model = models.Laboratorio
    fields = ['nome', 'coordenador', 'descricao']
    success_url = reverse_lazy('laboratorio_list')

class LaboratorioUpdate(UpdateView):
    model = models.Laboratorio
    fields = ['nome', 'coordenador', 'descricao']
    success_url = reverse_lazy('laboratorio_list')

class LaboratorioDelete(DeleteView):
    model = models.Laboratorio
    success_url = reverse_lazy('laboratorio_list')

class AlunoCreate(CreateView):
    model = models.Aluno
    fields = ['nome', 'username', 'email', 'senha']
    success_url = reverse_lazy('aluno_list')
    
class AlunoUpdate(UpdateView):
    model = models.Aluno
    fields = ['nome', 'username', 'email', 'senha']
    success_url = reverse_lazy('aluno_list')

class AlunoDelete(DeleteView):
    model = models.Aluno
    success_url = reverse_lazy('aluno_list')

class AlunoList(ListView):
    model = models.Aluno

class AlunoDetail(DetailView):
    model = models.Aluno


def aluno(request, id):
    return HttpResponse("Olhando o Aluno com id %i" % id)

def laboratorio(request, id):
    return HttpResponse("Olhando o Laboratorio com id %i" % id)

def noticia(request, id):
    return HttpResponse("Olhando o Noticia com id %i" % id)

