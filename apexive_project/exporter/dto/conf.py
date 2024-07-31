import os
import django
def setup():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.getenv("DJANGO_SETTINGS_MODULE","apexive_project.settings"))
    django.setup()
