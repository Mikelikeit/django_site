from django.db import models


class StatusCrm(models.Model):
    status = models.CharField(max_length=200, verbose_name='Статус')

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True, verbose_name='Дата Заказа')
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderComment(models.Model):
    order_comment = models.ForeignKey(Order, on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=1000, verbose_name='Комментарий')
    comment_dt = models.DateTimeField(auto_now=True, verbose_name='Дата Комментария')

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
