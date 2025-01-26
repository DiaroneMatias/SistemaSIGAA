from django.contrib import admin

from .models import Curso
from .models import Aluno
from .models import PeriodoLetivo
from .models import Disciplina
from .models import Turma
from .models import Professor
from .models import Matricula

# Register your models here.


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'matricula']
        
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'totalCreditos']

#admin.site.register(Aluno)
admin.site.register(PeriodoLetivo)
admin.site.register(Disciplina)
admin.site.register(Turma)
admin.site.register(Professor)
admin.site.register(Matricula)
