# Generated by Django 2.0.2 on 2018-03-11 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SelectGame', '0022_auto_20180311_1753'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='model_game',
            options={'ordering': ['name'], 'verbose_name': 'game', 'verbose_name_plural': 'games'},
        ),
    ]