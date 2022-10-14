from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')

def info(request):
    return render(request, 'info.html')

def experence(request):
    return render(request, 'experence.html')