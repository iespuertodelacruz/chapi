from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$",
        views.index,
        name="index"),
    url(r"^register/$",
        views.register,
        name="register"),
    url(r"^register/(?P<passcode>.*)/$",
        views.register,
        name="register"),
    url(r"^register_speaker/(?P<assistant_email>.*)/(?P<passcode>.*)/$",
        views.register_speaker,
        name="register_speaker"),
    url(r"^register_speaker/(?P<assistant_email>.*)/$",
        views.register_speaker,
        name="register_speaker"),
    url(r"^speakers/$",
        views.speakers,
        name="speakers"),
    url(r"^listeners/$",
        views.listeners,
        name="listeners"),
    url(r"^agenda/$",
        views.agenda,
        name="agenda"),
    url(r"^financing/$",
        views.financing,
        name="financing"),
    url(r"^rooms/$",
        views.rooms,
        name="rooms"),
    url(r"^closed_register/$",
        views.closed_register,
        name="closed_register"),
    url(r"^location/$",
        views.location,
        name="location"),
    url(r"^downloads/$",
        views.downloads,
        name="downloads")
]
