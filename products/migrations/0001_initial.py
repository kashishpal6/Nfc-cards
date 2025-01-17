# Generated by Django 5.1.3 on 2025-01-03 07:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.services')),
            ],
            options={
                'verbose_name_plural': 'products',
                'ordering': ['title'],
            },
        ),
    ]
