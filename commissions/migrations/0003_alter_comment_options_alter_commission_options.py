# Generated by Django 5.1.6 on 2025-03-13 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0002_rename_commissions_commission'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_on'], 'verbose_name': 'Comment', 'verbose_name_plural': 'Comment'},
        ),
        migrations.AlterModelOptions(
            name='commission',
            options={'ordering': ['created_on'], 'verbose_name': 'Commission', 'verbose_name_plural': 'Commission'},
        ),
    ]
