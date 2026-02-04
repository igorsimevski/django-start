from django.shortcuts import render
from .models import Book


def index(request):
    books = Book.objects.all()
    return render(request, "book_outlet/index.html", {"books": books})

def book_detail(request, id):
    book = Book.objects.get(id=id)
    return render(request, "book_outlet/book_detail.html", {"book": book})