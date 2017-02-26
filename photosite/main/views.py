from django.contrib import auth
from django.shortcuts import render, HttpResponseRedirect
from django.http import Http404
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import time, datetime


# Create your views here.

def main(request):
    page = 'main'
    guest = 'Гость'
    dude = 'Чувак'
    title = 'Главная'
    return render(request, "index.html", {'guest': guest, 'dude': dude, 'title': title, 'page': page})
