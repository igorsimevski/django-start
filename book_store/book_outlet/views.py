from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import Http404


def index(request):
    books = Book.objects.all()
    return render(request, "book_outlet/index.html", {"books": books})


def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, "book_outlet/book_detail.html", {"book": book})
