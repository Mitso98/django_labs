from django.shortcuts import render, get_object_or_404
from authors.models import Author
from books.models import Book

# Create your views here.


def authors(req):
    authors = Author.objects.all()

    ctx = {
        'authors': authors
    }
    return render(req, 'authors_index.html', ctx)


def author(req, author_id):
    author = get_object_or_404(Author, id=author_id)
    book = Book.objects.get(writer_id=author.id)
 
    ctx = {
        'author': author,
        'book': book
    }
    return render(req, 'author.html', ctx)
