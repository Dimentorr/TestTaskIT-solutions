# Generated by Django 5.1.2 on 2024-10-13 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='avatar',
        ),
    ]
