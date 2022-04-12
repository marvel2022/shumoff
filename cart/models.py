from django.db import models
from django.urls import reverse

# from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

User = get_user_model()

from core.models import Product, Category
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True,  on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, verbose_name="имя: ")
    phone = models.CharField(max_length=200, null=True, verbose_name="Телефонный номер: ")
    address = models.CharField(max_length=500, null=True, verbose_name = "Адрес: ")
   
    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return str(self.user)

    @property
    def get_ordered_total(self):
        ordereditems = self.customer_orders.all()
        total = sum([item.get_total for item in ordereditems if item.completed == False])
        return total 

    @property
    def get_ordered_items(self):
        ordereditems = self.customer_orders.all()
        total = sum([item.product_amount for item in ordereditems if item.completed == False])
        return total

    @property
    def get_completed_total(self):
        ordereditems = self.customer_orders.all()
        total = sum([item.get_total for item in ordereditems if item.completed == True])
        return total 

    @property
    def get_completed_items(self):
        ordereditems = self.customer_orders.all()
        total = sum([item.product_amount for item in ordereditems if item.completed == True])
        return total

        

def post_save_user_receiver(sender, instance, created, **kwargs):
    user = instance
    if created:
        customer = Customer(user=user)
        customer.save()

post_save.connect(post_save_user_receiver, sender=User)


class OrderedItem(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE, related_name="customer_orders", verbose_name = "Клиент: ")
    product  = models.CharField(max_length=300, blank=True, null=True, verbose_name="Продукт: ")
    product_option = models.CharField(max_length=100, null=True, blank=True, verbose_name="Вариант продукта")
    image    = models.ImageField(upload_to="ordered-product/%Y/%m/%d/", blank=True, null=True, verbose_name='Образ:')
    product_amount = models.IntegerField(default=0, verbose_name="Количество товара: ")
    single_price   = models.FloatField(default=0, verbose_name="Цена продукта: ")
    total_price    = models.FloatField(default=0, verbose_name="Итоговая цена: ")
    date_ordered   = models.DateTimeField(auto_now_add=True, verbose_name = "Дата заказа: ")
    completed      = models.BooleanField(default=False, verbose_name="Завершено: ")

    def __str__(self):
        return str(self.customer) + " | " + str(self.completed)
    
    @property
    def get_total(self):
        total = self.single_price * self.product_amount
        return total

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    class Meta:
        ordering = ["-date_ordered"]
        verbose_name = "Заказанный товар"
        verbose_name_plural = "Заказанные товары"

def post_save_customer_receiver(sender, instance, created, **kwargs):
    customer = instance
    if created:
        ordered_item = OrderedItem(customer=customer)
        ordered_item.save()

post_save.connect(post_save_customer_receiver, sender=Customer)



class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True) # Customer returns user email
    complete = models.BooleanField(default=False, verbose_name='Завершено: ')
    date_ordered = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа: ')
    transaction_id = models.CharField(max_length=100, null=True, verbose_name='номер транзакции: ')

    class Meta:
        verbose_name = "порядок"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return str(self.id)
        
 

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name="ordered_product", null=True)
    order   = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    option_price    = models.DecimalField( verbose_name='Цена', max_digits=10, decimal_places=2, default=100, validators=( MinValueValidator(1), MaxValueValidator(100000000),))
    option_discount = models.DecimalField( verbose_name='Скидка Цена', max_digits=10, decimal_places=2, blank=True, null=True, validators=( MinValueValidator(1), MaxValueValidator(100000000),))
    option_info     = models.CharField(max_length=100, blank=True, null=True, verbose_name="Вариант продукта")
    quantity   = models.IntegerField(default=0, null=True, blank=True, verbose_name="Количество: ")
    option_pk  = models.CharField(max_length=5, blank=True, null=True, verbose_name="вариант pk")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Дата заказа: ")

    class Meta:
        verbose_name="Позиция заказа"
        verbose_name_plural="Позиция заказа"

    # @property
    # def get_total(self):
    #     price = 0
    #     if self.product.discount:
    #         price = self.product.discount
    #     else:
    #         price = self.product.price
    #     total = price * self.quantity
    #     return total

    @property
    def get_total(self):
        price = 0
        if self.option_discount:
            price = self.option_discount
        else:
            price = self.option_price
        total = price * self.quantity
        return total

# class ShippingAddress(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
#     address = models.CharField(max_length=200, null=False)
#     city = models.CharField(max_length=200, null=False)
#     # state = models.CharField(max_length=200, null=False)
#     # zipcode = models.CharField(max_length=200, null=False)
#     date_added = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.address


class ArticleModel(models.Model):
    image        = models.ImageField(upload_to="article/%Y/%m/%d/", verbose_name='Изображение статьи:')
    # caption      = models.CharField(max_length=300, blank=True, null=True, verbose_name='заголовок:')

    title        = models.CharField(max_length=350, unique=True, verbose_name='заглавие:')
    slug         = models.SlugField(unique=True, max_length=400)
    description  = models.TextField(verbose_name='Описание:')
    author       = models.CharField(max_length=50, default='ShumOff', verbose_name = 'Автор:')
    view_counter = models.PositiveIntegerField(default=0)

    published_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано:')
    updated_at   = models.DateTimeField(auto_now=True, verbose_name='Обновлено:')

    class Meta:
        ordering            = ['published_at', 'updated_at',]
        verbose_name        = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title 

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("Core:article-detail-view", kwargs={"slug": self.slug})
    
    def is_updated(self):
        if self.published_at == self.updated_at:
            return self.published_at
        else:
            return self.updated_at
        
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    