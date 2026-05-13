from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def january(request):
    return HttpResponse("This works!")


def february(request):
    return HttpResponse("February hello!")


def get_challenges():
    return {
        "january": "January challenge",
        "february": "February challenge",
        "march": "March challenge",
        "april": "April challenge",
        "may": "May challenge",
        "june": "June challenge",
        "july": "July challenge",
        "august": "August challenge",
        "september": "September challenge",
        "october": "October challenge",
        "november": "November challenge",
        "december": "December challenge"
    }


def monthly_challenge_by_number(request, month):

    challenges = get_challenges()
    months = list(challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month!")

    redirect_month = months[month - 1]

    # redirect_path = f"/challenges/{redirect_month}"

    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):

    challenges = get_challenges()

    challenge = challenges.get(month)

    if challenge:
        return HttpResponse(challenge)
    else:
        return HttpResponseNotFound(f"Month {month} not found!")
