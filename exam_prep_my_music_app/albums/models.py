from django.core.validators import MinValueValidator
from django.db import models

from exam_prep_my_music_app.profiles.models import Profile


class Album(models.Model):
    MAX_NAME_LENGTH = 30
    MAX_ARTIST_NAME_LENGTH = 30
    MIN_PRICE = 0.0

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        unique=True,
        null=False,
        blank=False,
        verbose_name="Album name",
    )

    artist_name = models.CharField(
        max_length=MAX_ARTIST_NAME_LENGTH,
        null=False,
        blank=False,
        verbose_name="Artist",
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
        verbose_name="Image URL",
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