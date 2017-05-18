"""HotelApplicationAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from app import views


# Create a router and register our viewsets with it.
router = DefaultRouter()
#router.register(r'customers',views.customerList)
router.register(r'customers',views.customerViewSet)
router.register(r'rooms',views.roomViewSet)
router.register(r'occupations',views.occupationViewSet)
router.register(r'employees',views.employeeViewSet)
router.register(r'payments',views.paymentViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^rest-auth/', include('rest_auth.urls'))
]