# Generated by Django 3.0.5 on 2020-04-14 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samplelogin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=dict, max_length=200),
            preserve_default=False,
        ),
    ]
