# Generated by Django 2.0.2 on 2018-03-07 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_link',
            name='authenticated',
            field=models.BooleanField(default=False),
        ),
    ]
