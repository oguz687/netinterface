from django.db import models

from django.db import models


class Egitim(models.Model):
    etiket = models.CharField(max_length=200)
    text=models.TextField()

    def __str__(self):
        return self.etiket


class Tahmin(models.Model):
    # tahmin = models.ForeignKey(Egitim, on_delete=models.CASCADE
    tahmin=models.TextField()
    metin= models.TextField(help_text="Metin giriniz.")
    def __iter__(self):
        return self.tahmin,self.metin

