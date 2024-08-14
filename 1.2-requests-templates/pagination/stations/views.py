from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator

import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):

    stations = []
    path = settings.BUS_STATION_CSV
    with open(path, newline='', encoding='utf-8') as csvfile:
        data = csv.DictReader(csvfile)
        for station in data:
            stations.append(station)

    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(stations, 10)
    page = paginator.get_page(page_number)

    context = {
        'page': page,
    }
    return render(request, 'stations/index.html', context)
