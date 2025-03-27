from rest_framework import serializers
from .models import Curso, Avaliacao

class AvaliacaoSerializer(serializers.Serializer):
    
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )

class CursoSerializer(serializers.Serializer):
    
    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
        )