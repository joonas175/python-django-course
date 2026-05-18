from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Book

# Create your views here.

def index(request):
    all_books = Book.objects.all()
    return render(request, 'book_outlet/index.html', {
        'all_books': all_books
    })

def book_detail(request, book_slug):
    # try:
    #    book = Book.objects.get(id=book_id)
    # except Book.DoesNotExist:
    #     raise Http404("Book does not exist")
    
    book = get_object_or_404(Book, slug=book_slug)

    return render(request, 'book_outlet/book_detail.html', {
        'book': book
    })