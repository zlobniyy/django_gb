# Generated by Django 2.0.4 on 2018-04-27 07:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20170315_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='author',
            field=models.ForeignKey(default='4', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Categorymodel', verbose_name='Категория'),
        ),
    ]
