from django.db import models

class Person(models.Model):

    firstName = models.CharField(max_length=30)
    lastName = 	models.CharField(max_length=30)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    phoneNumber = models.CharField(max_length=30)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)

    class Meta:
        abstract = True