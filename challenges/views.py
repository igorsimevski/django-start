from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound


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


def monthly_challenge_by_number(request, month):
    if month < 1 or month > 12:
        return HttpResponseNotFound("Invalid month number!")
    months = list(monthly_challenges.keys())
    return HttpResponseRedirect(f"/challenges/{months[month - 1]}")


def monthly_challenge(request, month):

    challenge_text = monthly_challenges.get(month, "This month is not supported.")
    return HttpResponse(challenge_text)
