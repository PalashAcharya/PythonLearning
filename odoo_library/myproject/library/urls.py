from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.book_list, name='book_list'),
    path('books/add/', views.add_book, name='add_book'),
    path('authors/', views.author_list, name='author_list'),
    path('genres/', views.genre_list, name='genre_list'),
]
