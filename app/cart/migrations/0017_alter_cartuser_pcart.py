# Generated by Django 4.1.5 on 2023-01-21 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0016_remove_cartuser_total_price_remove_cartuser_pcart_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartuser',
            name='pcart',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
