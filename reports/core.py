from jinja2 import Environment, FileSystemLoader
from subprocess import Popen, PIPE
import uuid
from django.http import StreamingHttpResponse
import os
import datetime


TEMPLATES_DIR = "reports/templates"
RENDERED_FILES_DIR = "/tmp/"
PDFFILES_EXTENSION = ".pdf"

ENV = Environment(loader=FileSystemLoader(TEMPLATES_DIR))


class PdfReport():
    def __init__(self, template_filepath):
        self.template = ENV.get_template(template_filepath)
        self.generation_time = datetime.datetime.now()

    def render(self, **kwargs):
        self.output_filename = RENDERED_FILES_DIR + str(uuid.uuid4()) +\
            PDFFILES_EXTENSION
        kwargs["generation_time"] = self.generation_time
        self.rendered_template = self.template.render(kwargs)
        p = Popen(["prince", "-", self.output_filename], stdin=PIPE)
        p.stdin.write(self.rendered_template.encode("utf-8"))
        p.stdin.close()
        p.communicate()

    def http_response(self):
        response = StreamingHttpResponse(open(self.output_filename))
        os.remove(self.output_filename)
        response["Content-Type"] = "application/pdf"
        user_filename = os.path.splitext(
            os.path.basename(self.template.filename))[0]
        response["Content-Disposition"] = 'attachment; filename="%s.pdf"'\
            % (user_filename)
        return response
