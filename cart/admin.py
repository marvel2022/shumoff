from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models

from .models import (    
    Customer,
    Order,
    OrderItem,
    # ShippingAddress,
    OrderedItem,

    ArticleModel,
)

class ArticleModelAdmin(admin.ModelAdmin):
    list_display       = ('title', 'author', 'published_at', 'updated_at', )
    list_display_links = ('title', 'published_at', 'updated_at', )
    list_editable      = ('author', )
    ordering           = ('title', 'author','published_at', 'updated_at', )
    search_fields      = ('title', 'author',)

    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        (
            'Образ', {
                'fields' : ('image', )
            }
        ),
        (
            'Содержание', {
                'fields' : ('title', 'slug', 'author', 'description',)
            }
        ),
        
    )

    formfield_overrides = {
        models.TextField : {'widget' : TinyMCE}
    }

admin.site.register(ArticleModel, ArticleModelAdmin)

# Register your models here.

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
# admin.site.register(ShippingAddress)

class OrderedItemAdmin(admin.ModelAdmin):
    #  ('customer', 'product', 'product_amount', 'single_price', 'total_price', 'date_ordered', 'completed', )
    list_display       = ('customer', 'product', 'product_amount', 'total_price', 'date_ordered', 'completed'  )
    list_display_links = ('customer', 'product', )
    # list_editable      = ('author', )
    ordering           = ('customer', 'product', 'product_amount', 'single_price', 'total_price', 'date_ordered', 'completed',  )
    search_fields      = ('customer', 'product', 'product_amount', 'single_price', 'total_price', 'date_ordered', 'completed', )

    fieldsets = (
        (
            'Клиент: ', {
                'fields':
                ('customer', 'product', 'product_amount', 'single_price', 'total_price', 'completed', ),
            }
        ),
        
    )

    formfield_overrides = {
        models.TextField : {'widget' : TinyMCE}
    }

admin.site.register(OrderedItem, OrderedItemAdmin)