from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='library-home'),
    path('register/', views.register, name='library-register'),
    path('login/', views.login, name='library-login'),
    path('librarian/', include('Librarian.urls')),
    path('student/', include('Student.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('explore/', views.explore, name='explore-library'),
    path('book/<book_id>', views.get_book, name='full-book'),
    path('search/<query>', views.search, name='search')
]