from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from sorl.thumbnail.admin import AdminImageMixin

from .models import (
    Category, 
    Product, 
    ProductType,
    Images, 
)


# Register your models here.
class CategoryAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('category_name', 'primary', 'tools', 'accessory',)
    ordering = ('category_name', 'primary', 'tools', 'accessory',)
    search_fields = ('category_name', 'primary', 'tools', 'accessory',)
    list_editable = ('primary', 'tools', 'accessory')

    prepopulated_fields = {'slug': ('category_name', )}
    
    fieldsets = (
        ('Категория', {
            "fields": (
                'category_name',
                'slug',
                'image',

                'primary', 
                'tools', 
                'accessory',
            ),
        }),
    )

admin.site.register(Category, CategoryAdmin)

class ProductImageAdmin(AdminImageMixin, admin.TabularInline):
    model   = Images
    extra   = 1
    max_num = 3
class ProductTypeAdmin(admin.TabularInline):
    model   = ProductType
    extra   = 1
    max_num = 5
class ProductAdmin(AdminImageMixin, admin.ModelAdmin):
    inlines = [ProductTypeAdmin, ProductImageAdmin]
     
    list_display       = ('category', 'name', 'price', 'discount', "product_option", "quantity", 'published_at', 'updated_at', )
    list_display_links = ('name', 'published_at', 'updated_at', )
    search_fields      = ('name', 'price', 'discount', 'category', 'published_at', 'updated_at', )
    ordering           = ('name', 'price', 'discount', 'category', 'published_at', 'updated_at', )
    list_editable      = ('price', 'discount',   'category', )


    prepopulated_fields = {'slug': ('name', )}

    fieldsets = (
        ('Категория', {
            "fields": (
                ('category',)
            ),
        }),
        ('Изображений', {
            "fields": (
                'image',
                'caption',
            ),
        }),
        ('Товар', {
            "fields": (
                ('name', 'slug', 'short_description', 'description', 'price', 'discount', 'price_info', 'product_option', 'quantity')
            ),
        }),
    )
    formfield_overrides = {
        models.TextField : {'widget' : TinyMCE}
    }
    
admin.site.register(Product, ProductAdmin)