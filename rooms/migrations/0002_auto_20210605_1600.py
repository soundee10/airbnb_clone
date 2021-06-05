# Generated by Django 3.2.4 on 2021-06-05 07:00

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='address',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='baths',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='bedrooms',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='beds',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='check_in',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='check_out',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='city',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
