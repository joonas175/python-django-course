from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import ReviewForm
from .models import Review

# Create your views here.


def review(request: HttpRequest):

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            # name = form.cleaned_data['user_name']
            # print(f'Submitted: {name}')
            # review = Review(
            #     user_name=form.cleaned_data['user_name'],
            #     review_text=form.cleaned_data['review_text'],
            #     rating=form.cleaned_data['rating']
            # )
            # review.save()
            form.save()
            return HttpResponseRedirect(reverse('thank_you'))
        else:
            return render(request, 'reviews/review.html', {
                'form': form
            })

    form = ReviewForm()

    return render(request, 'reviews/review.html', {
        'form': form
    })


def thank_you(request: HttpRequest):
    return render(request, 'reviews/thank_you.html')
