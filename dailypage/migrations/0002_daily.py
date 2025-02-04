# Generated by Django 5.0.6 on 2025-01-24 22:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailypage', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Daily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gratitude', models.TextField()),
                ('field1', models.TextField()),
                ('affirmations', models.TextField()),
                ('field2', models.TextField()),
                ('field3', models.TextField()),
                ('field4', models.TextField()),
                ('field5', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Video Sahibi')),
            ],
        ),
    ]
