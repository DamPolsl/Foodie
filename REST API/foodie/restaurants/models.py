from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class BaseContactModel(models.Model):
    class Meta:
        abstract = True

    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)

    city = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        # chosen state must be in chosen country
        if self.state:
            assert self.state.country.id == self.country.id
        return super().save(force_insert, force_update, using, update_fields)


class Restaurant(BaseContactModel):
    code = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.city} - {self.code}"



