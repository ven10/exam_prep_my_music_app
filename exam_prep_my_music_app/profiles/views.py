from django.shortcuts import render
from django.views import generic as views

from exam_prep_my_music_app.profiles.models import Profile
from exam_prep_my_music_app.web.views import get_profile


class DetailProfileView(views.DetailView):
    queryset = Profile.objects.all()
    template_name = "profiles/profile-details.html"
    fields = "__all__"

    # TODO extract to different module
    def get_profile():
        return Profile.objects.first()

    def get_object(self, queryset=None):
        return get_profile()


class DeleteProfileView(views.DeleteView):
    pass
