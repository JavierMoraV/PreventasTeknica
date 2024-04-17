from django.contrib import admin
from django.urls import path, include
from usuarios.views import redirect_to_usuarios
#from preventa.views import redirect_to_preventa
from preventa.views import home_preventa


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_usuarios),
    path('preventa/', home_preventa, name='preventa' ),
    path('preventa/', include('preventa.urls')),
]
