from django.db import models


class Organization(models.Model):
    name = models.CharField(verbose_name='Название', max_length=32, unique=True)
    region = models.CharField(verbose_name='Регион', max_length=32, blank=True)
    tax_id = models.PositiveIntegerField(verbose_name='Регистрационный номер')
    site = models.URLField(verbose_name='Сайт', blank=True)


class Work(models.Model):
    organization = models.ForeignKey(Organization, verbose_name='Организация')
    position = models.CharField(verbose_name='Должность', max_length=32)
    duties = models.TextField(verbose_name='Обязанности')
    period = models.PositiveIntegerField(verbose_name='Период, мес')


class Hobby(models.Model):
    name = models.CharField(verbose_name='Название', max_length=32)
    #image = models.ImageField(upload_to='hobby')


class Study(models.Model):
    name = models.CharField(verbose_name='Название', max_length=64)
    type = models.CharField(verbose_name='Тип', max_length=64)
    number = models.PositiveIntegerField(verbose_name='Номер')
    study_from = models.DateField(verbose_name='Дата начала обучения')
    study_to = models.DateField(verbose_name='Дата окончания обучения')
