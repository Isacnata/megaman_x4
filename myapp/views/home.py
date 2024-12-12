from django.shortcuts import render, redirect
import requests

def index(request):
    return render(request, 'index.html')

