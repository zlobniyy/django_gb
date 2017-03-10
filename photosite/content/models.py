from django.db import models
from main.models import *
from django.contrib import auth
# Create your models here.


class Imagemodel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name=u'название', max_length=32, unique=True)
    category = models.ForeignKey(Categorymodel)
    image = models.ImageField(upload_to='images',blank=True)
    rating = models.PositiveIntegerField(verbose_name=u'рейтинг', default=0)
    description = models.TextField(verbose_name=u'описание', blank=True)
    # date = models.DateField(verbose_name=u'дата загрузки изображения', auto_now_add=True)