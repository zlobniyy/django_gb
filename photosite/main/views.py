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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def main1(request):
    page = 'main'
    guest = 'Гость'
    dude = 'Чувак'
    title = 'Главная'
    return render(request, "index.html", {'guest': guest, 'dude': dude, 'title': title, 'page': page})


# def main(request):
#     cats = Categorymodel.objects.all()
#     return render(request, 'index1.html', {'cats': cats})


#
# def admin_page1(request):
#     cats = Categorymodel.objects.all()
#     cat_form = CategoryForm()
#     print(request.GET)
#     # print(cats)
#     # print(str(cat_form.Meta.fields) + str(type(cat_form.name)) + str(type(cat_form.Meta.fields)))
#     return render(request, "admin_page1.html", {'cats': cats, 'form': cat_form})

def admin_cats(request):
    cats = Categorymodel.objects.all()
    form = CategoryFormChange()
    return render(request, 'admin_cats.html', {'cats': cats, 'form': form})


def get_cont_form(request, cat_id):
    """
    Возвращает заполненную форму для редактирования Категории(Categorymodel) с заданным cat_id
    """
    if request.is_ajax():
        cat = get_object_or_404(Categorymodel, id=cat_id)
        cat_form = CategoryFormChange(instance=cat)
        context = {'form': cat_form, 'id': cat_id}
        context.update(csrf(request))
        html = loader.render_to_string('inc-registration_form.html', context)
        data = {'errors': False, 'html': html}
        return JsonResponse(data)
    raise Http404


def create_category(request):
    if request.method == 'POST':
        form = Categorymodel(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin/cats/')
        context = {'form': form}
        return render(request, 'admin_cats.html', context)
    context = {'form': MyRegistrationForm()}
    return render(request, 'admin_cats.html', context)


#################
def admin_category_create(request):
    print('request.POST=' + str(request.POST))
    print('request.FILES=' + str(request.FILES))
    if request.method == 'POST':
        form = CategoryFormChange(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin/cats/')
        context = {'form': form}
        return render(request, 'admin_cat_create.html', context)
    context = {'form': CategoryFormChange()}
    return render(request, 'admin_cat_create.html', context)


def admin_category_delete(request, cat_id):
    category = get_object_or_404(Categorymodel, id=cat_id)
    category.delete()
    return HttpResponseRedirect('/admin/cats/')


def admin_category_update(request, id):
    category = get_object_or_404(Categorymodel, id=id)
    print('request.POST=' + str(request.POST))
    print('request.FILES=' + str(request.FILES))
    if request.method == 'POST':
        # form = GemsForm(request.POST or None, instance=gem)
        form = CategoryFormChange(request.POST, request.FILES, instance=category)
        if form.is_valid():
            category.save()
            return HttpResponseRedirect('/admin/cats/')
        context = {'form': form}
        return render(request, 'admin_cat_update.html', context)
    context = {'form': CategoryFormChange(instance=category)}
    return render(request, 'admin_cat_update.html', context)


def admin_category_detail(request, id):
    cat = get_object_or_404(Categorymodel, id=id)
    return render(request, 'admin_cat_detail.html', {'cat': cat})


def listing(request):
    category_list = Categorymodel.objects.all()
    print('category_list')
    print(category_list)
    # Show 25 objects per page
    paginator = Paginator(category_list, 2)
    print('paginator')
    print(paginator)
    page = request.GET.get('page')
    print('page')
    print(page)
    try:
        categories = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        categories = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        categories = paginator.page(paginator.num_pages)
        print(categories)

    return render(request, 'index1.html', {"categories": categories, 'category_list': category_list})
