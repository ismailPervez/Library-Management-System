from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='student-home'),
    path('register/', views.register, name='student-register'),
]