# Generated by Django 4.0 on 2021-12-20 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='beat',
            name='mp3',
            field=models.FileField(default='', upload_to='audio/mp3/'),
        ),
        migrations.AddField(
            model_name='beat',
            name='wave',
            field=models.FileField(default='', upload_to='audio/wave/'),
        ),
        migrations.AddField(
            model_name='beat',
            name='wrap',
            field=models.ImageField(default='', upload_to='images/wraps/'),
        ),
    ]
