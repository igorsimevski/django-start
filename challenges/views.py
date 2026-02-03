from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse


monthly_challenges = {
    "january": "Walk for at least 1 minutes every day.",
    "february": "Walk for at least 2 minutes every day.",
    "march": "Walk for at least 3 minutes every day.",
    "april": "Walk for at least 4 minutes every day.",
    "may": "Walk for at least 5 minutes every day.",
    "june": "Walk for at least 6 minutes every day.",
    "july": "Walk for at least 7 minutes every day.",
    "august": "Walk for at least 8 minutes every day.",
    "september": "Walk for at least 9 minutes every day.",
    "october": "Walk for at least 10 minutes every day.",
    "november": "Walk for at least 11 minutes every day.",
    "december": "Walk for at least 12 minutes every day.",
}


def index(request):
    months = list(monthly_challenges.keys())
    response_data = "<ul>"
    for month in months:
        response_data += f'<li><a href="{month}">{month.capitalize()}</a></li>'
    response_data += "</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    if month < 1 or month > 12:
        return HttpResponseNotFound("Invalid month number!")
    months = list(monthly_challenges.keys())
    redirect_path = reverse("month-challenge", args=[months[month - 1]])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):

    try:
        challenge_text = monthly_challenges.get(month, "This month is not supported.")
        response_data = render(request, "challenges/challenge.html", {"challenge_text": challenge_text, "month": month.capitalize()})

        return HttpResponse(response_data)
    except KeyError:
        return HttpResponseNotFound("This month is not supported.")
