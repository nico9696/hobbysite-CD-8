# Generated by Django 5.1.6 on 2025-03-13 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merchstore', '0003_alter_product_product_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producttype',
            options={'ordering': ['name'], 'verbose_name': 'Product type', 'verbose_name_plural': 'Product type'},
        ),
    ]
