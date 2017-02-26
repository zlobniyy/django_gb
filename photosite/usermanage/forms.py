from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label='Имя',required=False)
    last_name = forms.CharField(label='Фамилия',required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['Имя']
        user.last_name = self.cleaned_data['Фамилия']
        if commit:
            user.save()
        return user
