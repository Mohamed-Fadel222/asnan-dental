from django.shortcuts import render, redirect
from .models import Contact, Appointment
from .forms import AppointmentForm, ContactForm
# Create your views here.
def index(request):
    return render(request, 'index.html')

