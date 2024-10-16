from django.shortcuts import render
from django.views import generic as views

from exam_prep_my_music_app.profiles.models import Profile


# Create your views here.


def get_profile():
    return Profile.objects.first()

def create_profile(request):
    return render(request, "web/home-no-profile.html")


def index(request):
    profile = get_profile()

    if profile is None:
        return create_profile(request)

    return render(request, "web/home-with-profile.html")


# class IndexView(views.TemplateView):
#     def get_template_names(self):
#         if get_profile() is None:
#             return ["web/home-no-profile.html"]
#         return ["web/home-with-profile.html"]


