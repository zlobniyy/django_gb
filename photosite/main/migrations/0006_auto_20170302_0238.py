# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20170302_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymodel',
            name='image',
            field=models.ImageField(blank=True, upload_to='upload', verbose_name='картинка категории'),
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='image',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
    ]
