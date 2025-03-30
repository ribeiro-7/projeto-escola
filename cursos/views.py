from rest_framework import viewsets
from .models import Curso, Aluno
from .serializers import CursoSerializer, AlunoSerializer

class AlunoViewSet(viewsets.ModelViewSet):

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursoViewSet(viewsets.ModelViewSet):
    
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer