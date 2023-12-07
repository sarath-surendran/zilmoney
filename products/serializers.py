from rest_framework import serializers
from .models import Products, Purchase


class Itemviewserializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'