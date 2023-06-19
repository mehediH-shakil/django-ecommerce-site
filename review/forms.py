from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']

        widgets = {
            'rating': forms.NumberInput(attrs={'class': 'input--style-4', 'min': '0', 'max': '5', 'style': 'border-color: gray;'}),
            'comment': forms.Textarea(attrs={'class': 'input--style-4', 'rows': 4, 'style': 'border-color: gray; width: 100%;'})
        }
