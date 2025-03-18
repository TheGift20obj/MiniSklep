from django.shortcuts import render, get_object_or_404, redirect
from .models import Produkt
from .forms import ProduktForm

def lista_produktow(request):
    produkty = Produkt.objects.all()
    return render(request, '../templates/lista_produktow.html', {'produkty': produkty})

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

def usun_wybrane_produkty(request):
    if request.method == 'POST':
        produkt_ids = request.POST.getlist('produkty_do_usuniecia')
        for produkt_id in produkt_ids:
            produkt = get_object_or_404(Produkt, id=produkt_id)
            produkt.delete()
    return redirect('lista_produktow')

def usun_produkt(request, produkt_id):
    produkt = get_object_or_404(Produkt, id=produkt_id)
    produkt.delete()
    return redirect('lista_produktow')