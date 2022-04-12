from django.db import models
from django.urls import reverse

# from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from django.template.defaultfilters import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=200, unique=True, verbose_name='Категория:')
    slug          = models.SlugField(max_length=200, unique=True)
    image         = ImageField(upload_to="category/%Y/%m/%d/", verbose_name='Категория Образ:')
    added_date    = models.DateTimeField(auto_now_add="True")

    primary   = models.BooleanField(default=True, verbose_name="Основная")
    tools     = models.BooleanField(default=False, verbose_name="инструменты")
    accessory = models.BooleanField(default=False, verbose_name="Аксессуар")
    
    class Meta:
        ordering            = ['added_date']
        verbose_name        = 'Категория'
        verbose_name_plural = 'Категории'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.category_name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url  

class Product(models.Model):
    image       = ImageField(upload_to="product/%Y/%m/%d/", verbose_name='Образ')
    caption     = models.CharField(max_length=300, blank=True, null=True, verbose_name='Заголовок')

    name        = models.CharField(max_length=300, verbose_name='Hазвание')
    slug        = models.SlugField(max_length=320, unique=True)

    short_description = models.TextField(null=True, verbose_name='Краткое описание')
    description = models.TextField(verbose_name='Описание')
    # quantity    = models.PositiveIntegerField(default=0, verbose_name='Количество')

    # class CurrecyChoice(models.TextChoices):
    #     SUM="сум",_('сум')
    #     USD='$',_('доллар')
    #     RUB='₽',_('рубль')
    #     __empty__=_('')

    # currency    = models.CharField( verbose_name='Тип валюты:', max_length=5, choices=CurrecyChoice.choices, default=CurrecyChoice.SUM,)
    price       = models.DecimalField( verbose_name='Цена', max_digits=10, decimal_places=2, default=100, validators=( MinValueValidator(1), MaxValueValidator(100000000),))
    discount    = models.DecimalField( verbose_name='Скидка Цена', max_digits=10, decimal_places=2, blank=True, null=True, validators=( MinValueValidator(1), MaxValueValidator(100000000),))
    # price       = models.CharField(max_length=300, verbose_name="Цена")
    # discount    = models.CharField(max_length=300, blank=True, null=True, verbose_name="Скидка Цена")
    price_info  = models.CharField(max_length=300, blank=True, null=True, verbose_name="О цене")
    product_option = models.CharField(max_length=300, blank=True, null=True, verbose_name="Вариант продукта")
    quantity    = models.PositiveIntegerField(default=0, verbose_name='Количество')

    category     = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category', verbose_name='Категория:')
    # digital      = models.BooleanField(default=False,null=True, blank=True)

    published_at = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        ordering            = ['name', 'published_at', 'updated_at']
        verbose_name        = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('Core:detail-view', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def is_updated(self):
        if self.published_at == self.updated_at:
            return self.published_at
        else:
            self.updated_at

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class ProductType(models.Model):
    product  = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_price_option", verbose_name="Продукт")
    # price       = models.CharField(max_length=300, verbose_name="Цена")
    # discount    = models.CharField(max_length=300, blank=True, null=True, verbose_name="Скидка Цена")
    price       = models.DecimalField( verbose_name='Цена', max_digits=10, decimal_places=2, default=100, validators=( MinValueValidator(1), MaxValueValidator(100000000),))
    discount    = models.DecimalField( verbose_name='Скидка Цена', max_digits=10, decimal_places=2, blank=True, null=True, validators=( MinValueValidator(1), MaxValueValidator(100000000),))
    price_info  = models.CharField(max_length=300, blank=True, null=True, verbose_name="О цене")
    product_option = models.CharField(max_length=300, blank=True, null=True, verbose_name="Вариант продукта")
    quantity    = models.PositiveIntegerField(default=0, verbose_name='Количество')

    def __str__(self):
        return self.product.name
    class Meta:
        verbose_name_plural = "Тип продукта"

class Images(models.Model):
    product = models.ForeignKey(Product,  on_delete=models.CASCADE, related_name="product_images", verbose_name="Продукт")
    image   = ImageField(upload_to='product-images/%Y/%m/%d/', verbose_name="Образ")
    caption = models.CharField(max_length=300, blank=True, null=True, verbose_name='Заголовок')
    
    class Meta:
        verbose_name_plural = "Изображений"

    def __str__(self):
        return self.product.name

    @property
    def imageURL(self):
        try:
            url = self.images.url
        except:
            url = ''
        return url   


