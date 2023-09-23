from django.forms import ModelForm,Textarea
from .models import ReviewRating

class ReviewForm(ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['review', 'rating']
        widgets = {
            'review': Textarea(attrs={'cols': 46, 'rows': 5}),
            
        }