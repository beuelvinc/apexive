# Generated by Django 5.0.7 on 2024-07-31 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pilotlog_app', '0003_airfield_flight_imagepic_limitrules_myquery_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aircraft',
            name='table',
        ),
        migrations.RemoveField(
            model_name='airfield',
            name='table',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='table',
        ),
        migrations.RemoveField(
            model_name='imagepic',
            name='table',
        ),
        migrations.RemoveField(
            model_name='limitrules',
            name='table',
        ),
        migrations.RemoveField(
            model_name='myquery',
            name='table',
        ),
        migrations.RemoveField(
            model_name='myquerybuild',
            name='table',
        ),
        migrations.RemoveField(
            model_name='pilot',
            name='table',
        ),
        migrations.RemoveField(
            model_name='qualification',
            name='table',
        ),
        migrations.RemoveField(
            model_name='settingconfig',
            name='table',
        ),
    ]