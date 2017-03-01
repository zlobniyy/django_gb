from django.contrib import auth
from django.core.exceptions import ValidationError
from .models import *
from .forms import *
from usermanage.forms import *
from usermanage.models import *
from django.http import Http404, JsonResponse
from django.template import loader
from django.template.context_processors import csrf
from django.contrib.auth.decorators import user_passes_test
import time, datetime
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404



# Create your views here.

def main(request):
    page = 'main'
    guest = 'Гость'
    dude = 'Чувак'
    title = 'Главная'
    return render(request, "index.html", {'guest': guest, 'dude': dude, 'title': title, 'page': page})


def main1(request):
    cats = Categorymodel.objects.all()
    return render(request, 'index1.html', {'cats': cats})


#
# def admin_page1(request):
#     cats = Categorymodel.objects.all()
#     cat_form = CategoryForm()
#     print(request.GET)
#     # print(cats)
#     # print(str(cat_form.Meta.fields) + str(type(cat_form.name)) + str(type(cat_form.Meta.fields)))
#     return render(request, "admin_page1.html", {'cats': cats, 'form': cat_form})

def admin_content(request):
    cats = Categorymodel.objects.all()
    return render(request, 'admin_page1.html', {'cats': cats})


def create_category(request):
    if request.method == 'POST':
        form = Categorymodel(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin1/')
        context = {'form': form}
        return render(request, 'admin_page1.html', context)
    context = {'form': MyRegistrationForm()}
    return render(request, 'admin_page1.html', context)


#################
def admin_category_create(request):
    print(request.POST)
    if request.method == 'POST':
        form = CategoryFormChange(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin1/')
        context = {'form': form}
        return render(request, 'admin_cat_create.html', context)
    context = {'form': CategoryFormChange()}
    return render(request, 'admin_cat_create.html', context)


def admin_category_delete(request, id):
    category = get_object_or_404(Categorymodel, id=id)
    category.delete()
    return HttpResponseRedirect('/admin1/')


def admin_category_update(request, id):
    category = get_object_or_404(Categorymodel, id=id)
    if request.method == 'POST':
        # form = GemsForm(request.POST or None, instance=gem)
        form = CategoryFormChange(request.POST, instance=category)
        if form.is_valid():
            category.save()
            return HttpResponseRedirect('/admin1/')
        context = {'form': form}
        return render(request, 'admin_cat_update.html', context)
    context = {'form': CategoryFormChange(instance=category)}
    return render(request, 'admin_cat_update.html', context)


def admin_category_detail(request, id):
    cat = get_object_or_404(Categorymodel, id=id)
    return render(request, 'admin_cat_detail.html', {'cat': cat})
