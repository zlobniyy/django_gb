from django.shortcuts import render
import time, datetime
from main.models import Work
from main.models import Study
from main.models import Aboutme


# Create your views here.

def main(request):
    page = 'main'
    guest = 'Гость'
    dude = 'Чувак'
    title = 'Главная'
    return render(request, "index.html", {'guest': guest, 'dude': dude, 'title': title, 'page': page})


def aboutme(request):
    page = 'aboutme'
    age = time.localtime()[0] - 1982
    wasborn = datetime.date(1982, 9, 9)
    car = 'почти 18-летний старый Subaru Impreza. :)'
    name = 'Степан'
    title = 'Обо мне'
    hobby_list = Aboutme.objects.all() or ['Я ничем не увлекаюсьобожешьмой 0_о']
    return render(request, "aboutme.html", {'age': age,
                                            'car': car,
                                            'name': name,
                                            'title': title,
                                            'page': page,
                                            'wasborn': wasborn,
                                            'hobbys': hobby_list})


def study(request):
    page = 'study'
    schools_list = Study.objects.all() or ['Видимо я ничего не умею 0_о']
    title = 'Учеба'
    return render(request, 'study.html',
                  # {'schools': [study.schools + " - " + study.course for study in schools_list], 'title': title,
                  {'schools': schools_list,
                   'title': title,
                   'page': page})


def work(request):
    page = 'work'
    works_list = Work.objects.all() or ['Здесь пока ничего нет']

    title = 'Работа'
    return render(request, 'work.html',
                  # {'works': [work.organization + " - " + work.position for work in works_list], 'title': title,
                  {'works': works_list, 'title': title,
                   'page': page})
