from rest_framework import serializers
from .models import Regalos

class RegalosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regalos
        fields = '__all__'
