# Generated by Django 3.2 on 2021-05-01 21:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0002_auto_20210501_0438'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='vehicle_no',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='end_time',
            field=models.TimeField(default='03:13:40'),
        ),
        migrations.AlterField(
            model_name='book',
            name='start_time',
            field=models.TimeField(default='03:13:40'),
        ),
        migrations.AlterField(
            model_name='book',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
