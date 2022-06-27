from rest_framework.routers import DefaultRouter
from api import views

from django.urls import path


router = DefaultRouter()

router.register(
    'resturants', views.RestaurantView,
    basename="restaurants"
)

router.register(
    'dish-categories', views.DishCategoryView,
    basename="dishcategories"
)

router.register(
    'dishes', views.DishView,
    basename="dishes"
)

urlpatterns = [
    path("order-create/", views.OrderCreateView.as_view(), name="order_create")
] + router.urls
