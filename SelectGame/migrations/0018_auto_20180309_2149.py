# Generated by Django 2.0.2 on 2018-03-09 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SelectGame', '0017_auto_20180309_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_event',
            name='messages',
            field=models.ManyToManyField(blank=True, null=True, to='Social.model_message'),
        ),
    ]
