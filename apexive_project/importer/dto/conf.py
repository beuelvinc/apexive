import os
import django
from django.conf import  settings
def setup():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.getenv("DJANGO_SETTINGS_MODULE","apexive_project.settings"))
    django.setup()
