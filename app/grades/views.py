from django.shortcuts import render
from grades.models import Aluno
from django.http import JsonResponse
from grades.serializers import AlunoSerializer
from rest_framework import viewsets, mixins

# Create your views here.

class AlunoViewSet(viewsets.ModelViewSet, mixins.ListModelMixin):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

# def grades(request):
#     if(request.method == 'GET'):
#         student = Student.objects.first()
#         serializer = StudentSerializer(student)
#         return JsonResponse(serializer.data)