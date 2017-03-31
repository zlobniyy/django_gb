"""photosite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from main.views import *
from usermanage.views import *
from content.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^$', main, name='main'),
    # url(r'^main/$', main, name='main'),
    url(r'^$', listing, name='list'),
    url(r'^main/$', listing, name='list'),
    url(r'oops/$',oops,name='oops'),
    url(r'test',test,name='test'),
]

urlpatterns += [
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^registration/$', registration, name='registration'),
    url(r'^admin/$', admin_page, name='admin_users'),
    url(r'^admin/delete/user/(\d+)$', delete_user),
    url(r'^admin/get_user_form/(\d+)$', get_user_form),
    url(r'^admin/create/user/(\d*)$', create_user),
]

urlpatterns += [
                   # categories
                   url(r'admin/cats/$', admin_cats, name='admin_cats'),
                   url(r'^admin/cats/get_cont_form/(\d+)$', get_cont_form, name='get_cont_form'),
                   url(r'^admin/cats/create/category/$', admin_category_create, name='admin_category_create'),
                   url(r'^admin/cats/delete/category/(\d+)$', admin_category_delete, name='admin_category_delete'),
                   url(r'^admin/cats/update/category/(\d+)$', admin_category_update, name='admin_category_update'),
                   url(r'^admin/cats/detail/category/(\d+)$', admin_category_detail, name='admin_category_detail'),
                   # images
                   url(r'list/(\d*)/$', listimg, name='listimg'),
                   url(r'lists/$', images_list, name='images_list'),

                   # url(r'^admin/img/get_cont_form/(\d+)$', get_cont_form, name='get_cont_form'),
                   url(r'^admin/img/create/$', admin_image_create, name='admin_image_create'),
                   url(r'^list/img/create/$', album_image_create, name='album_image_create'),
                   url(r'^list/(\d+)/img/delete/(\d+)$', album_image_delete, name='album_image_delete'),
                   # url(r'^admin/img/delete/category/(\d+)$', admin_image_delete, name='admin_image_delete'),
                   # url(r'^admin/img/update/category/(\d+)$', admin_image_update, name='admin_image_update'),
                   # url(r'^admin/img/detail/category/(\d+)$', admin_image_detail, name='admin_image_detail'),

               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
