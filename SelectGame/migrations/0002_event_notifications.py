# Generated by Django 2.0.2 on 2018-03-29 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Social', '0004_auto_20180329_2104'),
        ('SelectGame', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='notifications',
            field=models.ManyToManyField(to='Social.Notification'),
        ),
    ]
