from django.shortcuts import render
import time

# Create your views here.

def main(request):
    guest = 'Гость'
    dude = 'Чувак'
    return render(request, "index.html",{'guest': guest, 'dude': dude})


def aboutme(request):
    age=time.localtime()[0]-1982
    car = 'почти 18-летний старый Subaru Impreza. :)'
    name = 'Степан'
    return render(request, "aboutme.html",{'age':age, 'car':car,'name':name})


def study(request):
    return render(request, 'study.html')


def work(request):
    return render(request, 'work.html')
