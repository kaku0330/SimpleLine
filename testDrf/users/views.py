from django.shortcuts import render
from rest_framework import viewsets
from .serializer import CreateUsersModelSerializers
from .models import user
# Create your views here.

class UsersViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = CreateUsersModelSerializers

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return user.objects.all()
    #     if self.action == 'create':
    #         return CreateUsersModelSerializers
        