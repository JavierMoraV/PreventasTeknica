from django.urls import path
from preventa.views import addInfo, home_preventa



urlpatterns = [
    path('addInfo/<int:preventa_id>/', addInfo, name='addInfo'),
    path('', home_preventa, name='preventa' ),
]