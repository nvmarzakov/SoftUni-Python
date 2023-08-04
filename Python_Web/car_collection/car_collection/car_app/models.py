from django.core import validators
from django.db import models

# Create your models here.
class Car(models.Model):
    TYPE_LENGTH = 10
    MODEL_MAX_LENGTH = 20
    MODEL_MIN_LENGTH = 2
    MIN_PRICE = 1
    CHOICES = (
        ("Sports Car", "Sports Car"),
        ("Pickup", "Pickup"),
        ("Crossover", "Crossover"),
        ("Minibus", "Minibus"),
        ("Other", "Other"),
    )

    type = models.CharField(
        max_length=TYPE_LENGTH,
        choices=CHOICES,
        blank=False,
        null=False,
    )

    model = models.CharField(
        max_length=MODEL_MAX_LENGTH,
        validators=[validators.MinLengthValidator(MODEL_MIN_LENGTH)],
        blank=False,
        null=False,
    )

    year = models.IntegerField(
        validators=(
            validators.MinValueValidator(1980, "Year must be between 1980 and 2049"),
            validators.MaxValueValidator(2049, "Year must be between 1980 and 2049"),
        ),
    )

    image_url = models.URLField(
        blank=False,
        null=False,
    )

    price = models.FloatField(
        blank=False,
        null=False,
        validators=[validators.MinValueValidator(MIN_PRICE)],
    )

