from django.shortcuts import render,HttpResponse

# Create your views here.



def home(request):
    
 return render(request,"ProyectoWebApp/home.html")

def equipos(request):
    
 return render(request,"ProyectoWebApp/equipos.html")

def calendario(request):
    
 return render(request,"ProyectoWebApp/calendario.html")

def posiciones(request):
    
 return render(request,"ProyectoWebApp/posiciones.html")


def resultados(request):
    
 return render(request,"ProyectoWebApp/resultados.html")











