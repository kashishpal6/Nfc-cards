# Generated by Django 5.1.3 on 2025-01-03 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='fullName',
        ),
        migrations.AddField(
            model_name='profile',
            name='fullName',
            field=models.CharField(default='null', max_length=250),
        ),
    ]
