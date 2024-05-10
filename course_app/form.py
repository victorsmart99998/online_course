from .models import ProductReview
from django import forms


class ProductReviewForm(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Leave A Comment'}))

    class Meta:
        model = ProductReview
        fields = ['review', 'rating']
