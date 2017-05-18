from django.shortcuts import render
from rest_framework import generics
from app.serializers import serializers
from rest_flex_fields import FlexFieldsModelViewSet
from rest_framework import viewsets
from app.models import Customer,Room,Occupation,Payment,Employee

# Create your views here.

class customerViewSet(FlexFieldsModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = serializers.customerSerializer

class roomViewSet(FlexFieldsModelViewSet):
    queryset = Room.objects.all()
    serializer_class = serializers.roomSerializer

class occupationViewSet(FlexFieldsModelViewSet):
    permit_list_expands = ['employee','customer','room']
    queryset = Occupation.objects.all()
    serializer_class = serializers.occupationSerializer

class employeeViewSet(FlexFieldsModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = serializers.employeeSerializer

class paymentViewSet(FlexFieldsModelViewSet):
    permit_list_expands = ['employee','occupation','occupation.customer','occupation.room','occupation.employee']
    queryset = Payment.objects.all()
    serializer_class = serializers.paymentSerializer