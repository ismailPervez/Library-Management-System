from django.urls import path
from . import views 
from Librarian.api import views as api_views

urlpatterns = [
    path('', views.index, name='librarian-home'),
    path('register/', views.register, name='librarian-register'),
    path('login/', views.log_in, name='librarian-login'),
    path('update/<email>', api_views.update_user),
    path('add-book', api_views.add_book), # should not end with a trailing slash
    path('borrow-book', api_views.register_taken_book),
]