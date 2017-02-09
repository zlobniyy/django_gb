from django.shortcuts import render
import time, datetime


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
    return render(request, "aboutme.html", {'age': age, 'car': car, 'name': name, 'title': title, 'page': page, 'wasborn':wasborn})


def study(request):
    page = 'study'
    schools = ['Высшее техническое образование по автоматизации проектирования в машиностроении',
               'Курсы Oracle DBA level 1&2', 'Курс Oracle SQL Tuning',
               'Linux(Debian-family)', 'Unix Solaris', 'Shell',
               'Так как последние пару лет работал в сопровождении банка, то бухучет знаком',
               'HTML/CSS+Bootstrap(курс GeekBrains)', 'JS(курс на GeekBrains в процессе)',
               'Python(курс на GeekBrains в процессе)', 'В общении с людьми не испытваю проблем'] or ['Видимо я ничего не умею 0_о']
    title = 'Учеба'
    return render(request, 'study.html', {'schools': schools, 'title': title, 'page': page})


def work(request):
    page = 'work'
    works = ['Вожатый', 'Мастер починки сотовых телефонов',
             'Эникейщик',
             'Сисадмин',
             'Инженер прикладного сопровождения',
             'Прикладной администратор',
             'Фотограф на соревноваяних RDS Сибирь.'] or ['Здесь пока ничего нет']


    title = 'Работа'
    return render(request, 'work.html', {'works': works, 'title': title, 'page': page})
