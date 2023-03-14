from rest_framework.views import APIView, Response
from .models import Aula, Professor
from .serializer import ProfessorSerializer, CadastrarAulaSerializer, AulaSerializer
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST) 
from django.shortcuts import get_object_or_404, get_list_or_404

# Create your views here.
class ProfessorApiView(APIView):
    def get(self, request, format=None):
        professores = Professor.objects.all()
        serializer = ProfessorSerializer(professores, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class CadastrarAulaApiView(APIView):
    def post(self, request, id, format=None):
        professor_ = get_object_or_404(Professor, id = id)
        serializer = CadastrarAulaSerializer(data=request.data)
        if serializer.is_valid():
            aula = Aula.objects.create(nome = serializer.validated_data.get("nome"), email = serializer.validated_data.get("email"),professor = professor_)
            aula.save()
            aula_serializer = AulaSerializer(aula, many=False)
            return Response(aula_serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def get(self, request ,id, format=None):
        aulas_professor = get_list_or_404(Aula, professor=id)
        aulas_professor_serialized = AulaSerializer(aulas_professor, many=True)
        return Response(aulas_professor_serialized.data, status=200)

