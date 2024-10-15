from rest_framework import serializers

from cars.models import Car, CarComments


class CarSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Car
        fields = '__all__'


class CarCommentsSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = CarComments
        fields = '__all__'
