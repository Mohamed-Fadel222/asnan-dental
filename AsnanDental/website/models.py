from django.db import models

# Create your models here.


class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)



