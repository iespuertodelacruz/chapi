# coding: utf-8

from django.shortcuts import render
from .forms import RegisterForm
from .forms import SpeakerRegisterForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .models import Assistant
from .models import Speaker
from .models import get_listeners
import collections
import json
from django.conf import settings
from .models import Config
from .forms import PassForm
from .models import Pass
from .utils import access_to_register


def index(request):
    return render(request, "app/index.html")


def register(request, passcode=None):
    if not access_to_register(passcode):
        return HttpResponseRedirect(reverse("closed_register"))

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            settings.REDIS.set(email, json.dumps(form.cleaned_data))
            if form.cleaned_data["is_speaker"]:
                return HttpResponseRedirect(
                    reverse("register_speaker",
                            kwargs={
                                "assistant_email": email,
                                "passcode": passcode
                            }))
            else:
                data = json.loads(settings.REDIS.get(email))
                a = Assistant(
                    email=data["email"],
                    name=data["name"],
                    workplace=data["workplace"],
                    shirt_size=data["shirt_size"],
                    girl_shirt=data["girl_shirt"],
                )
                a.save()
                settings.REDIS.delete(email)
                if passcode:
                    Pass.objects.filter(code=passcode).delete()
                return render(request, "app/thanks.html")
    else:
        form = RegisterForm()
    context = {
        "form": form
    }
    return render(request, "app/register.html", context)


def register_speaker(request, assistant_email, passcode=None):
    if not access_to_register(passcode):
        return HttpResponseRedirect(reverse("closed_register"))

    if request.method == "POST":
        form = SpeakerRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            data = json.loads(settings.REDIS.get(assistant_email))
            a = Assistant(
                email=data["email"],
                name=data["name"],
                workplace=data["workplace"],
                shirt_size=data["shirt_size"],
                girl_shirt=data["girl_shirt"],
            )
            a.save()
            settings.REDIS.delete(assistant_email)

            t = Speaker(
                avatar=form.cleaned_data["avatar"],
                bio=form.cleaned_data["bio"],
                assistant=Assistant.objects.get(pk=a.id),
                talk_title=form.cleaned_data["talk_title"],
                talk_abstract=form.cleaned_data["talk_abstract"],
                talk_duration=form.cleaned_data["talk_duration"],
                talk_is_workshop=form.cleaned_data["talk_is_workshop"]
            )
            t.save()
            if passcode:
                Pass.objects.filter(code=passcode).delete()
            return render(request, "app/thanks.html")
    else:
        form = SpeakerRegisterForm()
    context = {
        "form": form
    }
    return render(request, "app/register_speaker.html", context)


def page_not_found(request):
    return render(request, "app/404.html")


def server_error(request):
    return render(request, "app/500.html")


def speakers(request):
    return render(request, "app/speakers.html")


def normalize_workplace(workplace):
    workplace = workplace.upper()
    workplace = workplace.replace(u"Á", "A")
    workplace = workplace.replace(u"É", "E")
    workplace = workplace.replace(u"Í", "I")
    workplace = workplace.replace(u"Ó", "O")
    workplace = workplace.replace(u"Ú", "U")
    return workplace


def listeners(request):
    listeners = get_listeners()
    workplaces = {}
    for l in listeners:
        workplace = normalize_workplace(l.workplace)
        if workplace in workplaces:
            workplaces[workplace] += 1
        else:
            workplaces[workplace] = 1
    context = {
        "workplaces": collections.OrderedDict(sorted(workplaces.items()))
    }
    return render(request, "app/listeners.html", context)


def agenda(request):
    return render(request, "app/agenda.html")


def financing(request):
    return render(request, "app/financing.html")


def rooms(request):
    return render(request, "app/rooms.html")


def closed_register(request):
    if request.method == "POST":
        form = PassForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(
                reverse("register",
                        kwargs={"passcode": form.cleaned_data["passcode"]}))
    else:
        form = PassForm()

    context = {
        "register_deadline": Config.get_value("register_deadline"),
        "form": form
    }
    return render(request, "app/closed_register.html", context)


def location(request):
    return render(request, "app/location.html")


def downloads(request):
    return render(request, "app/downloads.html")
