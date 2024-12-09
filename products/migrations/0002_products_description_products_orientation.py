# Generated by Django 5.1.3 on 2024-12-10 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='products',
            name='orientation',
            field=models.CharField(choices=[('horizontal', 'Horizontal'), ('vertical', 'Vertical')], default='horizontal', max_length=200),
        ),
    ]
