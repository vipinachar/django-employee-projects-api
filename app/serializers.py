from dataclasses import field
from rest_framework import serializers 
from app.models import employee 

class employee_serializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = employee