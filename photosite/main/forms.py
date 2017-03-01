from django import forms
from main.models import *

class MyCatecoryForm():
    name = forms.CharField(label='Наименование категории',required=True)
    pic = forms.ImageField(label='Картинка категории',required=True)

    class Meta:
        model = Category
        fields = ('name', 'pic')

    # def save(self, commit=True):
    #     cat = super(MyCatecoryForm, self).save(commit=False)
    #     cat.name = self.cleaned_data['name']
    #     cat.pic = self.cleaned_data['pic']
    #     if commit:
    #         cat.save()
    #     return cat