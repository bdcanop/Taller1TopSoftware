# Generated by Django 4.1 on 2023-08-21 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('credit_card_info', models.IntegerField(max_length=16)),
                ('user_name', models.CharField(max_length=100)),
            ],
        ),
    ]
