# Generated by Django 5.0rc1 on 2023-12-07 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_salesorder_user'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesorder',
            name='products',
            field=models.ManyToManyField(to='products.products'),
        ),
    ]
