from datetime import datetime

from django.core import validators
from django.core.exceptions import ValidationError

from django.db import models
from django.utils import timezone


def validate_date_not_in_past(value):
    if value < timezone.now().date():
        raise ValidationError("The date cannot be in the past!")


# Create your models here.
class EventModel(models.Model):
    CATEGORY_CHOICES = [
        ('Sports', 'Sports'),
        ('Festivals', 'Festivals'),
        ('Conferences', 'Conferences'),
        ('Performing Art', 'Performing Art'),
        ('Concerts', 'Concerts'),
        ('Theme Party', 'Theme Party'),
        ('Other', 'Other'),
    ]

    EVENT_MIN_LENGTH = 2
    EVENT_MAX_LENGTH = 20

    event_name = models.CharField(
        validators=(
            validators.MinLengthValidator(EVENT_MIN_LENGTH),
            validators.MaxLengthValidator(EVENT_MAX_LENGTH),
        ),
        blank=False,
        null=False,
    )

    category = models.CharField(
        choices=CATEGORY_CHOICES,
        blank=False,
        null=False,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    date = models.DateField(
        validators=(
            validate_date_not_in_past,
        ),
        blank=False,
        null=False,
    )

    event_image = models.URLField(
        blank=False,
        null=False,
    )
