from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='library-home'),
    path('register/', views.register, name='library-register'),
    path('librarian/', include('Librarian.urls')),
    path('student/', include('Student.urls')),
]