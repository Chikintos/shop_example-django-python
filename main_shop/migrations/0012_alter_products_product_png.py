# Generated by Django 4.0.6 on 2022-07-30 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_shop', '0011_alter_products_product_png'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_png',
            field=models.ImageField(blank=True, default=0, null=True, upload_to='media\\img\\%Y\\%m\\%d'),
        ),
    ]
