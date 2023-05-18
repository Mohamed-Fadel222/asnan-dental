from django.shortcuts import render, redirect
from .models import Contact, Appointment
from .forms import AppointmentForm, ContactForm
# Create your views here.
def index(request):
    return render(request, 'index.html')


def contact(request):
    if request.POST:
        dataform = ContactForm(request.POST)
        if dataform.is_valid():
            dataform.save()
        return redirect(contact)
    # name = request.POST['message-name']
    return render(request, 'contact.html', {'dataform': ContactForm})