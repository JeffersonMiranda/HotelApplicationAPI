from django.db import models
from app.models.room import Room
from app.models.customer import Customer
from app.models.employee import Employee

class Occupation(models.Model):

    employee = models.ForeignKey(Employee)
    customer = models.ForeignKey(Customer)
    room = models.ForeignKey(Room)
    entryDate = models.DateField()  # WHEN THE CUSTOMER GETS IN THE HOTEL
    exitDate = models.DateField() # WHEN THE CUSTOMER GETS OUT
    