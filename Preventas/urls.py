from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from preventa.views import home_preventa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls')),
    path('preventa/', home_preventa, name='preventa' ),
    path('preventa/', include('preventa.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),  # URL de inicio de sesión
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # URL de cierre de sesión
]
