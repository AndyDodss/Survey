# Generated by Django 2.1.7 on 2019-03-18 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_auto_20190311_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='ask',
            name='is_visible',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
