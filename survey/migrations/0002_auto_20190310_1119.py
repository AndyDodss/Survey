# Generated by Django 2.1.7 on 2019-03-10 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ask',
            name='rateA',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ask',
            name='rateB',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ask',
            name='rateC',
            field=models.IntegerField(default=0),
        ),
    ]
