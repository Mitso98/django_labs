from django.shortcuts import render
from django.shortcuts import get_object_or_404, HttpResponse
from books.models import Book
from authors.models import Author
# Create your views here.


def book(req, book_id):
    book = get_object_or_404(Book, id=book_id)
    author = Author.objects.get(id=book.writer_id)
    ctx = {
        'book': book,
        'author': author
    }
    return render(req, 'books_index.html', ctx)
