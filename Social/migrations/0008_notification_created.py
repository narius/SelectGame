# Generated by Django 2.0.2 on 2018-04-15 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Social', '0007_auto_20180415_0628'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
