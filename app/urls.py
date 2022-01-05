from django.urls import path, include
from .views import Home, CustomLoginView, StudentListView, StudentDeleteView, LogoutTemplateView, CustomLogoutView
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('student_list/', StudentListView.as_view(), name='student_list'),
    path('student_delete/<int:pk>/',
         StudentDeleteView.as_view(), name='student_delete'),
    path('logout/', LogoutTemplateView.as_view(), name='logout'),
    path('authlogout/', CustomLogoutView.as_view(), name='authlogout'),
    path('api/',include('app.api.urls'))
]
