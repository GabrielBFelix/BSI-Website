from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),

    path('professor/<int:id>', views.professor, name='professor'),

    path('aluno/', views.AlunoList.as_view(), name='aluno_list'),
    path('aluno/view/<int:pk>', views.AlunoDetail.as_view(), name='aluno_view'),
    path('aluno/new', views.AlunoCreate.as_view(), name='aluno_new'),
    path('aluno/edit/<int:pk>', views.AlunoUpdate.as_view(), name='aluno_edit'),
    path('aluno/delete/<int:pk>', views.AlunoDelete.as_view(), name='aluno_delete'),

    path('laboratorio/<int:id>', views.laboratorio, name='laboratorio'),

    path('projeto/<int:id>', views.projeto, name='projeto'),

    path('noticia/<int:id>', views.noticia, name='noticia'),
]