# coding: utf-8

from django import forms
from django.core.exceptions import ValidationError
from .models import Assistant
from .models import SHIRT_SIZES
from .models import Pass


def validate_email(value):
    if Assistant.objects.filter(email=value):
        raise ValidationError(
            "Ya existe un usuario registrado con este email.")


class RegisterForm(forms.Form):
    email = forms.EmailField(label="Email", validators=[validate_email])
    name = forms.CharField(label="Nombre y apellidos", max_length=128)
    workplace = forms.CharField(label="Lugar de trabajo", max_length=256)
    shirt_size = forms.ChoiceField(label="Talla de camisa",
                                   choices=SHIRT_SIZES,
                                   help_text="Si tenemos presupuesto, \
haremos camisetas para todos los asistentes.")
    girl_shirt = forms.BooleanField(label="¿Camisa de chica?", required=False)
    is_speaker = forms.BooleanField(label="¿Eres ponente?", required=False)


class SpeakerRegisterForm(forms.Form):
    avatar = forms.ImageField(label="Foto de perfil", required=False)
    bio = forms.CharField(label="Cuéntamos algo de ti",
                          widget=forms.Textarea)
    talk_title = forms.CharField(label="Título de la charla")
    talk_abstract = forms.CharField(label="Resumen de la charla",
                                    widget=forms.Textarea)
    talk_duration = forms.IntegerField(label="Tiempo estimado (minutos)",
                                       min_value=10,
                                       max_value=120,
                                       help_text="Mínimo 10 minutos. \
Máximo 120 minutos.")
    talk_is_workshop = forms.BooleanField(label="¿Es un taller?",
                                          required=False)


def validate_passcode(value):
    if not Pass.objects.filter(code=value):
        raise ValidationError(
            "El código introducido no es válido.")


class PassForm(forms.Form):
    passcode = forms.CharField(label="Código", validators=[validate_passcode])
