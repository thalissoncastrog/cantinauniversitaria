# Generated by Django 5.0.dev20230218152810 on 2023-02-25 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_modelopedido_email_modelopedido_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemdemenu',
            name='disponivel',
            field=models.BooleanField(default=True),
        ),
    ]
