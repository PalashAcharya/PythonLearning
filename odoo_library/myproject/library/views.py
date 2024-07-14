from .models import Book, Author, Genre
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Book, Author, Genre
from .utils import fetch_book_data

def index(request):
    num_books = Book.objects.all().count()
    num_authors = Author.objects.all().count()
    num_genres = Genre.objects.all().count()

    context = {
        'num_books': num_books,
        'num_authors': num_authors,
        'num_genres': num_genres,
    }

    return render(request, 'index.html', context)

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})

def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'genre_list.html', {'genres': genres})


def add_book(request):
    if request.method == 'POST':
        isbn = request.POST.get('isbn')
        api_key = settings.GOOGLE_BOOKS_API_KEY
        book_data = fetch_book_data(isbn, api_key)
        if book_data:
            author_name = book_data['authors'][0]
            author, created = Author.objects.get_or_create(name=author_name)
            
            book = Book(
                title=book_data['title'],
                author=author,
                summary=book_data['description'],
                isbn=isbn,
                available=True,
                image_url=book_data['image_url']  # Save the image URL
            )
            book.save()
            
            for genre_name in book_data['categories']:
                genre, created = Genre.objects.get_or_create(name=genre_name)
                book.genre.add(genre)
            
            book.save()
            return redirect('book_list')
    return render(request, 'add_book.html')