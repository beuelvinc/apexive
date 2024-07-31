from django.contrib import admin
from .models import Aircraft, Flight

admin.site.register([Aircraft, Flight])
