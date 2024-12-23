from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.

class Buyer(models.Model):
    name = models.CharField(max_length=255)
    balance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    age = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=255)
    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    size = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title
