
from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(label='Your username', max_length=100)
    review_text = forms.CharField(label='Your review', widget=forms.Textarea)
    rating = forms.IntegerField(label='Your rating', min_value=1, max_value=5, initial=3)