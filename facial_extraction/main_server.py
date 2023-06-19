import os, sys

sys.path.append('interface')
sys.path.append('core')


from app_config_provider import AppConfigProvider
from app_logic import AppLogic
from json_matrix_parser import JsonMatrixParser

from django.conf import settings
from django.urls import path
from django.core.management import execute_from_command_line
from django.http import HttpResponse

settings.configure(
    DEBUG=True,
    SECRET_KEY="4l0ngs3cr3tstr1ngw3lln0ts0l0ngw41tn0w1tsl0ng3n0ugh",
    IGNORABLE_404_URLS=[r"^favicon\.ico$"],
    ROOT_URLCONF=sys.modules[__name__],
)


def getHello(request):
    return HttpResponse("<h1>Hello from server!</h1>")


def getFacesCoordsFromImageFile(request, faces_image_file):
    print("Server.getFacesCoordsFromImageFile.faces_image_file = " + faces_image_file)
    maxrix_result = app.extract_faces_coords_from_file(faces_image_file)
    json_result = parser.mapMatrixIntoJson(maxrix_result)
    return HttpResponse(json_result)

urlpatterns = [
    path(r"hello", getHello),
    path(r"faces/<faces_image_file>", getFacesCoordsFromImageFile, name="some-name"),
]

if __name__ == "__main__":
    appConfigProvider = AppConfigProvider()
    app_config = appConfigProvider.app_config
    image_input_dir = app_config["image_input_dir"]

    app = AppLogic(image_input_dir)
    parser = JsonMatrixParser()

    execute_from_command_line(sys.argv)
