from rest_framework import viewsets, generics
from .models import Curso, Aluno, Matricula
from .serializers import CursoSerializer, AlunoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer

class AlunoViewSet(viewsets.ModelViewSet):

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursoViewSet(viewsets.ModelViewSet):
    
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):

    queryset = Matricula.objaects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculasAluno(generics.ListAPIView):

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer