from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import DeleteView
from .forms import LoginForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.generic.base import TemplateView
from .models import Student
from django.urls import reverse_lazy

# Create your views here.



class Home(TemplateView):
    template_name = 'home.html'


class CustomLoginView(LoginView):
    # form_class = LoginForm
    template_name = 'login.html'

class LogoutTemplateView(TemplateView):
    template_name = 'logout.html'


class CustomLogoutView(LogoutView):
    pass

class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_delete_confirm.html'
    success_url = reverse_lazy('student_list')