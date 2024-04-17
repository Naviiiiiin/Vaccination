from django.db import models
from django.contrib.auth.models import User



class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_area = models.CharField(max_length=100)
    hospital_name = models.CharField(max_length=100)
    booking_date = models.DateField()
    booking_time = models.TimeField()

class Area(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Hospitals(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text
    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    verification_code = models.CharField(max_length=6, blank=True, null=True)

   
