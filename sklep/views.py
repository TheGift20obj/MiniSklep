from django.shortcuts import render
from .models import Produkt

def lista_produktow(request):
    produkty = Produkt.objects.all()
    return render(request, 'sklep/lista_produktow.html', {'produkty': produkty})