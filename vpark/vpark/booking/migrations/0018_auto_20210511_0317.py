# Generated by Django 3.2 on 2021-05-10 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0017_auto_20210511_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='end_time',
            field=models.TimeField(default='03:17:49'),
        ),
        migrations.AlterField(
            model_name='book',
            name='start_time',
            field=models.TimeField(default='03:17:49'),
        ),
    ]
