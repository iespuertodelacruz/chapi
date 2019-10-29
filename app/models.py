# coding: utf-8

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from PIL import Image, ImageOps
from django.conf import settings
import dateparser

SHIRT_SIZES = (
    ("S", "Talla S"),
    ("M", "Talla M"),
    ("L", "Talla L"),
    ("XL", "Talla XL"),
    ("XXL", "Talla XXL"),
)


def get_listeners():
    assistants = Assistant.objects.all()
    speakers = Speaker.objects.all()
    return assistants.exclude(
        id__in=speakers.values_list("assistant", flat=True)).order_by("name")


def get_speakers():
    return Speaker.objects.all().order_by("assistant__name")


@python_2_unicode_compatible
class Assistant(models.Model):
    email = models.EmailField(unique=True,
                              verbose_name="Email")
    name = models.CharField(verbose_name="Nombre y apellidos",
                            max_length=128)
    workplace = models.CharField(verbose_name="Lugar de trabajo",
                                 max_length=256)
    shirt_size = models.CharField(verbose_name="Talla de camisa",
                                  choices=SHIRT_SIZES,
                                  default="L",
                                  max_length=8)
    girl_shirt = models.BooleanField(verbose_name="Camisa de chica")

    def __str__(self):
        return self.name.upper()

    class Meta:
        verbose_name = "Asistente"


@python_2_unicode_compatible
class Speaker(models.Model):
    assistant = models.ForeignKey(Assistant,
                                  on_delete=models.CASCADE,
                                  verbose_name="Asistente")
    avatar = models.ImageField(verbose_name="Foto de perfil",
                               null=True,
                               blank=True,
                               upload_to="uploads/")
    bio = models.TextField(verbose_name="Bio")
    talk_title = models.CharField(verbose_name="Título de la charla",
                                  max_length=128)
    talk_abstract = models.TextField(verbose_name="Resumen de la charla")
    talk_duration = models.PositiveSmallIntegerField(
        verbose_name="Tiempo estimado")
    talk_is_workshop = models.BooleanField(verbose_name="¿Es un taller?")

    def __str__(self):
        return "{} - {}".format(self.assistant.name, self.talk_title)

    def save(self):
        super(Speaker, self).save()
        if self.avatar:
            image = Image.open(self.avatar)
            image = ImageOps.fit(image,
                                 settings.AVATAR_SIZE,
                                 Image.ANTIALIAS,
                                 centering=(0.5, 0.5))
            image.save(self.avatar.path)

    class Meta:
        verbose_name = "Ponente"


@python_2_unicode_compatible
class Config(models.Model):
    INTEGER = "I"
    FLOAT = "F"
    DATE = "D"
    BOOLEAN = "B"
    STRING = "S"

    FIELD_TYPES = (
        (INTEGER, "INTEGER"),
        (FLOAT, "FLOAT"),
        (DATE, "DATE"),
        (BOOLEAN, "BOOLEAN"),
        (STRING, "STRING"),
    )

    key = models.CharField(verbose_name="Clave",
                           max_length=256)
    value = models.CharField(verbose_name="Valor",
                             max_length=512)
    field_type = models.CharField(verbose_name="Tipo",
                                  max_length=8,
                                  choices=FIELD_TYPES)

    def __str__(self):
        return "{}: {}".format(self.key, self.value)

    class Meta:
        verbose_name = "Configuración"
        verbose_name_plural = "Configuraciones"

    @classmethod
    def get_value(cls, key, as_string=False):
        try:
            obj = cls.objects.get(key=key)
            r = obj.value
            if as_string:
                return r
            else:
                ft = obj.field_type
                if ft == cls.INTEGER:
                    return int(r)
                elif ft == cls.FLOAT:
                    return float(r)
                elif ft == cls.DATE:
                    return dateparser.parse(
                        r,
                        date_formats=["%d/%m/%Y"]).date()
                elif ft == cls.BOOLEAN:
                    return bool(r)
                elif ft == cls.STRING:
                    return r
        except:
            pass
        return None


@python_2_unicode_compatible
class Pass(models.Model):
    code = models.CharField(verbose_name="Código",
                            max_length=16)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "Pase especial"
        verbose_name_plural = "Pases especiales"
