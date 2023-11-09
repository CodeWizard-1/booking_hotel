from .models import Booking
from .models import Guest_reviews, Booking
from django import forms
from django.db import models
from datetime import date, datetime


class Guest_reviewsForm(forms.ModelForm):
    class Meta:
        model = Guest_reviews
        fields = ('body', )


class BaseBookingForm(forms.ModelForm):
    checking_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'min': datetime.now().date}), initial=date.today())
    checkout_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'min': datetime.now().date}), initial=date.today())

    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    people_count = forms.ChoiceField(label='Adults',
        choices=[(i, str(i)) for i in range(1, 10)],
        widget=forms.Select(attrs={'class': 'form-select'}))
    children_count = forms.ChoiceField(label='Children',
        choices=[(i, str(i)) for i in range(0, 10)],
        widget=forms.Select(attrs={'class': 'form-select'}))
    children_ages = forms.CharField(
    label='Ages of Children (comma-separated)',
    widget=forms.TextInput(attrs={'class': 'form-control'}),
    initial='0')
    child_bed = forms.BooleanField(
        label='Child Bed',
        required=False,
        widget=forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]))
    playroom_services = forms.BooleanField(
        label='Playroom Services',
        required=False,
        widget=forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]))

    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'checking_date', 'checkout_date',  'phone_number', 'email', 'people_count', 'children_count', 'children_ages', 'child_bed', 'playroom_services']


class BookingForm(BaseBookingForm):
    class Meta(BaseBookingForm.Meta):
        pass


class BookingEditForm(BaseBookingForm):
    class Meta(BaseBookingForm.Meta):
        pass
