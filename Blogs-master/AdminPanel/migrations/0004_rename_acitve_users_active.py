# Generated by Django 4.1.7 on 2023-03-11 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0003_blogs_blogtagmapping_history_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='acitve',
            new_name='active',
        ),
    ]