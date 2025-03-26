from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Produkt
from .forms import ProduktForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Poprawnie logujemy użytkownika
            return redirect('lista_produktow')  # Przekierowanie po udanym logowaniu
        else:
            # Dodajemy tutaj jakiś komunikat błędu, jeśli uwierzytelnienie się nie uda
            return render(request, 'login.html', {'error': 'Niepoprawny login lub hasło'})
    return render(request, 'login.html')


def logout_view(request):
    auth_logout(request)  # Poprawnie wylogowujemy użytkownika
    return redirect('login')  # Możesz przekierować na stronę logowania po wylogowaniu

@login_required(login_url='login')
def lista_produktow(request):
    produkty = Produkt.objects.all()
    return render(request, '../templates/lista_produktow.html', {'produkty': produkty})

@login_required(login_url='login')
def dodaj_edycja_produkt(request, produkt_id=None):
    if produkt_id:
        produkt = get_object_or_404(Produkt, id=produkt_id)
    else:
        produkt = None

    if request.method == 'POST':
        form = ProduktForm(request.POST, request.FILES, instance=produkt)
        if form.is_valid():
            form.save()
            return redirect('lista_produktow')
    else:
        form = ProduktForm(instance=produkt)

    return render(request, '../templates/dodaj_edycja_produkt.html', {'form': form, 'produkt': produkt})

@login_required(login_url='login')
def usun_wybrane_produkty(request):
    if request.method == 'POST':
        produkt_ids = request.POST.getlist('produkty_do_usuniecia')
        for produkt_id in produkt_ids:
            produkt = get_object_or_404(Produkt, id=produkt_id)
            produkt.delete()
    return redirect('lista_produktow')

@login_required(login_url='login')
def usun_produkt(request, produkt_id):
    produkt = get_object_or_404(Produkt, id=produkt_id)
    produkt.delete()
    return redirect('lista_produktow')