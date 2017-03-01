from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Category name',max_length=200)
    pic= models.ImageField(verbose_name='Category pic',upload_to='upload/',height_field=250,width_field=375)
    date = models.DateField(verbose_name='Category creation date', auto_now_add=True)
