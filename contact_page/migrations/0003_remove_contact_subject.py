# Generated by Django 5.1.3 on 2024-12-13 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_page', '0002_rename_query_contact_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='subject',
        ),
    ]
