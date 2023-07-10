#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Trapesium:
    def __init__(self, alas, atas, tinggi):
        self.alas = alas
        self.atas = atas
        self.tinggi = tinggi

    def hitung_luas(self):
        luas = 0.5 * (self.alas + self.atas) * self.tinggi
        return luas

alas = float(input("Masukkan panjang alas trapesium: "))
atas = float(input("Masukkan panjang atas trapesium: "))
tinggi = float(input("Masukkan tinggi trapesium: "))

if alas > 0 and atas > 0 and tinggi > 0:
    trapesium = Trapesium(alas, atas, tinggi)
    luas = trapesium.hitung_luas()

    print("Luas trapesium dengan alas", alas, ", atas", atas, ", dan tinggi", tinggi, "adalah", luas)
else:
    print("Masukkan nilai yang valid (nilai harus lebih besar dari 0) untuk alas, atas, dan tinggi trapesium.")

