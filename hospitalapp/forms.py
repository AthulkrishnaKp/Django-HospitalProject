from msilib.schema import MsiDigitalCertificate
from django import forms



from hospitalapp.models import Booking

class DateInput(forms.DateInput):
    input_type='date'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields= '__all__'  

        widgets = {
            'booking_date':DateInput(),
        }  

        labels = {
           'patient_name':'Patient Name',
           'patient_phone':'Phone Number',
           'patient_mail':'Email',           
           'doc_name':'Doctor Name',
           'booking_date':'Booking Date',
        }
