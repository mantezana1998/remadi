# Generated by Django 3.2.6 on 2021-10-28 23:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0002_auto_20211028_2245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='date',
            name='user',
        ),
        migrations.AddField(
            model_name='date',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
