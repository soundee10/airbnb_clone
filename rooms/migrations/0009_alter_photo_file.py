# Generated by Django 3.2.4 on 2021-06-08 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0008_alter_photo_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(upload_to='room_photos'),
        ),
    ]
