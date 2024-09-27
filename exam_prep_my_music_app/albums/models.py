from enum import unique

from django.core.validators import MinValueValidator
from django.db import models

from profiles.models import Profile

"""
    • Album
        ◦ Album Name
            ▪ Character field, required.
            ▪ All album names must be unique.
            ▪  It should consist of a maximum of 30 characters.
        ◦ Artist
            ▪ Character field, required.
            ▪ It should consist of a maximum of 30 characters.
        ◦ Genre
            ▪ Character field, required.
            ▪ It should consist of a maximum of 30 characters.
            ▪ The choices are "Pop Music", "Jazz Music", "R&B Music", "Rock Music", "Country Music", "Dance Music", "Hip Hop Music", and "Other".
        ◦ Description
            ▪ Text field, optional.
        ◦ Image URL
            ▪ URL field, required.
        ◦ Price
            ▪ Float field, required.
            ▪ The price cannot be below 0.0.
        ◦ Owner
            ▪ A foreign key to the Profile model.
            ▪ Establishes a many-to-one relationship with the Profile model, associating each album with a profile.
            ▪ The ON DELETE constraint must be configured to an appropriate value in alignment with the specified additional tasks.
            ▪ This field should remain hidden in forms.


"""

class Album(models.Model):
    MAX_NAME_LENGTH = 30
    MAX_ARTIST_NAME_LENGTH = 30
    MIN_PRICE = 0.0

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        unique=True,
        null=False,
        blank=False,
    )

    artist_name = models.CharField(
        max_length=MAX_ARTIST_NAME_LENGTH,
        null=False,
        blank=False,
    )

    genre = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        choices=[
            ('Pop Music', 'Pop Music'),
            ('Jazz Music', 'Jazz Music'),
            ('R & B Music', 'R & B Music'),
            ('Rock Music', 'Rock Music'),
            ('Country Music', 'Country Music'),
            ('Dance Music', 'Dance Music'),
            ('Hip Hop Music', 'Hip Hop Music'),
            ('Other', 'Other'),
        ]
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(MIN_PRICE)
        ]
    )

    owner = models.ForeignKey(
        to=Profile,
        #TODO check owner foreign key
        on_delete=models.DO_NOTHING,
    )