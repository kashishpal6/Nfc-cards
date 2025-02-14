# Generated by Django 5.1.3 on 2025-01-03 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('nfc', 'NFC Card'), ('menucard', 'Menu Card'), ('vcard', 'Contact Card'), ('payment', 'NFC with payment'), ('miniweb', 'Web page')], max_length=200)),
                ('description', models.TextField(max_length=500)),
                ('price', models.PositiveIntegerField(default=999)),
                ('image', models.ImageField(upload_to='services/')),
            ],
            options={
                'verbose_name_plural': 'services',
                'ordering': ['type'],
            },
        ),
    ]
