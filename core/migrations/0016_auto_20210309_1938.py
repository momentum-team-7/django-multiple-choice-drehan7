# Generated by Django 3.1.7 on 2021-03-09 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20210309_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='media/iconfinder_moon_dark_mode_night_5402400.png', upload_to='media'),
        ),
    ]
