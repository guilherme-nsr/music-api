# Generated by Django 2.2.7 on 2019-12-07 09:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('musics', '0007_auto_20191116_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='person', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]