# Generated by Django 4.1 on 2023-08-21 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HomeMiddleApp', '0002_furniture_review'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Furniture',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
