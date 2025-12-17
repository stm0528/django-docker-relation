import os
import django
from django.conf import settings
from django.http import HttpResponse
from django.urls import path
from django.core.management import execute_from_command_line

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

settings.configure(
    DEBUG=True,
    SECRET_KEY="docker-django-secret",
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["*"],
    MIDDLEWARE=[
        "django.middleware.common.CommonMiddleware",
    ],
)

def home(request):
    return HttpResponse("Hello from Django inside Docker 🚀")

urlpatterns = [
    path("", home),
]

django.setup()
