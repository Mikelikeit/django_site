from django.db import models


class PriceCard(models.Model):
    card_price = models.CharField(max_length=200, verbose_name='Цена')
    card_descript = models.CharField(max_length=200, verbose_name='Описание')

    def __str__(self):
        return self.card_price

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'


class PriceTable(models.Model):
    table_title = models.CharField(max_length=200, verbose_name='Услуга')
    table_old_price = models.PositiveIntegerField(verbose_name='Старая Цена')
    table_new_price = models.PositiveIntegerField(verbose_name='Новая Цена')

    def __str__(self):
        return self.table_title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
