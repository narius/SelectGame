# Generated by Django 2.0.2 on 2018-03-03 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SelectGame', '0013_model_game_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_event',
            name='name',
            field=models.CharField(blank=True, max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='model_game',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/game_images'),
        ),
    ]
