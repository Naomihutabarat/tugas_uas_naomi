#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def hitung_luas(self):
        luas = 0.5 * self.alas * self.tinggi
        return luas

alas = float(input("Masukkan panjang alas segitiga: "))
tinggi = float(input("Masukkan tinggi segitiga: "))

segitiga = Segitiga(alas, tinggi)
luas = segitiga.hitung_luas()

print("Luas segitiga dengan alas", alas, "dan tinggi", tinggi, "adalah", luas)

