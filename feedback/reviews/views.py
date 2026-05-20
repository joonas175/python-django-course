from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic import TemplateView, FormView

# Create your views here.


class ReviewView(FormView):
    template_name = 'reviews/review.html'
    form_class = ReviewForm
    success_url = '/thank-you/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

    # def get(self, request: HttpRequest):
    #     form = ReviewForm()
    #     return render(request, 'reviews/review.html', {
    #         'form': form
    #     })

    # def post(self, request: HttpRequest):
    #     form = ReviewForm(request.POST)

    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(reverse('thank_you'))
    #     else:
    #         return render(request, 'reviews/review.html', {
    #             'form': form
    #         })

# def review(request: HttpRequest):

#     if request.method == 'POST':
#         form = ReviewForm(request.POST)

#         if form.is_valid():
#             # name = form.cleaned_data['user_name']
#             # print(f'Submitted: {name}')
#             # review = Review(
#             #     user_name=form.cleaned_data['user_name'],
#             #     review_text=form.cleaned_data['review_text'],
#             #     rating=form.cleaned_data['rating']
#             # )
#             # review.save()
#             form.save()
#             return HttpResponseRedirect(reverse('thank_you'))
#         else:
#             return render(request, 'reviews/review.html', {
#                 'form': form
#             })

#     form = ReviewForm()

#     return render(request, 'reviews/review.html', {
#         'form': form
#     })


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

