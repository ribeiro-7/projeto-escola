from rest_framework import viewsets
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

class CursosViewSet(viewsets.ModelViewSet):

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class AvaliacaoAPIView(viewsets.ModelViewSet):
    
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer