from django.db import models

class Room(models.Model):

    #ROOM_STATUS = ('Occupied','Available')

    roomType = models.CharField(max_length=20)
    bedType = models.CharField(max_length=20)
    rate = models.DecimalField(decimal_places=2,max_digits=8)
    roomStatus = models.CharField(max_length=20)
    notes = models.CharField(max_length=80)

    

