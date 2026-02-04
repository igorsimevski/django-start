from django.shortcuts import render
from .models import Book
from django.http import Http404


def index(request):
    books = Book.objects.all()
    return render(request, "book_outlet/index.html", {"books": books})


def book_detail(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    return render(request, "book_outlet/book_detail.html", {"book": book})
