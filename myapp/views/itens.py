from django.shortcuts import render, redirect
import requests

def itens(request):
    return render(request, 'itens.html')