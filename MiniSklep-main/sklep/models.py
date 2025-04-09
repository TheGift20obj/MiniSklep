from django.db import models
from decimal import Decimal

class Produkt(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.TextField()
    cena_netto = models.DecimalField(max_digits=10, decimal_places=2)
    cena_brutto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ilosc = models.PositiveIntegerField(default=0)  # ilość produktów na magazynie
    obrazek = models.ImageField(upload_to='', null=True, blank=True)

    def __str__(self):
        return self.nazwa

    def save(self, *args, **kwargs):
        # Automatyczne obliczanie ceny brutto na podstawie ceny netto i VAT (np. 23%)
        if self.cena_brutto is None or self.cena_brutto == 0:
            self.cena_brutto = self.cena_netto * Decimal('1.23')
        super().save(*args, **kwargs)