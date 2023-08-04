from django.core import validators
from django.db import models


# Create your models here.
class Profile(models.Model):
    MAX_LENGTH_USERNAME = 10
    MIN_LENGTH_USERNAME = 2
    MIN_AGE = 18
    PASSWORD_MAX_CHARACTERS = 30
    NAME_LENGTH = 30

    username = models.CharField(
        max_length=MAX_LENGTH_USERNAME,
        validators=[validators.MinLengthValidator(MIN_LENGTH_USERNAME, "The username must be a minimum of 2 chars")],
        blank=False,
        null=False,
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.PositiveIntegerField(
        blank=False,
        null=False,
        validators=[validators.MinValueValidator(MIN_AGE)],
    )

    password = models.CharField(
        max_length=PASSWORD_MAX_CHARACTERS,
        blank=False,
        null=False,
    )

    first_name = models.CharField(
        max_length=NAME_LENGTH,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=NAME_LENGTH,
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )

    def get_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        else:
            return ''