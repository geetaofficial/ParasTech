from django.db.models import query
from rest_framework.generics import ListAPIView
from app.models import Student
from .serializers import StudentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class StudentListAPIView(ListAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    filter_backends = [filters.SearchFilter]
    filterset_fields = ['name','s_class__name']
