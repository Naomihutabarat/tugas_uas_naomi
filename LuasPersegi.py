#!/usr/bin/env python
# coding: utf-8

# In[5]:


class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_luas(self):
        luas = self.sisi * self.sisi
        return luas

sisi = float(input("Masukkan panjang sisi persegi: "))
persegi = Persegi(sisi)
luas = persegi.hitung_luas()
print("Luas persegi dengan sisi", sisi, "adalah", luas)

