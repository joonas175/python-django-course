from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def january(request):
    return HttpResponse("This works!")


def february(request):
    return HttpResponse("February hello!")


def monthly_challenge(request, month):

    challenges = {
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

    challenge = challenges.get(month)

    if challenge:
        return HttpResponse(challenge)
    else:
        return HttpResponseNotFound(f"Month {month} not found!")
