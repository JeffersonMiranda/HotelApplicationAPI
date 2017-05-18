from django.db import models
from app.models.occupation import Occupation
from app.models.employee import Employee

class Payment(models.Model):

    occupation = models.ForeignKey(Occupation) # THE PAYMENT IS LINKED TO AN OCCUPATION
    employee = models.ForeignKey(Employee,blank = True, null = True)
    paymentDate = models.DateField(blank = True, null = True)
    totalDays = models.IntegerField()
    price = models.DecimalField(decimal_places=2,max_digits=8)
    notes = models.CharField(max_length=80,blank = True, null = True)
    paid = models.BooleanField(default=False)
