from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='library-home'),
    path('librarian/', include('Librarian.urls')),
    path('student/', include('Student.urls')),
]