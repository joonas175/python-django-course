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


def index(request):
    challenges = get_challenges()
    months = list(challenges.keys())
    return HttpResponse(f"""
        <ul>
            {''.join([f"""
                <li><a href=\"{reverse('month-challenge', args=[month])}\">{month.capitalize()}</a></li>
            """ for month in months])}
        </ul>""")


def monthly_challenge_by_number(request, month: int):

    challenges = get_challenges()
    months = list(challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month!")

    redirect_month = months[month - 1]

    # redirect_path = f"/challenges/{redirect_month}"

    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month: str):

    challenges = get_challenges()

    challenge = challenges.get(month)

    return render(
        request,
        "challenges/challenge.html", {"challenge": challenge, "month": month},
        status=200 if challenge else 404
    )
