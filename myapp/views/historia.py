from django.shortcuts import render, redirect
import requests

def historia(request):
    return render(request, 'historia.html')

