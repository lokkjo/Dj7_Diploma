from django import forms
from .models import Review

RATING_CHOICES = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
]

class ReviewCreateForm(forms.ModelForm):
    """
    Форма создания отзыва на странице наименования товара (item page)
    """
    rating = forms.ChoiceField(choices=RATING_CHOICES,
                               widget=forms.RadioSelect())

    class Meta:
        model = Review
        fields = ['text', 'rating']
        exclude = ['author', 'reviewed_item']
        widgets = {
            'text': forms.Textarea(attrs={
                    'id': "content",
                    'placeholder': "Содержание",
                    'class': 'form-control',
                    }),
        }
