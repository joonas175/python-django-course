from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.

def review(request: HttpRequest):
    if request.method == 'POST':
        name = request.POST.get('name')

        return render(request, 'reviews/thank_you.html', {
            'name': name,
        })

    return render(request, 'reviews/review.html')