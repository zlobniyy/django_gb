from django.db import models
from main.models import *
from django.contrib.auth.models import User
from django.contrib import auth
# from content.views import *
# Create your models here.


class Imagemodel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name=u'название', max_length=32, unique=False)
    category = models.ForeignKey(Categorymodel,verbose_name='Категория',blank=False)
    image = models.ImageField(upload_to='images',blank=False)
    rating = models.PositiveIntegerField(verbose_name=u'рейтинг', default=0)
    description = models.TextField(verbose_name=u'описание', blank=True)
    date = models.DateField(verbose_name=u'дата загрузки изображения', auto_now_add=True)
    author = models.ForeignKey(User,verbose_name=u'Автор', blank=False, default='4')