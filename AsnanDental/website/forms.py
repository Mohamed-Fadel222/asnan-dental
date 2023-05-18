from django.forms import ModelForm
from django import forms
from .models import Appointment, Contact

class AppointmentForm(forms.ModelForm):
   
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
