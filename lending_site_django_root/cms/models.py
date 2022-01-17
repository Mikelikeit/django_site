from django.db import models


class CmsSlider(models.Model):
    slider_img = models.ImageField(upload_to='slider_img/', verbose_name='Изображение')
    slider_title = models.CharField(max_length=200, verbose_name='Заголовок')
    slider_text = models.CharField(max_length=200, verbose_name='Текст')
    slider_css = models.CharField(max_length=200, null=True, default='-', verbose_name='CSS Класс')

    def __str__(self):
        return self.slider_title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
