# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 15:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobbyname', models.CharField(max_length=200, verbose_name='Хобби')),
                ('hobbylevel', models.PositiveIntegerField(blank=True, verbose_name='Сила увлечения')),
                ('period', models.PositiveIntegerField(default=1, verbose_name='Время работы')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Наименование')),
                ('site', models.URLField(blank=True, verbose_name='Сайт')),
                ('addres', models.CharField(blank=True, max_length=200, verbose_name='Адрес')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Телефон')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Наименование')),
            ],
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course', models.CharField(max_length=160, verbose_name='Курс/Специальность')),
                ('period', models.PositiveIntegerField(default=1, verbose_name='Длительность обучения(месяцов)')),
                ('organization', models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, related_name='Org', to='main.Organization', verbose_name='Наименование учебного учреждения')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Region', verbose_name='Регион')),
                ('site', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.Organization', verbose_name='Сайт')),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('position', models.CharField(max_length=200, verbose_name='Должность')),
                ('duties', models.TextField(verbose_name='Обязанности')),
                ('period', models.PositiveIntegerField(default=1, verbose_name='Время работы')),
                ('organization', models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, related_name='Orga', to='main.Organization', verbose_name='Организация')),
                ('region', models.ForeignKey(default=9999, on_delete=django.db.models.deletion.CASCADE, to='main.Region', verbose_name='Регион')),
                ('site', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.Organization', verbose_name='Сайт')),
            ],
        ),
        migrations.AddField(
            model_name='organization',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Region', verbose_name='Регион'),
        ),
    ]
