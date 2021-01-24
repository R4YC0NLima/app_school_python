from django.shortcuts import render
from grades.models import Student
from django.http import JsonResponse
from grades.serializers import StudentSerializer
from rest_framework import viewsets, mixins

# Create your views here.

class StudentViewSet(viewsets.ModelViewSet, mixins.ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# def grades(request):
#     if(request.method == 'GET'):
#         student = Student.objects.first()
#         serializer = StudentSerializer(student)
#         return JsonResponse(serializer.data)