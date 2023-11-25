from .models import Guest_reviews, Booking
from django import forms
from django.db import models
from datetime import date, datetime
from django.core.validators import (
    RegexValidator,
    EmailValidator,
    MinLengthValidator,
    MaxLengthValidator,
)
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.forms import PasswordResetForm
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.forms import DateInput
from django_flatpickr.widgets import (
    DatePickerInput,
    TimePickerInput,
    DateTimePickerInput,
)
from django_flatpickr.schemas import FlatpickrOptions


class Guest_reviewsForm(forms.ModelForm):
    class Meta:
        model = Guest_reviews
        fields = ("body",)
        labels = {
            "body": "Message",
        }
        widgets = {
            "body": forms.Textarea(attrs={"placeholder": "Type your message here..."}),
        }


class BaseBookingForm(forms.ModelForm):
    phone_number = forms.CharField(
        label="Phone Number",
        widget=forms.TextInput(attrs={"class": "form-control", "type": "tel"}),
        required=True,
        validators=[
            RegexValidator(
                regex=r"^[\d\+\-]+$",
                message="Enter a valid phone number with digits, +, or - only.",
            ),
            MinLengthValidator(
                limit_value=10,
                message="Phone number must have at least 10 digits.",
            ),
            MaxLengthValidator(
                limit_value=15,
                message="Phone number must have at most 15 digits.",
            ),
        ],
    )

    email = forms.EmailField(
        label="Email address",
        widget=forms.EmailInput(attrs={"class": "form-control"}),
        required=True,
    )

    first_name = forms.CharField(
        label="First Name",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
        validators=[
            MinLengthValidator(2, message="Enter at least 2 characters."),
            MaxLengthValidator(15, message="Enter at most 15 characters."),
            RegexValidator(
                regex=r"^[A-Za-zА-Яа-яЁё]+$",
                message="Enter a valid first name without numbers, symbols, or spaces.",
            ),
        ],
    )

    last_name = forms.CharField(
        label="Last Name",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
        validators=[
            MinLengthValidator(2, message="Enter at least 2 characters."),
            MaxLengthValidator(15, message="Enter at most 15 characters."),
            RegexValidator(
                regex=r"^[A-Za-zА-Яа-яЁё]+$",
                message="Enter a valid last name without numbers, symbols, or spaces.",
            ),
        ],
    )

    people_count = forms.ChoiceField(
        label="Adults",
        choices=[(i, str(i)) for i in range(1, 10)],
        widget=forms.Select(attrs={"class": "form-select"}),
        required=True,
    )

    children_count = forms.ChoiceField(
        label="Children",
        choices=[(i, str(i)) for i in range(0, 4)],
        widget=forms.Select(attrs={"class": "form-select"}),
        required=True,
    )

    def validate_children_ages(value):
        ages = [int(age.strip()) for age in value.split(",") if age.strip().isdigit()]
        for age in ages:
            if age < 0 or age > 99:
                raise forms.ValidationError("Enter valid ages between 1 and 99.")

    children_ages = forms.CharField(
        label="Ages of Children (comma-separated)",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        initial="0",
        validators=[
            RegexValidator(
                regex=r"^\d+(,\s*\d+)*$",
                message="Enter valid ages separated by commas.",
            ),
            validate_children_ages,
        ],
        required=True,
    )

    child_bed = forms.BooleanField(
        label="Child Bed (complimentary)",
        required=False,
        widget=forms.RadioSelect(choices=[(True, "Yes"), (False, "No")]),
    )

    playroom_services = forms.BooleanField(
        label="Playroom Services (complimentary)",
        required=False,
        widget=forms.RadioSelect(choices=[(True, "Yes"), (False, "No")]),
    )

    def clean(self):
        cleaned_data = super().clean()
        children_count = cleaned_data.get("children_count")
        children_ages = cleaned_data.get("children_ages")

        if int(children_count) == 0 and int(children_ages) == 0:
            return cleaned_data

        if (
            children_count
            and int(children_count) > 0
            and not any(age.strip() for age in str(children_ages).split(","))
        ):
            raise ValidationError("Please enter at least one age for the children.")

        if any(age.strip() for age in str(children_ages).split(",")) and (
            not children_count or int(children_count) <= 0
        ):
            raise ValidationError("Please enter a valid number of children.")

        if children_count and int(children_count) > 0:
            ages = [
                int(age.strip())
                for age in str(children_ages).split(",")
                if age.strip().isdigit()
            ]
            if not all(age > 0 for age in ages):
                raise ValidationError("Please enter valid ages for the children.")

        room = self.room
        existing_bookings = Booking.objects.filter(
            Q(room=room),
            Q(Q(checkout_date__gt=checking_date) & Q(checking_date__lt=checkout_date))
            | Q(
                Q(checking_date__lt=checkout_date) & Q(checkout_date__gt=checking_date)
            ),
        )

        return cleaned_data

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        self.room = kwargs.pop("room", None)
        super(BaseBookingForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Booking
        fields = [
            "first_name",
            "last_name",
            "checking_date",
            "checkout_date",
            "phone_number",
            "email",
            "people_count",
            "children_count",
            "children_ages",
            "child_bed",
            "playroom_services",
        ]

        widgets = {
            "checking_date": forms.TextInput(attrs={"autocomplete": "off"}),
            "checking_date": forms.TextInput(attrs={"autocomplete": "off"}),
        }


class BookingForm(BaseBookingForm):
    class Meta(BaseBookingForm.Meta):
        pass

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)

        room = self.room
        if room:
            capacity = room.capacity
            self.fields["people_count"].choices = [
                (i, str(i)) for i in range(1, capacity + 1)
            ]

    def clean(self):
        cleaned_data = super().clean()
        checking_date = cleaned_data.get("checking_date")
        checkout_date = cleaned_data.get("checkout_date")

        if checking_date and checkout_date:
            if checking_date >= checkout_date:
                raise ValidationError(
                    "Check-out date must be later than check-in date."
                )

            room = self.room
            existing_bookings = Booking.objects.filter(
                Q(room=room),
                Q(
                    Q(checkout_date__gt=checking_date)
                    & Q(checking_date__lt=checkout_date)
                )
                | Q(
                    Q(checking_date__lt=checkout_date)
                    & Q(checkout_date__gt=checking_date)
                ),
            )

            if existing_bookings.filter(Q(is_cancelled=False)).exists():
                raise ValidationError(
                    "The selected dates overlap with an existing booking for this room."
                )

        return cleaned_data


class BookingEditForm(BaseBookingForm):
    class Meta(BaseBookingForm.Meta):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if "instance" in kwargs:
            booking = kwargs["instance"]
            self.fields["checking_date"].initial = booking.checking_date.strftime(
                "%m/%d/%Y"
            )
            self.fields["checkout_date"].initial = booking.checkout_date.strftime(
                "%m/%d/%Y"
            )

    def clean(self):
        cleaned_data = super().clean()
        checking_date = cleaned_data.get("checking_date")
        checkout_date = cleaned_data.get("checkout_date")

        if checking_date and checkout_date:
            if checking_date >= checkout_date:
                raise ValidationError(
                    "Check-out date must be later than check-in date."
                )

            room = self.room
            existing_bookings = Booking.objects.filter(
                Q(room=room),
                Q(
                    Q(checkout_date__gt=checking_date)
                    & Q(checking_date__lt=checkout_date)
                )
                | Q(
                    Q(checking_date__lt=checkout_date)
                    & Q(checkout_date__gt=checking_date)
                ),
            )

            if self.instance:
                existing_bookings = existing_bookings.exclude(id=self.instance.id)

            if existing_bookings.filter(Q(is_cancelled=False)).exists():
                raise ValidationError(
                    "The selected dates overlap with an existing booking for this room."
                )

        return cleaned_data
