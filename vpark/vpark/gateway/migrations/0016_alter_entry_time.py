# Generated by Django 3.2 on 2021-05-10 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gateway', '0015_alter_entry_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='time',
            field=models.TimeField(default='01:15:06'),
        ),
    ]
