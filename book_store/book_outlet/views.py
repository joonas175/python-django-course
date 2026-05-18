from django.shortcuts import render
from .models import Book

# Create your views here.

def index(request):
    all_books = Book.objects.all()
    return render(request, 'book_outlet/index.html', {
        'all_books': all_books
    })

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'book_outlet/book_detail.html', {
        'book': book
    })