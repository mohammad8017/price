# Generated by Django 4.0.3 on 2022-04-05 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_price_api', '0003_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]