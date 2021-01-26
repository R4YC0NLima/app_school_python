from django.contrib import admin

# Register your models here.
from grades.models import Prova
from grades.models import Gabarito
from grades.models import Aluno
from grades.models import GabaritoAluno

@admin.register(Prova)
class ProvaAdmin(admin.ModelAdmin):
    list_display = ('id', 'materia', 'questao', 'resposta', 'created_at', 'updated_at')

@admin.register(Gabarito)
class GabaritoAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_prova', 'questao', 'resposta', 'created_at', 'updated_at')

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'nota', 'status', 'created_at', 'updated_at')

@admin.register(GabaritoAluno)
class GabaritoAlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_aluno', 'id_prova', 'questao', 'resposta', 'created_at', 'updated_at')
