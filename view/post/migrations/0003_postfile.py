# Generated by Django 5.0.2 on 2024-02-28 18:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_post_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.ImageField(upload_to='post/%Y/%m/%d')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='post.post')),
            ],
            options={
                'db_table': 'tbl_post_file',
            },
        ),
    ]
