#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Balok:
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def hitung_luas(self):
        luas_permukaan = 2 * (self.panjang * self.lebar + self.panjang * self.tinggi + self.lebar * self.tinggi)
        return luas_permukaan

panjang = float(input("Masukkan panjang balok: "))
lebar = float(input("Masukkan lebar balok: "))
tinggi = float(input("Masukkan tinggi balok: "))

if panjang > 0 and lebar > 0 and tinggi > 0:
    balok = Balok(panjang, lebar, tinggi)
    luas_permukaan = balok.hitung_luas()

    print("Luas permukaan balok dengan panjang", panjang, ", lebar", lebar, ", dan tinggi", tinggi, "adalah", luas_permukaan)
else:
    print("Masukkan nilai yang valid (nilai harus lebih besar dari 0) untuk panjang, lebar, dan tinggi balok.")

