from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'usuarios'

urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),  # Redirige la URL raíz al inicio de sesión
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Otras URLs específicas de la aplicación usuarios
]