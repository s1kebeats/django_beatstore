# Generated by Django 4.0.1 on 2022-02-03 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beats', '0007_alter_beat_mp3_alter_beat_wave_alter_beat_wrap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beat',
            name='wrap',
            field=models.ImageField(default='media/wraps/S.svg', upload_to='media/wraps/'),
        ),
    ]