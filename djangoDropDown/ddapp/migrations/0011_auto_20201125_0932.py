# Generated by Django 3.1.3 on 2020-11-25 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ddapp', '0010_countrypresident'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='countrypresident',
            name='country_name',
        ),
        migrations.RemoveField(
            model_name='countrypresident',
            name='president_name',
        ),
        migrations.DeleteModel(
            name='Capital',
        ),
        migrations.DeleteModel(
            name='CountryName',
        ),
        migrations.DeleteModel(
            name='countrypresident',
        ),
        migrations.DeleteModel(
            name='President',
        ),
    ]
