# Generated by Django 4.1.5 on 2023-01-05 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=120)),
                ('slug', models.CharField(db_index=True, max_length=120, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='product/%Y/%m/%d')),
                ('description', models.TextField(blank=True, max_length=1500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('uploaded', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.category')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ('name',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]
