from django.urls import path
from django.views.generic import DetailView

from exam_prep_my_music_app.albums.views import DetailAlbumView
from exam_prep_my_music_app.albums.views import CreateAlbumView

urlpatterns = (
    path("add/", CreateAlbumView.as_view(), name="create_album"),
    path("<int:pk>/details/", DetailAlbumView.as_view(), name="details_album"),

)