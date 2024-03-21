# Generated by Django 5.0.2 on 2024-02-27 21:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=80)),
                ('post_content', models.TextField()),
                ('post_status', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.user')),
            ],
            options={
                'db_table': 'tbl_post',
                'ordering': ['-id'],
            },
        ),
    ]