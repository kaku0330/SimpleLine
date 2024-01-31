from django.shortcuts import render
from rest_framework import viewsets
from .serializer import CreateUsersModelSerializers
from .models import users
# Create your views here.

class UsersViewSet(viewsets.ModelViewSet):
    queryset = users.objects.all()
    base_serializer_class = CreateUsersModelSerializers()