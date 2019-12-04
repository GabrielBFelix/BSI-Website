from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [

    path('', views.index, name='index'),


    path('professor/', views.ProfessorList.as_view(), name='professor_list'),
    path('professor/view/<int:pk>', views.ProfessorView.as_view(), name='professor_view'),
    path('professor/new', views.ProfessorCreate.as_view(), name='professor_new'),
    path('professor/edit/<int:pk>', views.ProfessorUpdate.as_view(), name='professor_edit'),
    path('professor/delete/<int:pk>', views.ProfessorDelete.as_view(), name='professor_delete'),
    

    path('projeto/', views.ProjetoList.as_view(), name='projeto_list'),
    path('projeto/view/<int:pk>', views.ProjetoView.as_view(), name='projeto_view'),
    path('projeto/new', views.ProjetoCreate.as_view(), name='projeto_new'),
    path('projeto/edit/<int:pk>', views.ProjetoUpdate.as_view(), name='projeto_edit'),
    path('projeto/delete/<int:pk>', views.ProjetoDelete.as_view(), name='projeto_delete'),

    path('laboratorio', views.LaboratorioList.as_view(), name='laboratorio_list'),
    path('laboratorio/view/<int:pk>', views.LaboratorioView.as_view(), name='laboratorio_view'),
    path('laboratorio/new', views.LaboratorioCreate.as_view(), name='laboratorio_new'),
    path('laboratorio/edit/<int:pk>', views.LaboratorioUpdate.as_view(), name='laboratorio_edit'),
    path('laboratorio/delete/<int:pk>', views.LaboratorioDelete.as_view(), name='laboratorio_delete'),
    
    path('aluno/', views.AlunoList.as_view(), name='aluno_list'),
    path('aluno/view/<int:pk>', views.AlunoDetail.as_view(), name='aluno_view'),
    path('aluno/new', views.AlunoCreate.as_view(), name='aluno_new'),
    path('aluno/edit/<int:pk>', views.AlunoUpdate.as_view(), name='aluno_edit'),
    path('aluno/delete/<int:pk>', views.AlunoDelete.as_view(), name='aluno_delete'),

    path('laboratorio/<int:id>', views.laboratorio, name='laboratorio'),

    path('noticia/<int:id>', views.noticia, name='noticia'),
]