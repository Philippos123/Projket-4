# Generated by Django 5.0.3 on 2024-03-09 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_news_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'news'},
        ),
    ]
