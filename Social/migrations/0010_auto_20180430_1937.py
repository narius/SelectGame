# Generated by Django 2.0.4 on 2018-04-30 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Social', '0009_auto_20180430_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privatemessage',
            name='notification',
            field=models.ManyToManyField(blank=True, related_name='message', to='Social.Notification', verbose_name='notification'),
        ),
    ]
