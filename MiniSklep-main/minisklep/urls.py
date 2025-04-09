from django.contrib import admin
from django.urls import path, include
from sklep import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista_produktow, name='lista_produktow'),  # Lista produktów
    path('_edit', views.lista_produktow_edit, name='lista_produktow_edit'),
    path('login/', views.login_view, name='login'),  # Logowanie
    path('logout/', views.logout_view, name='logout'),
    path('dodaj/', views.dodaj_edycja_produkt, name='dodaj_edycja_produkt'),  # Dodaj nowy produkt
    path('edycja/<int:produkt_id>/', views.dodaj_edycja_produkt, name='dodaj_edycja_produkt'),  # Edytuj produkt
    path('usun/<int:produkt_id>/', views.usun_produkt, name='usun_produkt'),  # Usuń produkt
    path('usun_wybrane/', views.usun_wybrane_produkty, name='usun_wybrane_produkty'),
]