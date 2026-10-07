from django import forms
from .models import Seat


class SeatBookingForm(forms.Form):
    seat = forms.ModelChoiceField(
        queryset=Seat.objects.filter(
            booking_status=False
        ),
        empty_label="Select Seat"
    )