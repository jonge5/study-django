# Generated by Django 5.0.2 on 2024-02-22 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friend', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friend',
            old_name='sander',
            new_name='sender',
        ),
    ]
