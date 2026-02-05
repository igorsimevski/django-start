from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from .forms import ReviewForm
from .models import Review


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/review.html", {"form": form})

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank_you")
        return render(request, "reviews/review.html", {"form": form})


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


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "This Works"
        return context
