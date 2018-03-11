# Generated by Django 2.0.2 on 2018-03-11 09:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SelectGame', '0020_auto_20180311_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_event',
            name='maximum_number_of_players',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='maximum number of players'),
        ),
        migrations.AddField(
            model_name='model_event',
            name='minimum_number_of_players',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='minimum number of players'),
        ),
    ]