# Generated by Django 3.1.1 on 2020-09-28 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category_ID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Eshop.category'),
        ),
    ]
