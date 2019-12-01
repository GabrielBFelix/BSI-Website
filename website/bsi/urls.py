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

    

    path('aluno/<int:id>', views.aluno, name='aluno'),

    path('laboratorio/<int:id>', views.laboratorio, name='laboratorio'),

    path('noticia/<int:id>', views.noticia, name='noticia'),
]