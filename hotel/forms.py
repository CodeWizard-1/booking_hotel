from .models import Guest_reviews
from django import forms


class Guest_reviewsForm(forms.ModelForm):
    class Meta:
        model = Guest_reviews
        fields = ('body', )
