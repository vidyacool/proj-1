# Generated by Django 4.1.3 on 2022-11-03 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Transliteration', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transliteration',
            name='image',
        ),
    ]
