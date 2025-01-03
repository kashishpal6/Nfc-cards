# Generated by Django 5.1.3 on 2025-01-03 07:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('variant', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(default='default', max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed'), ('refunded', 'Refunded')], default='pending', max_length=20)),
                ('payment_method', models.CharField(default='NFC', max_length=50)),
                ('payment_at', models.DateTimeField(auto_now_add=True)),
                ('UTR', models.CharField(default='blank', max_length=100)),
                ('product_variation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variation', to='variant.variant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['status'],
            },
        ),
    ]
