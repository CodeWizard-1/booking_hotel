from .models import Booking
from .models import Guest_reviews, Booking
from django import forms
from django.db import models
from datetime import date, datetime
from django.core.validators import RegexValidator, EmailValidator,  MinLengthValidator, MaxLengthValidator
from phonenumber_field.formfields import PhoneNumberField


class Guest_reviewsForm(forms.ModelForm):
    class Meta:
        model = Guest_reviews
        fields = ('body', )


class BaseBookingForm(forms.ModelForm):
    checking_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'min': datetime.now().date, 'id': 'id_check_in_date'}),  initial=date.today())
    checkout_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'min': datetime.now().date, 'id': 'id_check_out_date'}), initial=date.today())

    phone_number = forms.CharField(
        label='Phone Number',
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'tel'}),
        required=True,
        validators=[
            RegexValidator(
                regex=r'^[\d\+\-]+$',
                message='Enter a valid phone number with digits, +, or - only.',
            ),
            MinLengthValidator(
                limit_value=10,
                message='Phone number must have at least 10 digits.',
            ),
            MaxLengthValidator(
                limit_value=15,
                message='Phone number must have at most 15 digits.',
            ),
        ],
    )

    email = forms.EmailField(label='Email address', widget=forms.EmailInput(attrs={'class': 'form-control'}), required=True)

    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form-control'}), 
    required=True,
    validators=[MinLengthValidator(2, message='Enter at least 2 characters.'), MaxLengthValidator(15, message='Enter at most 15 characters.'),
    RegexValidator(
                regex=r'^[A-Za-zА-Яа-яЁё]+$',
                message='Enter a valid first name without numbers, symbols, or spaces.',
            ),]
    )


    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control'}), 
    required=True,
    validators=[MinLengthValidator(2, message='Enter at least 2 characters.'), MaxLengthValidator(15, message='Enter at most 15 characters.'),
    RegexValidator(
                regex=r'^[A-Za-zА-Яа-яЁё]+$',
                message='Enter a valid last first name without numbers, symbols, or spaces.',
            ),
    ]
    )

    people_count = forms.ChoiceField(label='Adults',
        choices=[(i, str(i)) for i in range(1, 10)],
        widget=forms.Select(attrs={'class': 'form-select'}), required=True)

    children_count = forms.ChoiceField(label='Children',
        choices=[(i, str(i)) for i in range(0, 10)],
        widget=forms.Select(attrs={'class': 'form-select'}), required=True)

    children_ages = forms.CharField(
    label='Ages of Children (comma-separated)',
    widget=forms.TextInput(attrs={'class': 'form-control'}),
    initial='0',
    validators=[RegexValidator(regex=r'^\d+(,\s*\d+)*$', message='Enter valid ages separated by commas.')], required=True)
    

    child_bed = forms.BooleanField(
        label='Child Bed (complimentary)',
        required=False,
        widget=forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]))

    playroom_services = forms.BooleanField(
        label='Playroom Services (complimentary)',
        required=False,
        widget=forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]))


    def clean(self):
        cleaned_data = super().clean()
        checking_date = cleaned_data.get('checking_date')
        checkout_date = cleaned_data.get('checkout_date')

        if checking_date and checkout_date and checkout_date < checking_date:
            self.add_error('checkout_date', 'Checkout date must be later than checking date.')


    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'checking_date', 'checkout_date',  'phone_number', 'email', 'people_count', 'children_count', 'children_ages', 'child_bed', 'playroom_services']



class BookingForm(BaseBookingForm):
    class Meta(BaseBookingForm.Meta):
        pass


class BookingEditForm(BaseBookingForm):
    class Meta(BaseBookingForm.Meta):
        pass
