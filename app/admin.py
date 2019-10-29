from django.contrib import admin
from .models import Assistant
from .models import Speaker
from .models import Config
from .models import Pass
from .admin_actions import download_csv
from .admin_actions import emails_as_txt
from .admin_actions import attendance_certificates
from .admin_actions import course_giving_certificates


class SpeakerAdmin(admin.ModelAdmin):
    search_fields = ["assistant__name",
                     "assistant__email",
                     "assistant__workplace",
                     "talk_title"]
    actions = [download_csv, course_giving_certificates]

admin.site.register(Speaker, SpeakerAdmin)


class AssistantAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "workplace")
    search_fields = ["name", "email", "workplace"]
    actions = [emails_as_txt, download_csv, attendance_certificates]

admin.site.register(Assistant, AssistantAdmin)


class ConfigAdmin(admin.ModelAdmin):
    list_display = ("key", "value", "field_type")
    search_fields = ["key", "value", "field_type"]

admin.site.register(Config, ConfigAdmin)


class PassAdmin(admin.ModelAdmin):
    pass

admin.site.register(Pass, PassAdmin)
