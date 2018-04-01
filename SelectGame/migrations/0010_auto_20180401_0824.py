# Generated by Django 2.0.2 on 2018-04-01 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SelectGame', '0009_auto_20180401_0815'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventgamevote',
            name='game',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='SelectGame.Game'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='eventgame',
            name='games',
            field=models.ManyToManyField(to='SelectGame.Rating'),
        ),
        migrations.AlterUniqueTogether(
            name='eventgamevote',
            unique_together={('game', 'user')},
        ),
    ]