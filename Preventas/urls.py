from django.contrib import admin
from django.urls import path
from usuarios.views import redirect_to_usuarios
from preventa.views import redirect_to_preventa
from preventa.views import addInfo
from preventa.views import ingresar_proyecto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_usuarios),
    path('preventa/',redirect_to_preventa, name='preventa' ),
    path('addInfo/', addInfo, name='addInfo'),
    path('ingresar_proyecto/', ingresar_proyecto, name='ingresar_proyecto'),
]
