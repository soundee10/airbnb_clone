# Generated by Django 3.2.4 on 2021-06-06 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_auto_20210605_1735'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='Accuracy',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='check_in',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='cleanliness',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='communication',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='location',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rooms.room'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='value',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.TextField(null=True),
        ),
    ]
