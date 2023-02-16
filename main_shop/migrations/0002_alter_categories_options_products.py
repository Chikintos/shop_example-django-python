# Generated by Django 4.0.3 on 2022-07-29 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'Категорія', 'verbose_name_plural': 'Категорії'},
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=150, verbose_name='Назва товару')),
                ('product_description', models.CharField(max_length=350, verbose_name='опис товару')),
                ('product_price_initial', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Початкова ціна')),
                ('Category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_shop.categories')),
            ],
        ),
    ]
