# Generated by Django 4.0.1 on 2022-01-10 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricecard',
            name='card_price',
            field=models.CharField(max_length=200, verbose_name='Цена'),
        ),
    ]
