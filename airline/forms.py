from decimal import Decimal
from django import forms
from .models import Airport, Customer


class BookingDeleteForm(forms.Form):
    customer_code = forms.IntegerField(label="Customer Code", required=True)
    booking_id = forms.IntegerField(label="Booking ID", required=True)


class BookingForm(forms.Form):
    customer_code = forms.IntegerField(label="Customer Code", required=False)
    title = forms.ChoiceField(choices=Customer.TITLE_CHOICES, required=False)
    first_name = forms.CharField(label="First Name", max_length=50, required=False)
    last_name = forms.CharField(label="Last Name", max_length=50, required=False)
    gender = forms.ChoiceField(choices=Customer.GENDER_CHOICES, required=False)
    email = forms.CharField(max_length=255, required=False)


class SearchForm(forms.Form):
    depart_loc = forms.ModelChoiceField(
        queryset=Airport.objects.all(), label="Departing Location", required=False
    )

    depart_date_range_start = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}),
        label="Date Range Start",
        required=False,
    )

    depart_date_range_end = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}),
        label="Date Range End",
        required=False,
    )

    arrive_loc = forms.ModelChoiceField(
        queryset=Airport.objects.all(), label="Arrival Location", required=False
    )

    arrive_date_range_start = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}),
        label="Date Range Start",
        required=False,
    )

    arrive_date_range_end = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}),
        label="Date Range End",
        required=False,
    )

    min_price = forms.DecimalField(
        decimal_places=2, label="Minimum Price", required=False, initial=Decimal("0.00")
    )
    max_price = forms.DecimalField(
        decimal_places=2, label="Maximum Price", required=False, initial=Decimal("0.00")
    )
    seats_required = forms.IntegerField(
        label="Seats Required", initial=1, required=False
    )
