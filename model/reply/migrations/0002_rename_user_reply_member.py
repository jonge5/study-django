# Generated by Django 5.0.2 on 2024-02-22 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reply', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='user',
            new_name='member',
        ),
    ]