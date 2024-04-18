#from django.contrib import admin
from django.urls import path
from preventa.views import addInfo
#from preventa.views import ingresar_proyecto

urlpatterns = [
    path('addInfo/<int:preventa_id>/', addInfo, name='addInfo'),
    
]