from django.urls import path

from ProyectowebApp import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    
    path('',views.home,name='Home'),
    path('equipos',views.equipos,name='Equipos'),
    path('calendario',views.calendario,name='Calendario'),
    path('posiciones',views.posiciones,name='Posiciones'),
    path('resultados',views.resultados,name='Resultados'),
    
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
