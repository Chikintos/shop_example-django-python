# Generated by Django 4.0.3 on 2022-07-29 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_shop', '0005_alter_products_product_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_final_price',
            field=models.DecimalField(decimal_places=2, default=4, editable=False, max_digits=15, verbose_name=' ціна'),
        ),
    ]