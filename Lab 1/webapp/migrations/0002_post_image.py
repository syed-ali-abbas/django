# Generated by Django 3.1.7 on 2021-03-06 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Image',
            field=models.ImageField(blank=True, upload_to='products/'),
        ),
    ]
