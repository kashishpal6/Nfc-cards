# Generated by Django 5.1.3 on 2024-12-06 10:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('size', models.CharField(blank=True, max_length=50, null=True)),
                ('orientation', models.CharField(choices=[('horizontal', 'Horizontal'), ('vertical', 'Vertical')], default='horizontal', max_length=200)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('front_image', models.ImageField(null=True, upload_to='uploads/front_images/')),
                ('back_image', models.ImageField(null=True, upload_to='uploads/back_images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='products.products')),
            ],
            options={
                'ordering': ['product', 'color', 'size'],
            },
        ),
    ]
