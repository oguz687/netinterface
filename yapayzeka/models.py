from django.db import models
import sys
import os
PATH=""
sys.path += [os.path.abspath(r'/home/atessu/PycharmProjects/otomasyon')]

from django.db import models
from yapayzekacore import Yapayzeka


class Egitim(models.Model):
    etiket = models.CharField(max_length=200)
    text=models.TextField()

    def __str__(self):
        return self.etiket

class Tahmin(models.Model):
    # tahmin = models.ForeignKey(Egitim, on_delete=models.CASCADE
    tahmin = models.TextField(blank=True)
    metin = models.TextField(help_text="Metin giriniz.")
    beklenen = models.TextField(blank=True)


    def save(self, *args,**kwargs):
        orn=Yapayzeka()
        self.tahmin=orn.predict_from_model(self.metin)
        super(Tahmin,self).save(self,*args,**kwargs)

    def deneme(self):
        return tuple((self.metin,self.tahmin))
