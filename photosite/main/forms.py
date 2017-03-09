from django import forms
from .models import *


class CategoryForm(forms.ModelForm):
    name = forms.CharField(label=u'Наименование категории', required=True)
    image = forms.ImageField(label=u'Картинка категории', required=False)
    description = forms.CharField(label=u'Описание категории', required=False)
    date = forms.DateField(label=u'Дата создания категории')

    class Meta:
        model = Categorymodel
        fields = ('name', 'image', 'description')


class CategoryFormChange(forms.ModelForm):
    name = forms.CharField(label=u'Наименование категории', required=True)
    image = forms.ImageField(label=u'Картинка категории', required=False)
    description = forms.CharField(label=u'Описание категории', required=False)

    class Meta:
        model = Categorymodel
        fields = ('name', 'image', 'description')
