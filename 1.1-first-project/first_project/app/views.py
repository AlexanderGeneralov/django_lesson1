from django.http import HttpResponse
from django.shortcuts import render, reverse

import os
import datetime


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.datetime.now().time()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    list_dir = os.listdir('C:\\Users\\Александр\\Desktop\\programming\\django_lesson1\\dj-homeworks\\1.1-first-project\\first_project\\app')
    msg = f"Содержимое текущего каталога: {list_dir}"
    return HttpResponse(msg)

def hello_view(request):
    name = request.GET.get('name')
    age = int(request.GET.get('age', 20))
    print(age)
    return HttpResponse(f"Hello, {name}, from django!")


def summ(requeset, op1, op2):
    res = op1 + op2
    return HttpResponse(f"summ = {res}")
