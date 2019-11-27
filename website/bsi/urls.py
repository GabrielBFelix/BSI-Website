from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('professor/<int:id>', views.professor, name='professor'),

    path('aluno/<int:id>', views.aluno, name='aluno'),

    path('laboratorio/<int:id>', views.laboratorio, name='laboratorio'),

    path('projeto/<int:id>', views.projeto, name='projeto'),

    path('noticia/<int:id>', views.noticia, name='noticia'),
]