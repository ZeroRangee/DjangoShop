# Generated by Django 4.1.5 on 2023-01-15 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_available_alter_product_created_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0003_remove_cartuser_in_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartuser',
            name='final_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Общая цена'),
        ),
        migrations.RemoveField(
            model_name='cartuser',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='cartuser',
            name='products',
        ),
        migrations.AddField(
            model_name='cartuser',
            name='owner',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL, verbose_name='Владелец корзины'),
        ),
        migrations.AddField(
            model_name='cartuser',
            name='products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_cart', to='shop.product'),
        ),
    ]
