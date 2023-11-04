from .models import Booking
from .models import Guest_reviews, Booking
from django import forms
from django.db import models


class Guest_reviewsForm(forms.ModelForm):
    class Meta:
        model = Guest_reviews
        fields = ('body', )


# class BookingForm(forms.ModelForm):
#     checking_date = forms.DateField(
#         input_formats=['%d.%m.%Y'],
#         widget=forms.TextInput(attrs={'class': 'datepicker'}))
#     checkout_date = forms.DateField(
#         input_formats=['%d.%m.%Y'],
#         widget=forms.TextInput(attrs={'class': 'datepicker'}))
#     phone_number = forms.CharField()
#     email = forms.EmailField()
#     first_name = forms.CharField(label='First Name')
#     last_name = forms.CharField(label='Last Name')
#     people_count = forms.ChoiceField(
#         choices=[(i, str(i)) for i in range(1, 11)])
#     children_count = forms.ChoiceField(
#         choices=[(i, str(i)) for i in range(0, 11)])
#     children_ages = forms.CharField(label='Ages of Children (comma-separated)')
#     child_bed = forms.BooleanField(
#         label='Child Bed',
#         required=False,
#         widget=forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]))
#     playroom_services = forms.BooleanField(
#         label='Playroom Services',
#         required=False,
#         widget=forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]))

#     class Meta:
#         model = Booking
#         fields = ['first_name', 'last_name', 'phone_number', 'checking_date', 'checkout_date', 'email',
#                   'people_count', 'children_count', 'children_ages', 'child_bed', 'playroom_services']


# class BookingEditForm(forms.ModelForm):
#     checking_date = forms.DateField(
#         input_formats=['%d.%m.%Y'],
#         widget=forms.TextInput(attrs={'class': 'datepicker'}))
#     checkout_date = forms.DateField(
#         input_formats=['%d.%m.%Y'],
#         widget=forms.TextInput(attrs={'class': 'datepicker'}))
#     phone_number = forms.CharField()
#     email = forms.EmailField()
#     first_name = forms.CharField(label='First Name')
#     last_name = forms.CharField(label='Last Name')
#     people_count = forms.ChoiceField(
#         choices=[(i, str(i)) for i in range(1, 11)])
#     children_count = forms.ChoiceField(
#         choices=[(i, str(i)) for i in range(0, 11)])
#     children_ages = forms.CharField(label='Ages of Children (comma-separated)')
#     child_bed = forms.BooleanField(
#     label='Child Bed',required=False,
#     widget=forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]))
#     playroom_services = forms.BooleanField(
#     label='Playroom Services',
#     required=False,
#     widget=forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]))

#     class Meta:
#         model = Booking
#         fields = ['first_name', 'last_name', 'phone_number', 'checking_date', 'checkout_date', 'email',
#                   'people_count', 'children_count', 'children_ages', 'child_bed', 'playroom_services']


class BaseBookingForm(forms.ModelForm):
    checking_date = forms.DateField(
        input_formats=['%d.%m.%Y'],
        widget=forms.TextInput(attrs={'class': 'datepicker'}))
    checkout_date = forms.DateField(
        input_formats=['%d.%m.%Y'],
        widget=forms.TextInput(attrs={'class': 'datepicker'}))
    phone_number = forms.CharField()
    email = forms.EmailField()
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    people_count = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(1, 11)])
    children_count = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(0, 11)])
    children_ages = forms.CharField(label='Ages of Children (comma-separated)')
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
        fields = ['first_name', 'last_name', 'phone_number', 'checking_date', 'checkout_date', 'email',
                  'people_count', 'children_count', 'children_ages', 'child_bed', 'playroom_services']


class BookingForm(BaseBookingForm):
    class Meta(BaseBookingForm.Meta):
        pass


class BookingEditForm(BaseBookingForm):
    class Meta(BaseBookingForm.Meta):
        pass
