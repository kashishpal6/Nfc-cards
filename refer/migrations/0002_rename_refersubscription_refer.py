# Generated by Django 5.1.3 on 2024-12-09 09:16

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('refer', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='referSubscription',
            new_name='refer',
        ),
    ]
