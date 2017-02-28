from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name='Наименование категории',max_length=200)
    #pic= models.ImageField
    date = models.DateField(verbose_name='Дата создания категории', auto_now_add=True)
