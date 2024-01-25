from rest_framework import serializers
from testDrfApp.models import testDrf 

class testDrfAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = testDrf
        field = '__all__'
        # field = ('id','test_id','test_name')

        