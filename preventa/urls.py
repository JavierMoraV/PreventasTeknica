#from django.contrib import admin
from django.urls import path
from preventa.views import addInfo
from preventa.views import ingresar_proyecto

urlpatterns = [
    path('addInfo/', addInfo, name='addInfo'),
    path('ingresar_proyecto/', ingresar_proyecto, name='ingresar_proyecto')
]