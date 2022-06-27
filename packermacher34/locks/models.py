from django.db import models
from django.urls import reverse


class Category(models.Model):
    cat = models.CharField(max_length=255, verbose_name='Категория услуги')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def get_absolute_url(self):
        return reverse('show_category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = "Категория услуги"
        verbose_name_plural = "Категории услуг"
        ordering = ['pk']

    def __str__(self):
        return self.cat


class Sales(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Содержание акции')
    photo = models.ImageField(upload_to="photo_sales/%Y/%m/%d", blank=True, verbose_name='Фото')
    time_create = models.DateField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Акции"
        verbose_name_plural = "Акции"
        ordering = ['-time_create']


    def get_absolute_url(self):
        return reverse('show_sale')


class Price(models.Model):
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория")
    price = models.CharField(max_length=255, verbose_name='Цена')

    def __str__(self):
        return self.price

    class Meta:
        verbose_name = "Прайс"
        verbose_name_plural = "Прайс"

    def get_absolute_url(self):
        return reverse('show_services')


class Gallery(models.Model):
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория")
    photo = models.ImageField(upload_to="photo_work/%Y/%m/%d", verbose_name='Фото_работ')

    def get_absolute_url(self):
        return reverse('show_gallery')

    class Meta:
        verbose_name = "Галлерея"
        verbose_name_plural = "Галлерея"



class Contacts(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    phone_number = models.TextField(max_length=255, verbose_name='Номер телефона')
    date = models.CharField(max_length=255, verbose_name='Дата')
    time = models.CharField(max_length=255, verbose_name='Время')
    message = models.TextField(blank=True, verbose_name='Сообщение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Заявки с сайта"
        verbose_name_plural = "Заявки с сайта"
        ordering = ['pk']
