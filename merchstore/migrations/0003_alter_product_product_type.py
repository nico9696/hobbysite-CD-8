# Generated by Django 5.1.6 on 2025-03-10 08:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchstore', '0002_alter_product_options_alter_producttype_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='merchstore.producttype'),
        ),
    ]
