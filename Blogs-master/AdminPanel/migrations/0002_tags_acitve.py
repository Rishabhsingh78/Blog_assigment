# Generated by Django 4.1.7 on 2023-03-11 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tags',
            name='acitve',
            field=models.BooleanField(default=True),
        ),
    ]
