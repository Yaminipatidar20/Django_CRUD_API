from rest_framework import serializers
from .models import *

class ElectricDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectricDevice
        fields = "__all__"
    