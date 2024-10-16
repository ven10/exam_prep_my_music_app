from django.contrib import admin

from albums.models import Album
from profiles.models import Profile


# Register your models here.

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass