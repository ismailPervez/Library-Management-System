from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='student-home'),
    path('register/', views.register, name='student-register'),
    path('login/', views.log_in, name='student-login'),
]