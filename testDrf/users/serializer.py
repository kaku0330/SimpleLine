from rest_framework import serializers
from .models import users

# class CreateUsersSerializers(serializers.Serializer):
#     user = serializers.CharField()
#     password = serializers.CharField()

class CreateUsersModelSerializers(serializers.ModelSerializer):
    class Meta:
        field="all"
        model=users