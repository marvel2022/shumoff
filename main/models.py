from django.db import models
from django.urls import reverse

# from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _
# Create your models here.

class New(models.Model):
    image = models.ImageField(upload_to='news-image/%Y/%m/%d/', blank=True, null=True, verbose_name='Образ:')
    caption = models.CharField(max_length=500, blank=True, null=True, verbose_name = "Заголовок: ")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Новый"
        verbose_name_plural = "Новости"
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url  

class Home(models.Model):
    image = models.ImageField(upload_to='home-image/%Y/%m/%d/', blank=True, null=True, verbose_name='Образ:')
    caption = models.CharField(max_length=500, blank=True, null=True, verbose_name = "Заголовок: ")

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = "Главная"
        verbose_name_plural = "Главная"
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url  


class ToolVideo(models.Model):
    video = models.FileField(upload_to='tool-video/%Y/%m/%d/', verbose_name="Bидео")
    name  = models.CharField(max_length=200, verbose_name="заглавие")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Инструменты Vdieo"