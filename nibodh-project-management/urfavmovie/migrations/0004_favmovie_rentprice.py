# Generated by Django 3.2.6 on 2021-09-11 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urfavmovie', '0003_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='favmovie',
            name='RentPrice',
            field=models.FloatField(default=0),
        ),
    ]
