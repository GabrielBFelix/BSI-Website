from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('list/professor', views.ProfessorList.as_view(), name='professor_list'),
    path('view/professor/<int:pk>', views.ProfessorView.as_view(), name='professor_view'),
    path('new/professor', views.ProfessorCreate.as_view(), name='professor_new'),
    path('edit/professor/<int:pk>', views.ProfessorUpdate.as_view(), name='professor_edit'),
    path('delete/professor/<int:pk>', views.ProfessorDelete.as_view(), name='professor_delete'),

    path('aluno/<int:id>', views.aluno, name='aluno'),

    path('laboratorio/<int:id>', views.laboratorio, name='laboratorio'),

    path('projeto/<int:id>', views.projeto, name='projeto'),

    path('noticia/<int:id>', views.noticia, name='noticia'),
]