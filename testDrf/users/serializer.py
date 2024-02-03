from rest_framework import serializers
from .models import user

# class CreateUsersSerializers(serializers.Serializer):
#     user = serializers.CharField()
#     password = serializers.CharField()

class CreateUsersModelSerializers(serializers.ModelSerializer):
    class Meta:
        model=user
        fields = ('username','password')

    # def create(self,POSTdata):

    #     create_user = user(
    #         username=POSTdata['username'],
    #         password=POSTdata['password']
    #     )

    #     create_user.save()

    #     return create_user