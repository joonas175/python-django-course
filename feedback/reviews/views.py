from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.


def review(request: HttpRequest):
    if request.method == 'POST':
        name = request.POST.get('name')
        print(f'Submitted: {name}')
        return HttpResponseRedirect(reverse('thank_you'))

    return render(request, 'reviews/review.html')


def thank_you(request: HttpRequest):
    return render(request, 'reviews/thank_you.html')
