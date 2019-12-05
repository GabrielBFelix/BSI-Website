from django.contrib import admin

from .models import Professor
from .models import Aluno
from .models import Laboratorio
from .models import Noticia
from .models import Projeto
from .models import Estagio

admin.site.register(Professor)
admin.site.register(Aluno)
admin.site.register(Laboratorio)
admin.site.register(Noticia)
admin.site.register(Projeto)
admin.site.register(Estagio)

