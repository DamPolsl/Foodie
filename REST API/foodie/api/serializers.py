from rest_framework import serializers

from restaurants.models import Restaurant
from menu.models import DishCategory, Dish


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'country_name', 'state_name',
            'city', 'address', 'code'
        )
        model = Restaurant

    country_name = serializers.CharField(source='country.name')
    state_name = serializers.CharField(source='state.name')


class DishCategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("name", )
        model = DishCategory


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name', 'category_name', 'price',
            'image'
        )
        model = Dish

    category_name = serializers.CharField(source='category.name')
