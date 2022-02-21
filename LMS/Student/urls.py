from django.urls import path
from . import views
from Student.api import views as api_views

urlpatterns = [
    path('', views.index, name='student-home'),
    path('register/', views.register, name='student-register'),
    path('login/', views.log_in, name='student-login'),
    path('update/<email>', api_views.update_student),
]