# Generated by Django 5.1.6 on 2025-03-13 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0002_alter_article_options_alter_articlecategory_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_on'], 'verbose_name': 'Article', 'verbose_name_plural': 'Article'},
        ),
        migrations.AlterModelOptions(
            name='articlecategory',
            options={'ordering': ['name'], 'verbose_name': 'Article Category', 'verbose_name_plural': 'Article Category'},
        ),
    ]
