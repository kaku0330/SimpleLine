# from django.shortcuts import render
from testDrfApp.models import testDrf
from testDrfApp.serializers import testDrfAppSerializer

from rest_framework import viewsets
# Create your views here.

class testDrfViewSet(viewsets.ModelViewSet):
    queryset = testDrf.objects.all()
    serializer_class = testDrfAppSerializer
