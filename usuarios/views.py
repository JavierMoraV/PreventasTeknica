from django.shortcuts import render
from django.shortcuts import redirect


def redirect_to_usuarios(request):
    return redirect('login')


def logout(request):
    return render(request, 'registration/logout.html')