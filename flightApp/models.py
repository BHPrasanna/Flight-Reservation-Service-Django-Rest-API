from django.db import models

# Create your models here.
class Flight(models.Model):
    flightNumber=models.CharField(max_length=10)
    operatingAirlines=models.CharField(max_length=20)
    departingCity=models.CharField(max_length=20)
    arrivingCity=models.CharField(max_length=20)
    dateOfDeparture=models.DateField()
    departingTime=models.TimeField()
class Passenger(models.Model):
    firstName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    middleName=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    mobile=models.CharField(max_length=10)
class Reservation(models.Model):
    flight=models.ForeignKey(Flight,on_delete=models.CASCADE)
    passenger=models.OneToOneField(Passenger,on_delete=models.CASCADE)