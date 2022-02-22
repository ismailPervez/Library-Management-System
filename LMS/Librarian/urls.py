from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='librarian-home'),
    path('register/', views.register, name='librarian-register'),
    path('login/', views.log_in, name='librarian-login'),
]