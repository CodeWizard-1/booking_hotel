from .models import Guest_reviews, Booking
from django import forms
from django.db import models


class Guest_reviewsForm(forms.ModelForm):
    class Meta:
        model = Guest_reviews
        fields = ('body', )


class BookingForm(forms.ModelForm):
    checking_date = forms.DateField(
        input_formats=['%d.%m.%Y'],
        widget=forms.TextInput(attrs={'class': 'datepicker'}))
    checkout_date = forms.DateField(
        input_formats=['%d.%m.%Y'],
        widget=forms.TextInput(attrs={'class': 'datepicker'}))
    phone_number = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = Booking
        fields = ['phone_number', 'checking_date', 'checkout_date', 'email']
