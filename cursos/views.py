from rest_framework import viewsets
from .models import Curso, Aluno, Matricula
from .serializers import CursoSerializer, AlunoSerializer, MatriculaSerializer

class AlunoViewSet(viewsets.ModelViewSet):

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursoViewSet(viewsets.ModelViewSet):
    
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):

    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer