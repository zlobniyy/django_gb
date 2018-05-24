from django import forms
from .models import Imagemodel
from usermanage.models import *
from usermanage.forms import UserChangeForm, MyRegistrationForm
from django.utils.timezone import now
from django.contrib import auth


class ImageForm(forms.ModelForm):
    name = forms.CharField(label=u'Наименование картинки', required=True)
    # category = forms.IntegerField(label=u'Категория', required=True)
    image = forms.ImageField(label=u'Картинка', required=False)
    #image_orig = forms.ImageField(label=u'Картинка', required=False)
    rating = forms.IntegerField(label=u'Рейтинг', required=False)
    description = forms.CharField(label=u'Описание', required=False)
    date = forms.DateField(label=u'Дата загрузки')

    class Meta:
        model = Imagemodel
        # fields = ('__all__')
        fields = ('name', 'image', 'description', 'category','image_orig')


class ImageFormChange(forms.ModelForm):
    name = forms.CharField(label=u'Наименование картинки', required=True)
    # category = forms.IntegerField(label=u'Категория', required=True)
    image = forms.ImageField(label=u'Картинка', required=True)
    #image_orig = forms.ImageField(label=u'Картинка', required=True)
    #rating = forms.IntegerField(label=u'Рейтинг', required=False)
    description = forms.CharField(label=u'Описание', required=False)
    #author = forms.ChoiceField(widget=forms.HiddenInput,required=False)

    class Meta:
        model = Imagemodel
        # fields = ('__all__')
        # model.author=auth.get_user
        fields = ('name', 'image', 'description', 'category', 'author')
        #fields = ('name', 'image', 'description', 'category')
