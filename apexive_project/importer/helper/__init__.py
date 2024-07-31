import django
import os
import sys
sys.path.append("..") #preconfig
os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.getenv("DJANGO_SETTINGS_MODULE","apexive_project.settings"))
django.setup()