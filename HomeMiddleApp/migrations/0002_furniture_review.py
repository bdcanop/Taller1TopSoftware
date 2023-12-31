# Generated by Django 4.1 on 2023-08-21 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeMiddleApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Furniture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=100)),
                ('maker', models.CharField(max_length=30)),
                ('material', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.CharField(max_length=1000)),
                ('customer_rating', models.IntegerField()),
                ('moderation_status', models.CharField(max_length=30)),
                ('moderated_by', models.CharField(max_length=50)),
                ('posted_by', models.CharField(max_length=50)),
            ],
        ),
    ]
