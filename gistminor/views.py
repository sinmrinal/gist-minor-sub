from django.shortcuts import redirect, render, HttpResponse
from django import forms
from .od import search
from .sms import send
import requests as r


def index(request):
    return render(request, 'layout.html',)


def od(request):
    search_result = {}
    word = request.GET.get('word')
    if word:
        search_result = search(word=word)
    return render(request, 'od.html', {'search_result': search_result})


def sms(request):
    status = ''
    rmessage = ''
    number = request.GET.get('number')
    message = request.GET.get('message')
    if number and message:
        response = send(number, message)
        status = response['status']
        rmessage = response['message']
    return render(request, 'sms.html', {'status': status, 'rmessage': rmessage})
