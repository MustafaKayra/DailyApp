# Generated by Django 5.0.6 on 2025-01-23 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='role',
        ),
        migrations.DeleteModel(
            name='UserRole',
        ),
    ]
