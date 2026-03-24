from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')

def persona(request):
    return render(request, 'persona.html')

def propietario(request):
    return render(request, 'propietario.html')