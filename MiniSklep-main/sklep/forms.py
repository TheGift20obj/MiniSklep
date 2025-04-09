from django import forms
from .models import Produkt

class ProduktForm(forms.ModelForm):
    class Meta:
        model = Produkt
        fields = ['nazwa', 'opis', 'cena_netto', 'ilosc', 'obrazek']