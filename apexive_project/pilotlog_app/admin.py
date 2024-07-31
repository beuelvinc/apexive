from django.contrib import admin
from .models import *

admin.site.register([
    Aircraft,
    Airfield,
    Flight,
    ImagePic,
    LimitRules,
    MyQuery,
    MyQueryBuild,
    Pilot,
    Qualification,
    SettingConfig
])