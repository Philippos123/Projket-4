# Generated by Django 5.0.3 on 2024-03-08 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='number_of_people',
            field=models.IntegerField(default=0),
        ),
    ]