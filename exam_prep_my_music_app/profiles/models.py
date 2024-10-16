from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here

def validate_username(username):
    is_valid = all(ch.isalnum() or ch == "_" for ch in username)
    if not is_valid:
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")

class Profile(models.Model):
    MIN_USERNAME_LENGTH = 2
    MAX_USERNAME_LENGTH = 15


    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(MIN_USERNAME_LENGTH),
    ])

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )


