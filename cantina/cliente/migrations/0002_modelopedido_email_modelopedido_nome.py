# Generated by Django 5.0.dev20230218152810 on 2023-02-24 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelopedido',
            name='email',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='modelopedido',
            name='nome',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
