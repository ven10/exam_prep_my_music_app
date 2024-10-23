from django.shortcuts import render
from django.template.base import kwarg_re
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from exam_prep_my_music_app.albums.models import Album
from exam_prep_my_music_app.web.views import get_profile


# Create your views here.

class CreateAlbumView(CreateView):
    queryset = Album.objects.all()
    fields = ('name', 'artist_name', 'genre', 'description', 'image_url', 'price')
    template_name = "albums/album-add.html"
    success_url = reverse_lazy("index")


    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        # Can be moved to mixin
        form.fields["name"].widget.attrs["placeholder"] = "Album Name"
        form.fields["artist_name"].widget.attrs["placeholder"] = "Artist"
        form.fields["description"].widget.attrs["placeholder"] = "Description"
        form.fields["image_url"].widget.attrs["placeholder"] = "Image URL"
        form.fields["price"].widget.attrs["placeholder"] = "Price"

        return form

    # TODO: Check for better solution.Working OK
    def form_valid(self, form):
        # instance = form.save(commit=False)
        # instance.owner = get_profile()
        form.instance.owner_id = get_profile().pk

        return super().form_valid(form)


class DetailAlbumView(DetailView):
    queryset = Album.objects.all()
    template_name = "albums/album-details.html"
