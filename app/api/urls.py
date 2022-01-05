from django.urls import path
from .views import StudentListAPIView

urlpatterns = [
    path('student-search/',StudentListAPIView.as_view(), name='student-search')
]
