# Generated by Django 4.0 on 2022-05-22 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0006_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrumento',
            name='imagenInstrumento',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
