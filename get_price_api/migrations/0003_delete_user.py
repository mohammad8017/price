# Generated by Django 4.0.3 on 2022-04-05 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('get_price_api', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]