from django import forms
from .models import Imagemodel
from django.utils.timezone import now


class ImageForm(forms.ModelForm):
    name = forms.CharField(label=u'Наименование картинки', required=True)
    # category = forms.IntegerField(label=u'Категория', required=True)
    image = forms.ImageField(label=u'Картинка', required=False)
    rating = forms.IntegerField(label=u'Рейтинг', required=False)
    description = forms.CharField(label=u'Описание', required=False)
    date = forms.DateField(label=u'Дата загрузки')

    class Meta:
        model = Imagemodel
        #fields = ('__all__')
        fields = ('name', 'image', 'description', 'category' )


class ImageFormChange(forms.ModelForm):
    name = forms.CharField(label=u'Наименование картинки', required=True)
    # category = forms.IntegerField(label=u'Категория', required=True)
    image = forms.ImageField(label=u'Картинка', required=False)
    rating = forms.IntegerField(label=u'Рейтинг', required=False)
    description = forms.CharField(label=u'Описание', required=False)

    class Meta:
        model = Imagemodel
        #fields = ('__all__')
        fields = ('name', 'image', 'description', 'category')
