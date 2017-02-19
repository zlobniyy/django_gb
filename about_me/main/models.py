from django.db import models


# Create your models here.

class Region(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Наименование', max_length=200, unique=True)


class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Наименование', max_length=200, unique=True)
    region = models.ForeignKey(Region, verbose_name='Регион')
    site = models.URLField(verbose_name='Сайт', blank=True)
    addres = models.CharField(verbose_name='Адрес', blank=True, max_length=200)
    phone = models.CharField(verbose_name='Телефон', blank=True, max_length=20)


class Work(models.Model):
    id = models.AutoField(primary_key=True)
    organization = models.ForeignKey(Organization,related_name='Orga', verbose_name='Организация', max_length=200)
    region = models.ForeignKey(Region, verbose_name='Регион', default=9999)
    site = models.ForeignKey(Organization, verbose_name='Сайт', blank=True)
    position = models.CharField(verbose_name='Должность', max_length=200)
    duties = models.TextField(verbose_name='Обязанности')
    period = models.PositiveIntegerField(verbose_name='Время работы', default=1)


class Study(models.Model):
    id = models.AutoField(primary_key=True)
    organization = models.ForeignKey(Organization,related_name='Org', verbose_name='Наименование учебного учреждения', max_length=200)
    site = models.ForeignKey(Organization, verbose_name='Сайт', blank=True)
    region = models.ForeignKey(Region, verbose_name='Регион')
    course = models.CharField(verbose_name='Курс/Специальность', max_length=160)
    period = models.PositiveIntegerField(verbose_name='Длительность обучения(месяцов)', default=1)


class Aboutme(models.Model):
    hobbyname = models.CharField(verbose_name='Хобби', max_length=200)
    hobbylevel = models.PositiveIntegerField(verbose_name='Сила увлечения', blank=True)
    period = models.PositiveIntegerField(verbose_name='Время работы', default=1)
