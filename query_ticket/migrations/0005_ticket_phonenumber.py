# Generated by Django 5.1.3 on 2024-12-13 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query_ticket', '0004_alter_ticket_fullname_alter_ticket_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='phoneNumber',
            field=models.CharField(default='0000', max_length=10),
        ),
    ]
