from rest_framework import serializers
from .models import user

# class CreateUsersSerializers(serializers.Serializer):
#     user = serializers.CharField()
#     password = serializers.CharField()

class CreateUsersModelSerializers(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model=user