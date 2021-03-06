# Generated by Django 4.0.1 on 2022-02-03 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beats', '0006_alter_beat_wrap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beat',
            name='mp3',
            field=models.FileField(default='', upload_to='media/audio/mp3/'),
        ),
        migrations.AlterField(
            model_name='beat',
            name='wave',
            field=models.FileField(default='', upload_to='media/audio/wave/'),
        ),
        migrations.AlterField(
            model_name='beat',
            name='wrap',
            field=models.ImageField(default='media/wraps/S.svg', upload_to='wraps/'),
        ),
    ]
