from django.shortcuts import render


# Create your views here.

def main(request):
    return render(request, "index.html")


def aboutme(request):
    return render(request, "aboutme.html")


def study(request):
    return render(request, 'study.html')


def work(request):
    return render(request, 'work.html')
