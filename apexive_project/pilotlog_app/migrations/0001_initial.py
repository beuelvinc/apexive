# Generated by Django 5.0.7 on 2024-07-31 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('guid', models.UUIDField()),
                ('platform', models.IntegerField()),
                ('_modified', models.IntegerField()),
                ('meta', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('guid', models.UUIDField()),
                ('platform', models.IntegerField()),
                ('_modified', models.IntegerField()),
                ('meta', models.JSONField()),
            ],
        ),
    ]
