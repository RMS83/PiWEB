from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=60, unique=True, verbose_name='Наименование товара')
    description = models.TextField(null=True, blank=True, verbose_name='Описание товара')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Stock(models.Model):
    address = models.CharField(max_length=200, unique=True, verbose_name='Адрес склада')
    products = models.ManyToManyField(
        Product,
        through='StockProduct',
        related_name='stocks',
        verbose_name='Продукты на складе'
    )

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'


class StockProduct(models.Model):
    stock = models.ForeignKey(
        Stock,
        on_delete=models.CASCADE,
        related_name='positions',

    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='positions',

    )
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество на складе')
    price = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name='Стоимость хранения'
    )
