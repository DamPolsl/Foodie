from django.db import models


class DishCategory(models.Model):
    name = models.CharField(max_length=255)
    # NOTE - should there be anything else here?

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=255)
    # there is a possibility for a dish to be in multiple categories
    # This may be changed
    category = models.ForeignKey(DishCategory, on_delete=models.CASCADE)
    price = models.FloatField()

    image = models.ImageField(upload_to='dishes/')

    def __str__(self):
        return self.name
