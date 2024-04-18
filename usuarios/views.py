from django.shortcuts import render
#from django.shortcuts import redirect


# Create your views here.
def redirect_to_usuarios(request):
    return render(request, 'login.html', {})

