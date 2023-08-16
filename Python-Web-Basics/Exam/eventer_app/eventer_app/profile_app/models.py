from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


def validate_letters(value):
    from django.core import exceptions

    for ch in value:
        if not ch.isalnum():
            raise ValidationError("The name should contain only letters!")


def validate_password(value):
    if not any(char.isdigit() for char in value):
        raise ValidationError("The password must contain at least 1 digit.")


# Create your models here.
class ProfileModel(models.Model):
    FIRST_NAME_MAX_LENGTH = 20
    LAST_NAME_MIN_LENGTH = 4
    LAST_NAME_MAX_LENGTH = 30
    EMAIL_MAX_CHAR = 45
    PASSWORD_MIN_CHAR = 5
    PASSWORD_MAX_CHAR = 20

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=[validate_letters],
        blank=False,
        null=False,
    )

    last_name = models.CharField(
        validators=(
            validators.MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validators.MaxLengthValidator(LAST_NAME_MAX_LENGTH),
        ),
        blank=False,
        null=False,
    )

    email = models.EmailField(
        max_length=EMAIL_MAX_CHAR,
        blank=False,
        null=False,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )

    password = models.CharField(
        validators=(
            validators.MinLengthValidator(PASSWORD_MIN_CHAR),
            validators.MaxLengthValidator(PASSWORD_MAX_CHAR),
            validate_password,
        )
    )
