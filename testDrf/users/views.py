from django.shortcuts import render
from rest_framework import viewsets
from .serializer import CreateUserModelSerializers
from .models import user
# Create your views here.

class UsersViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = CreateUserModelSerializers

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return user.objects.all()
    #     if self.action == 'create':
    #         return CreateUsersModelSerializers
        