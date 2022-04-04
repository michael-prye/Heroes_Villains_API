import imp
from rest_framework import serializers
from .models import SuperType

class SuperTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperType
        fields = ['id', 'type']