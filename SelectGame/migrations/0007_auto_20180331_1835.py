# Generated by Django 2.0.2 on 2018-03-31 18:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SelectGame', '0006_auto_20180331_1821'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='eventparticipant',
            unique_together={('user', 'event')},
        ),
    ]
