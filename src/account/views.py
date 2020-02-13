from django.http import HttpResponse
from django.shortcuts import render


def smoke(request):
    return HttpResponse('smoke')
