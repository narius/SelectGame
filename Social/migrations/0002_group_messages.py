# Generated by Django 2.0.2 on 2018-03-23 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Social', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='messages',
            field=models.ManyToManyField(to='Social.UserMessage', verbose_name='messages'),
        ),
    ]
