from django import forms
from .models import *


class CategoryForm(forms.ModelForm):
    name = forms.CharField(label='Наименование категории', required=True)
    image = forms.ImageField(label='Картинка категории', required=False)
    description = forms.CharField(label='Описание категории', required=False)
    date = forms.DateField(label='Дата создания категории')

    class Meta:
        model = Categorymodel
        fields = ('name', 'image', 'description')


class CategoryFormChange(forms.ModelForm):
    name = forms.CharField(label='Наименование категории', required=True)
    image = forms.ImageField(label='Картинка категории', required=False)
    description = forms.CharField(label='Описание категории', required=False)

    class Meta:
        model = Categorymodel
        fields = ('name', 'image', 'description')
