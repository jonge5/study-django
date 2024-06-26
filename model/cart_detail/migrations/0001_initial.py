# Generated by Django 5.0.2 on 2024-02-23 12:58

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
        ('product', '0002_alter_product_options_remove_product_member_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('quantity', models.IntegerField(default=1)),
                ('status', models.SmallIntegerField(default=0)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cart.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product')),
            ],
            options={
                'db_table': 'tbl_cart_detail',
                'ordering': ['-id'],
            },
        ),
    ]
