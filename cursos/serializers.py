from rest_framework import serializers
from .models import Aluno, Curso, Matricula
from .validators import *

class AlunoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'email', 'rg', 'cpf', 'data_nascimento']

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"O CPF deve conter 11 dígitos numéricos."})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': "O nome precisa conter somente letras."})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':"O RG deve conter 9 dígitos numéricos"})
        return data
    

class CursoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Matricula
        fields = '__all__'
    
class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):

    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()
    
class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):

    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')

    class Meta:
        model = Matricula
        fields = ['aluno_nome']