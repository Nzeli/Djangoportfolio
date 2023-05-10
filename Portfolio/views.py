from django.shortcuts import render
from django.http import HttpResponse


def thiss(request):
    return render(request, "About.html")
# Create your views here.
