from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from app.models import Customer,Room,Occupation,Payment,Employee

class customerSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        
class employeeSerializer(FlexFieldsModelSerializer):    
    class Meta:
        model = Employee
        fields = '__all__'

class roomSerializer(FlexFieldsModelSerializer):    
    class Meta:
        model = Room
        fields = '__all__'

class occupationSerializer(FlexFieldsModelSerializer):    
    class Meta:
        model = Occupation
        fields = '__all__'

    expandable_fields = {
        'employee': (employeeSerializer, {'source': 'employee'}),
        'room': (roomSerializer, {'source': 'room'}),
        'customer': (customerSerializer, {'source': 'customer'}),
    }

class paymentSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

    expandable_fields = {
        'occupation' : (occupationSerializer, {'source': 'occupation'}),
        'employee' : (employeeSerializer, {'source': 'employee'})
      }