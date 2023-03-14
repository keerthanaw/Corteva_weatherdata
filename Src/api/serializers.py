from rest_framework import serializers
from .models import Weather

#Define a serializer class for the Weather model
class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'
