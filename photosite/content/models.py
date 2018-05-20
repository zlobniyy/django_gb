from django.db import models
from main.models import *
from django.contrib.auth.models import User
from django.contrib import auth
from PIL import Image
from os import path
# from content.views import *
# Create your models here.
_MAX_SIZE = 2000

class Imagemodel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name=u'название', max_length=32, unique=False)
    category = models.ForeignKey(Categorymodel,verbose_name='Категория',blank=False, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images',blank=False)
    rating = models.PositiveIntegerField(verbose_name=u'рейтинг', default=0)
    description = models.TextField(verbose_name=u'описание', blank=True)
    date = models.DateField(verbose_name=u'дата загрузки изображения', auto_now_add=True)
    author = models.ForeignKey(User,verbose_name=u'Автор', blank=False, default='4', on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        # Сначала - обычное сохранение
        super(Imagemodel, self).save(*args, **kwargs)

        # Проверяем, указан ли логотип
        if self.image:
            filepath = self.image.path
            width = self.image.width
            height = self.image.height

            max_size = max(width, height)

            # Может, и не надо ничего менять?
            if max_size > _MAX_SIZE:
                # Надо, Федя, надо
                image = Image.open(filepath)
                # resize - безопасная функция, она создаёт новый объект, а не
                # вносит изменения в исходный, поэтому так
                image = image.resize(
                    (round(width / max_size * _MAX_SIZE),  # Сохраняем пропорции
                    round(height / max_size * _MAX_SIZE)),
                    Image.ANTIALIAS
                )
                # И не забыть сохраниться
                image.save(filepath)
