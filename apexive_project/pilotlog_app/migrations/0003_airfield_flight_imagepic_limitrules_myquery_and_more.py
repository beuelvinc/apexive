# Generated by Django 5.0.7 on 2024-07-31 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pilotlog_app', '0002_pilotdata_delete_aircraft_delete_flight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airfield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('table', models.CharField(max_length=255)),
                ('guid', models.UUIDField()),
                ('platform', models.IntegerField()),
                ('_modified', models.IntegerField()),
                ('meta', models.JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('table', models.CharField(max_length=255)),
                ('guid', models.UUIDField()),
                ('platform', models.IntegerField()),
                ('_modified', models.IntegerField()),
                ('meta', models.JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImagePic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('table', models.CharField(max_length=255)),
                ('guid', models.UUIDField()),
                ('platform', models.IntegerField()),
                ('_modified', models.IntegerField()),
                ('meta', models.JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LimitRules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('table', models.CharField(max_length=255)),
                ('guid', models.UUIDField()),
                ('platform', models.IntegerField()),
                ('_modified', models.IntegerField()),
                ('meta', models.JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MyQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('table', models.CharField(max_length=255)),
                ('guid', models.UUIDField()),
                ('platform', models.IntegerField()),
                ('_modified', models.IntegerField()),
                ('meta', models.JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MyQueryBuild',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('table', models.CharField(max_length=255)),
                ('guid', models.UUIDField()),
                ('platform', models.IntegerField()),
                ('_modified', models.IntegerField()),
                ('meta', models.JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pilot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('table', models.CharField(max_length=255)),
                ('guid', models.UUIDField()),
                ('platform', models.IntegerField()),
                ('_modified', models.IntegerField()),
                ('meta', models.JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('table', models.CharField(max_length=255)),
                ('guid', models.UUIDField()),
                ('platform', models.IntegerField()),
                ('_modified', models.IntegerField()),
                ('meta', models.JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SettingConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('table', models.CharField(max_length=255)),
                ('guid', models.UUIDField()),
                ('platform', models.IntegerField()),
                ('_modified', models.IntegerField()),
                ('meta', models.JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameModel(
            old_name='PilotData',
            new_name='Aircraft',
        ),
    ]