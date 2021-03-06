# Generated by Django 3.1.3 on 2020-11-17 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ddapp', '0008_auto_20201114_0119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Capital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capital_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CountryName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='President',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('president_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='user_info',
            name='age',
        ),
        migrations.RemoveField(
            model_name='user_info',
            name='height',
        ),
        migrations.DeleteModel(
            name='User_A',
        ),
        migrations.DeleteModel(
            name='User_h',
        ),
        migrations.DeleteModel(
            name='User_Info',
        ),
        migrations.AddField(
            model_name='capital',
            name='country_name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ddapp.countryname'),
        ),
        migrations.AddField(
            model_name='capital',
            name='president_name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ddapp.president'),
        ),
    ]
