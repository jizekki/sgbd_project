# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import View

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
from datetime import date
from django.contrib import messages
from django.template.defaulttags import register


def home(request):
    context = {
    }
    return render(request, 'html/home.html', context)


def baseModify(request):
    context = {
    }
    return render(request, 'html/baseModify.html', context)


def rencontres(request):
    context = {
    }
    return render(request, 'html/rencontres.html', context)


def clubs(request):
    context = {
    }
    return render(request, 'html/clubs.html', context)


def statistics(request):
    context = {
    }
    return render(request, 'html/statistics.html', context)


@register.filter
def get_item(dictionary, key):
    return dictionary.get(str(key))


def rencontre_details(request):
    student = {
        'prenom': 'Jalal',
        'nom': 'IZEKKI',
        'email': 'jalal.izekki99@gmail.com',
        'telephone': '+33698934757',
    }
    context = {
        'student': student,
    }
    return render(request, 'html/rencontre_details.html', context)


def club_details(request):
    student = {
        'prenom': 'Jalal',
        'nom': 'IZEKKI',
        'email': 'jalal.izekki99@gmail.com',
        'telephone': '+33698934757',
    }
    context = {
        'student': student,
    }
    return render(request, 'html/club_details.html', context)


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels = [
            'A',
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            'H'
        ]
        chartLabel = "Nombre d'étudiants pour trajet"
        chartdata = [3, 7, 5, 2, 20, 30, 45, 9]
        data = {
            "labels": labels,
            "chartLabel": chartLabel,
            "chartdata": chartdata,
        }
        return Response(data)
