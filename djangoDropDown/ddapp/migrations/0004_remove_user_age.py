# Generated by Django 3.1.3 on 2020-11-13 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ddapp', '0003_auto_20201114_0108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
    ]
