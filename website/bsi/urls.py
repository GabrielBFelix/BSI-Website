from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('professor/<int:id>', views.professor, name='professor'),

    path('aluno/', views.AlunoList.as_view(), name='aluno_list'),
    path('aluno/views/<int:id>', views.AlunoDetail.as_view(), name='aluno_detail'),
    path('aluno/create', views.AlunoCreate.as_view(), name='aluno_create'),
    path('aluno/update/<int:id>', views.AlunoUpdate.as_view(), name='aluno_update'),
    path('aluno/delete/<int:id>', views.AlunoDelete.as_view(), name='aluno_delete'),

    path('laboratorio/<int:id>', views.laboratorio, name='laboratorio'),

    path('projeto/<int:id>', views.projeto, name='projeto'),

    path('noticia/<int:id>', views.noticia, name='noticia'),
]