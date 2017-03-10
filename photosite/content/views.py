from django.contrib import auth
from django.core.exceptions import ValidationError
from .models import *
from .forms import *
from usermanage.forms import *
from usermanage.models import *
from main.forms import *
from main.models import *
from django.http import Http404, JsonResponse
from django.template import loader
from django.template.context_processors import csrf
from django.contrib.auth.decorators import user_passes_test
import time, datetime
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

# @user_passes_test(lambda user: user.is_superuser, login_url='/main/')
def images_list(request):
    imagelist = Imagemodel.objects.all()
    form = ImageForm()
    return render(request, 'admin_images.html', {'imagelist': imagelist, 'form': form})


# List of items + Paginator
def listimg(request, id):
    title=get_object_or_404(Categorymodel,id=id)
    image_list = Imagemodel.objects.filter(category_id=id)
    paginator = Paginator(image_list, 4)
    page = request.GET.get('page')
    try:
        imagelist = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        imagelist = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        imagelist = paginator.page(paginator.num_pages)

    return render(request, 'album.html',
                  {"imagelist": imagelist, 'image_list': image_list, 'page': page,'title':title})


def admin_image_create(request):
    title = 'Добавить картинку'
    if request.method == 'POST':
        form = ImageFormChange(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin/lists/')
        context = {'form': form}
        return render(request, 'admin_image_create.html', context, {'title': title})
    context = {'form': ImageFormChange()}
    return render(request, 'admin_image_create.html', context, {'title': title})
