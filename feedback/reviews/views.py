from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from .models import Review


def review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            # data = form.cleaned_data
            # review = Review(
            #     user_name=data["user_name"],
            #     review_text=data["review_text"],
            #     rating=data["rating"],
            # )
            # review.save()
            #
            # Alternatively: 
            form.save()
            return HttpResponseRedirect("/thank_you")

    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {"form": form})


def thank_you(request):
    return render(request, "reviews/thank_you.html")
