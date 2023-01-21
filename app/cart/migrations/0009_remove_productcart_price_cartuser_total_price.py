# Generated by Django 4.1.5 on 2023-01-16 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_alter_cartuser_user_productcart_cartuser_pcart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcart',
            name='price',
        ),
        migrations.AddField(
            model_name='cartuser',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Цена'),
        ),
    ]
