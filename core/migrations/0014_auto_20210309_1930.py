# Generated by Django 3.1.7 on 2021-03-09 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20210309_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='media/media/default_icon_a2OAY11.jpg', upload_to='media'),
        ),
    ]