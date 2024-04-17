from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['booking_area', 'hospital_name', 'booking_date', 'booking_time']

# class CreateList(forms.Form):
#     name = forms.CharField(label="name", max_length=100)
#     check = forms.BooleanField(required=False)