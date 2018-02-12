# Generated by Django 2.0.2 on 2018-02-12 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SelectGame', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='model_game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('comment', models.TextField(verbose_name='Comment')),
            ],
        ),
        migrations.AlterModelOptions(
            name='model_category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='model_game',
            name='category',
            field=models.ManyToManyField(to='SelectGame.model_category'),
        ),
    ]
