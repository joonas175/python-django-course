
from django import forms

from .models import Review


# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label='Your username', max_length=100)
#     review_text = forms.CharField(label='Your review', widget=forms.Textarea, max_length=500)
#     rating = forms.IntegerField(label='Your rating', min_value=1, max_value=5, initial=3)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        labels = {
            'user_name': 'Your username',
            'review_text': 'Your review',
            'rating': 'Your rating'
        }
