import random

from rest_framework import viewsets
from django.db.models import QuerySet

from rest_framework.views import APIView
from django.http import JsonResponse
from django.urls import path

from restaurants.models import Restaurant
from menu.models import DishCategory, Dish
from api.serializers import (
    RestaurantSerializer, DishCategorySerializer,
    DishSerializer
)



class RestaurantView(viewsets.ReadOnlyModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()


class DishCategoryView(viewsets.ReadOnlyModelViewSet):
    serializer_class = DishCategorySerializer
    queryset = DishCategory.objects.all()


class DishView(viewsets.ReadOnlyModelViewSet):
    serializer_class = DishSerializer

    def get_queryset(self) -> QuerySet:
        category_name = self.request.GET.get('category')
        if category_name:
            return Dish.objects.filter(category__name=category_name)

        return Dish.objects.all()


class OrderCreateView(APIView):
    def post(self, request, *args, **kwargs) -> JsonResponse:
        data = request.data.copy()
        data['id'] = random.randint(0, 1500)
        return JsonResponse(data=data, status=201)