# Generated by Django 5.1.6 on 2025-03-13 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merchstore', '0004_alter_producttype_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name'], 'verbose_name': 'Product', 'verbose_name_plural': 'Product'},
        ),
        migrations.AlterModelOptions(
            name='producttype',
            options={'ordering': ['name'], 'verbose_name': 'Product Type', 'verbose_name_plural': 'Product Type'},
        ),
    ]
