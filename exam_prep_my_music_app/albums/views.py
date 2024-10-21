from django.shortcuts import render
from django.template.base import kwarg_re
from django.views.generic import CreateView
from exam_prep_my_music_app.albums.models import Album
from exam_prep_my_music_app.web.views import get_profile


# Create your views here.

class CreateAlbumView(CreateView):
    queryset = Album.objects.all()
    fields = ('name', 'artist_name', 'genre', 'description', 'image_url', 'price')
    template_name = "albums/album-add.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        kwargs["data"] = {
            **kwargs["data"],
            "profile": get_profile()
        }
        return kwargs

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        # Can be moved to mixin
        form.fields["name"].widget.attrs["placeholder"] = "Album Name"
        form.fields["artist_name"].widget.attrs["placeholder"] = "Artist"
        form.fields["description"].widget.attrs["placeholder"] = "Description"
        form.fields["image_url"].widget.attrs["placeholder"] = "Image URL"
        form.fields["price"].widget.attrs["placeholder"] = "Price"


        return form

