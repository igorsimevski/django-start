from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import Http404
from django.db.models import Avg


def index(request):
    books = Book.objects.all().order_by("-title")
    number_of_books = books.count()
    average_rating = books.aggregate(Avg("rating"))["rating__avg"]
    return render(
        request,
        "book_outlet/index.html",
        {
            "books": books,
            "total_books": number_of_books,
            "average_rating": average_rating,
        },
    )


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_detail.html", {"book": book})
