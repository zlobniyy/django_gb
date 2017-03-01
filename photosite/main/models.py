from django.db import models
from django.utils.timezone import now


# Create your models here.

class Categorymodel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name=u'название', max_length=16)
    description = models.TextField(verbose_name=u'описание')
    image = models.ImageField(verbose_name=u'картинка категории', upload_to='upload')
    date = models.DateField(verbose_name=u'дата создания категории', auto_now_add=True)


class Imagemodel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name=u'название', max_length=32, unique=True)
    category = models.ForeignKey(Categorymodel)
    image = models.ImageField(upload_to='upload',blank=True)
    rating = models.PositiveIntegerField(verbose_name=u'рейтинг', default=0)
    description = models.TextField(verbose_name=u'описание', blank=True)
    date = models.DateField(verbose_name=u'дата загрузки изображения', auto_now_add=True)
