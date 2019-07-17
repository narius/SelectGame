# Generated by Django 2.0.4 on 2018-04-30 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Social', '0008_notification_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ['-created'], 'verbose_name': 'notification', 'verbose_name_plural': 'notifications'},
        ),
        migrations.RemoveField(
            model_name='usermessage',
            name='notification',
        ),
        migrations.AddField(
            model_name='privatemessage',
            name='notification',
            field=models.ManyToManyField(blank=True, null=True, related_name='message', to='Social.Notification', verbose_name='notification'),
        ),
    ]