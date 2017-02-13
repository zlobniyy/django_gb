from django.db import models


# Create your models here.

class Work(models.Model):
    organization = models.CharField(verbose_name='Организация', max_length=32)
    region = models.CharField(verbose_name='Регион', max_length=32, blank=True)
    site = models.CharField(verbose_name='Сайт', max_length=64, blank=True)
    position = models.CharField(verbose_name='Должность', max_length=16)
    duties = models.TextField(verbose_name='Обязанности')
    period = models.PositiveIntegerField(verbose_name='Время работы', default=1)


class Study(models.Model):
    schools = models.CharField(verbose_name='Наименование учебного учреждения', max_length=32)
    site = models.CharField(verbose_name='Сайт Учреждения', max_length=64, blank=True)
    course = models.CharField(verbose_name='Курс/Специальность', max_length=16)
    period = models.PositiveIntegerField(verbose_name='Длительность обучения(месяцов)', default=0)


class Aboutme(models.Model):
    hobbyname = models.CharField(verbose_name='Хобби', max_length=32)
    region = models.CharField(verbose_name='Регион', max_length=32, blank=True)
    site = models.CharField(verbose_name='Образцы работ', max_length=64, blank=True)
    hobbylevel = models.CharField(verbose_name='Сила увлечения', max_length=16)
