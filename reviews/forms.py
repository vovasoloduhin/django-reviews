from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'text', 'rating']
        widgets = {
            'author': forms.TextInput(attrs={'placeholder': "Ваше ім'я"}),
            'text': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Ваш відгук'}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if not 1 <= rating <= 5:
            raise forms.ValidationError('Рейтинг має бути від 1 до 5.')
        return rating
