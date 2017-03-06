from django.contrib import auth
from django.core.exceptions import ValidationError
from .forms import MyRegistrationForm
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User
from usermanage.forms import MyRegistrationForm, UserChangeForm
from django.http import Http404, JsonResponse
from django.template import loader
from django.template.context_processors import csrf
from django.contrib.auth.decorators import user_passes_test
import time, datetime


# Create your views here.


def login(request):
    if request.method == 'POST':
        print("POST data =", request.POST)
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect("/")
        else:
            print('user not logged.')
            mess = 'Неверный логин/пароль.'
            return render(request, 'index_old.html', {'username': username, 'errors': True, 'mess': mess})
    raise Http404


def logout(request):
    print(request)
    print(request.POST)
    print(request.GET)
    auth.logout(request)
    return HttpResponseRedirect("/")


def registration_low(request):
    if request.method == 'POST':
        errors = {}  # Тут будем хранить ошибки, чтобы отобразить на странице
        username = request.POST.get('name')
        email = request.POST.get('email')
        email2 = request.POST.get('confirm_email')
        password = request.POST.get('password')
        password2 = request.POST.get('confirm_password')
        print(request.POST)
        # Validate data
        if email != email2:
            errors['email'] = 'does not match'
        if password != password2:
            errors['password'] = 'does not match'
        user = User(username=username, email=email)
        # Пароли хранятся в виде хэшей, поэтому их нельзя передавать напрямую
        user.set_password(password)
        # Проверяем, существует ли пользователь с таким именем
        try:
            user.validate_unique()
        except ValidationError as er:
            errors.update(er.message_dict)
        # Если есть ошибки, передаем их в контексте шаблону, который умеет их отображать
        if errors:
            return render(request, 'registration_low.html', {'reg_errors': errors})
        # Если ошибок нет, сохраняем пользователя в базе, перенаправляем на главную
        user.save()
        return HttpResponseRedirect("/")
    return render(request, 'registration_low.html')


def registration(request):
    print(request)
    print(request.POST)
    print(request.GET)
    page = 'registration'
    title = 'Регистрация'
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        context = {'form': form}
        return render(request, 'registration.html', context)
    context = {'form': MyRegistrationForm()}
    print(page, title)
    return render(request, 'registration.html', context)

# here admin-side
def admin_page(request):
    # TODO: сделать доступ у админке только суперпользователю
    users = User.objects.all()
    return render(request, 'admin_page.html', {'users': users})


# def delete_user(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     user.delete()
#     return HttpResponseRedirect('/admin')
#
#     if request.is_ajax():
#         if not user_id:
#             user = User(request.POST)
#         else:
#             user = get_object_or_404(User, id=user_id)
#             user = MyRegistrationForm(request.POST or None, instance=user)
#         if user.is_valid():
#             user.save()
#             users = User.objects.all()
#             html = loader.render_to_string('users_list.html', {'users': users}, request=request)
#             data = {'errors': False, 'html': html}
#             return JsonResponse(data)
#         else:
#             errors = user.errors.as_json()
#             return JsonResponse({'errors': errors})
#     raise Http404


# def get_user_form(request, user_id):
#     """
#     Возвращает заполненную форму для редактирования Пользователя(User) с заданным user_id
#     """
#     if request.is_ajax():
#         user = get_object_or_404(User, id=user_id)
#         user_form = MyRegistrationForm(instance=user)
#         context = {'form': user_form, 'id': user_id}
#         context.update(csrf(request))
#         html = loader.render_to_string('inc-registration_form.html', context)
#         data = {'errors': False, 'html': html}
#         return JsonResponse(data)
#     raise Http404

@user_passes_test(lambda user: user.is_superuser, login_url='/main/')
def admin_page(request):
    users = User.objects.all()
    user_form = MyRegistrationForm()

    return render(request, 'admin_page.html', {'users': users, 'form': user_form})

@user_passes_test(lambda user: user.is_superuser, login_url='/main/')
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return HttpResponseRedirect('/admin')

@user_passes_test(lambda user: user.is_superuser, login_url='/main/')
def get_user_form(request, user_id):
    """
    Возвращает заполненную форму для редактирования Пользователя(User) с заданным user_id
    """
    if request.is_ajax():
        user = get_object_or_404(User, id=user_id)
        user_form = MyRegistrationForm(instance=user)
        context = {'form': user_form, 'id': user_id}
        context.update(csrf(request))
        html = loader.render_to_string('inc-registration_form.html', context)
        data = {'errors': False, 'html': html}
        return JsonResponse(data)
    raise Http404

@user_passes_test(lambda user: user.is_superuser, login_url='/main/')
def create_user(request, user_id=None):
    """
    Создает Пользователя(User)
    Или редактирует существующего, если указан  user_id
    """
    if request.is_ajax():
        print('user_id = ', user_id)
        if not user_id:
            print('Not user_id')
            # user = User(request.POST)
            user_form = MyRegistrationForm(request.POST)
        else:
            user = get_object_or_404(User, id=user_id)
            user_form = UserChangeForm(request.POST or None, instance=user)
            print('Edited' + str(user_id))
        if user_form.is_valid():
            user_form.save()
            users = User.objects.all()
            html = loader.render_to_string('inc-users_list.html', {'users': users}, request=request)
            data = {'errors': False, 'html': html}
            return JsonResponse(data)
        else:
            errors = user_form.errors.as_json()
            return JsonResponse({'errors': errors})

    raise Http404
