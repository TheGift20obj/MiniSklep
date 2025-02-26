from django.contrib import admin
from django.urls import path, include
from sklep.views import lista_produktow

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lista_produktow, name='lista_produktow')
]