from django.shortcuts import render
import datetime
from .models import Work, Hobby


def main(request):
    title = "Главная"
    fistname = "евгений"
    lastname = "пухов"
    title = "Главная"
    birthday = datetime.date(day=11, month=11, year=1980)
    city = "Курган"
    return render(request, "index.html",
                  {
                      'title': title,
                      'fistname': fistname,
                      'lastname': lastname,
                      'birthday': birthday,
                      'city': city,
                  }
                  )


def works(request):
    title = "Работы"
    page = "works"
    work_places = Work.objects.all()
    return render(request, "works.html",
                  {
                      'title': title,
                      'page': page,
                      'work_places': work_places,
                  }
                  )
    # return render(request, "works.html", {'page': 'works'})


def learn(request):
    title = "Главная"
    page = "learns"
    learns = {
        "date_start": datetime.date(year=1997, month=9, day=1),
        "date_end": datetime.date(year=2002, month=6, day=25),
    }
    return render(request, "learn.html",
                  {
                      'title': title,
                      'page': page,
                      'learns': learns,
                  }
                  )


def hobby(request):
    title = "Хобби"
    page = "hobby"
    hobbies = Hobby.objects.all()
    return render(request, "hobby.html",
                  {
                      'title': title,
                      'page': page,
                      'hobbies': hobbies,
                  }
                  )
