from django.db import models

class Produkt(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.TextField()
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    zdjecie = models.ImageField(upload_to='produkty/', null=True, blank=True)

    def __str__(self):
        return self.nazwa