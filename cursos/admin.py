from django.contrib import admin
from .models import Curso, Aluno, Matricula

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome', 'email')
    search_fields = ('nome',)
    list_per_page = 10
    ordering = ('nome',)

admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso',)

admin.site.register(Curso, Cursos)

class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'periodo')
    list_display_links = ('id',)

admin.site.register(Matricula, Matriculas)