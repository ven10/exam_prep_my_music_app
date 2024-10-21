from django.urls import path
from exam_prep_my_music_app.albums.views import CreateAlbumView

urlpatterns = (
    path("add/", CreateAlbumView.as_view(), name="create_album"),

)