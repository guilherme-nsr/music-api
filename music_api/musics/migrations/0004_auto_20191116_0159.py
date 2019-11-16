# Generated by Django 2.2.7 on 2019-11-16 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0003_auto_20191116_0009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='musics',
        ),
        migrations.AddField(
            model_name='music',
            name='album',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='musics', to='musics.Album'),
        ),
    ]
