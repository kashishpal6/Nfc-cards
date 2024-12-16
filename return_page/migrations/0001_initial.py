# Generated by Django 5.1.3 on 2024-12-16 04:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('purchase', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReturnPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='returns/')),
                ('reason', models.TextField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('resolved', 'Resolved'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('return_date', models.DateTimeField(auto_now_add=True)),
                ('is_eligible', models.BooleanField(default=False)),
                ('refund_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('return_type', models.CharField(choices=[('exchange', 'Exchange'), ('refund', 'Refund'), ('store_credit', 'Store Credit')], default='refund', max_length=20)),
                ('purchase_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='purchase.purchase')),
            ],
        ),
    ]
