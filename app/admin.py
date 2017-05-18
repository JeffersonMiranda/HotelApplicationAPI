from django.contrib import admin
from app.models import Customer,Employee,Occupation,Room,Payment

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Customer, CustomerAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Employee, EmployeeAdmin)

class OccupationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Occupation, OccupationAdmin)

class RoomAdmin(admin.ModelAdmin):
    pass
admin.site.register(Room, RoomAdmin)

class PaymentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Payment, PaymentAdmin)


