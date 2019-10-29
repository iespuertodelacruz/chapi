from django.core.files.base import ContentFile
from django.http import HttpResponse
import djqscsv
from reports.core import PdfReport
from .models import Config


def emails_as_txt(modeladmin, request, queryset):
    emails = ",".join(queryset.values_list("email", flat=True))
    file = ContentFile(emails)
    response = HttpResponse(file, "text/plain")
    response["Content-Length"] = file.size
    response["Content-Disposition"] = "attachment; filename=emails_chapi.txt"
    return response
emails_as_txt.short_description = "Descargar emails como TXT"


def download_csv(modeladmin, request, queryset):
    qs = queryset.all()
    return djqscsv.render_to_csv_response(qs)
download_csv.short_description = "Exportar como CSV"


def attendance_certificates(modeladmin, request, queryset):
    report = PdfReport("attendance/attendance.tmpl")
    report.render(attendants=queryset.all(),
                  config=Config)
    return report.http_response()
attendance_certificates.short_description =\
    "Generar certificados de asistencia"


def course_giving_certificates(modeladmin, request, queryset):
    report = PdfReport("course_giving/course_giving.tmpl")
    report.render(speakers=queryset.all(),
                  config=Config)
    return report.http_response()
course_giving_certificates.short_description =\
    "Generar certificados de impartir charla/taller"
