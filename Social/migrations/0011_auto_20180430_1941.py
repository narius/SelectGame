# Generated by Django 2.0.4 on 2018-04-30 19:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Social', '0010_auto_20180430_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privatemessage',
            name='participants',
            field=models.ManyToManyField(related_name='private_messages', to=settings.AUTH_USER_MODEL, verbose_name='participants'),
        ),
    ]