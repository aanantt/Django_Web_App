# Generated by Django 3.0.5 on 2020-04-27 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samplelogin', '0006_auto_20200427_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='userprofile/avatar.png', max_length=200, upload_to='userprofile/'),
        ),
    ]
