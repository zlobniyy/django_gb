from django import forms
from .models import Imagemodel
from django.utils.timezone import now


class ImageForm(forms.ModelForm):
    name = forms.CharField(label=u'Наименование категории', required=True)
    category = forms.CharField(label=u'Категория', required=True)
    image = forms.ImageField(label=u'Картинка', required=False)
    rating = forms.IntegerField(label = u'Рейтинг', required = False)
    description = forms.CharField(label=u'Описание', required=False)
    date = forms.DateField(label=u'Дата загрузки')

    class Meta:
        model = Imagemodel
        fields = ('name', 'image', 'description','category','rating','date')


# name = models.CharField(verbose_name=u'Название', max_length=32, unique=True)
# category = models.ForeignKey(Categorymodel)
# image = models.ImageField(upload_to='images', blank=True)
# rating = models.PositiveIntegerField(verbose_name=u'рейтинг', default=0)
# description = models.TextField(verbose_name=u'описание', blank=True)
# date = models.DateField(verbose_name=u'дата загрузки изображения', auto_now_add=True)




class ImageFormChange(forms.ModelForm):
    name = forms.CharField(label=u'Наименование категории', required=True)
    category = forms.CharField(label=u'Категория', required=True)
    image = forms.ImageField(label=u'Картинка', required=False)
    rating = forms.IntegerField(label=u'Рейтинг', required=False)
    description = forms.CharField(label=u'Описание', required=False)

    class Meta:
        model = Imagemodel
        fields = ('name', 'image', 'description','category','rating')
