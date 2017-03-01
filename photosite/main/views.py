from django.contrib import auth
from django.core.exceptions import ValidationError
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .models import *
from .forms import *
from django.http import Http404, JsonResponse
from django.template import loader
from django.template.context_processors import csrf
from django.contrib.auth.decorators import user_passes_test
import time, datetime


# Create your views here.

def main(request):
    page = 'main'
    guest = 'Гость'
    dude = 'Чувак'
    title = 'Главная'
    return render(request, "index.html", {'guest': guest, 'dude': dude, 'title': title, 'page': page})


def main1(request):
    cats = Category.objects.all()
    return render(request, 'index1.html', {'cats': cats})


def admin_page1(request):
    cats = Category.objects.all()
    cat_form = MyCatecoryForm()
    print(request.GET)
    # print(cats)
    # print(str(cat_form.Meta.fields) + str(type(cat_form.name)) + str(type(cat_form.Meta.fields)))
    return render(request, "admin_page1.html", {'cats': cats, 'form': cat_form})
