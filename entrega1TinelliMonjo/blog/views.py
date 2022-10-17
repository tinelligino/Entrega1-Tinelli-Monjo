from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Contact,User,Historia


def inicio(request):
    return render(request, "inicio.html")


def info(request):
    return render(request, "info.html")


def experence(request):
    return render(request, "experence.html")


@csrf_exempt
def contact(request):
    if request.method == 'GET':
        context = {"user":[]}
        return render(request, 'contact.html', context)
    if request.method == 'POST':
        nombre = request.POST["nombre"]
        email = request.POST["email"]
        telefono = request.POST["telefono"]
        asunto = request.POST["asunto"]
        descripcion = request.POST["descripcion"]
        User.objects.create( nombre = nombre, email = email, telefono = telefono)
        Contact.objects.create( asunto = asunto, descripcion = descripcion)
        return render(request, 'contact.html')

@csrf_exempt
def historia(request):
    if request.method == 'GET':

        return render(request, 'historia.html')
    if request.method == 'POST':
        nombre = request.POST["nombre"]
        email = request.POST["email"]
        telefono = request.POST["telefono"]
        resumen = request.POST["resumen"]
        descripcion = request.POST["descripcion"]
        User.objects.create( nombre = nombre, email = email, telefono = telefono)
        Historia.objects.create( resumen = resumen, descripcion = descripcion)
        return render(request, 'historia.html')

@csrf_exempt
def buscar(request):
    #print(buscar)
    if request.method == 'GET':
        return render(request, 'contact.html')
    if request.method == 'POST':
        email = request.POST["emailbuscar"]
        #print(email)
        lista = User.objects.filter(email = f'{email}')
        #print(lista)
        if len(lista) == 0:
            return render(request, 'contact.html')
        else:
            context = {"user":lista.first()}
            print(context)
            return render(request, 'contact.html',context)