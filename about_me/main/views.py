from django.shortcuts import render
import time

# Create your views here.

def main(request):
    page = 'main'
    guest = 'Гость'
    dude = 'Чувак'
    title = 'Главная'
    return render(request, "index.html",{'guest': guest, 'dude': dude,'title':title,'page':page })


def aboutme(request):
    page = 'aboutme'
    age=time.localtime()[0]-1982
    car = 'почти 18-летний старый Subaru Impreza. :)'
    name = 'Степан'
    title = 'Обо мне'
    return render(request, "aboutme.html",{'age':age, 'car':car,'name':name,'title':title,'page':page })


def study(request):
    page = 'study'
    schools=['высшее техническое образование по автоматизации проектирования в машиностроении',
             'курсы Oracle DBA level 1&2','курс Oracle SQL Tuning',
             'Linux(Debian-family), Unix Solaris, Shell',
             'Так как последние пару лет работал в сопровождении банка, то бухучет знаком',
             'HTML/CSS+Bootstrap(курс GeekBrains)','JS(курс на GeekBrains в процессе)',
             'Python(курс на GeekBrains в процессе)','В общении с людьми не испытваю проблем']
    title = 'Учеба'
    return render(request, 'study.html',{'schools':schools,'title':title,'page':page })


def work(request):
    page='work'
    works=['Вожатый','Мастер починки сотовых телефонов',
                            'Сисадмин',
                            'Эникейщик',
                            'Инженер прикладного сопровождения',
                            'Прикладной администратор',
                            'Фотограф на соревноваяних RDS Сибирь.']
    title = 'Работа'
    return render(request, 'work.html',{'works':works,'title':title,'page':page })
