from django.contrib import admin
from restaurants.models import (
    Country, State, Restaurant
)

# Register your models here.
admin.site.register(Country)
admin.site.register(State)
admin.site.register(Restaurant)
