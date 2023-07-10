#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

class Lingkaran:
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def hitung_luas(self):
        luas = math.pi * self.jari_jari ** 2
        return luas

jari_jari = float(input("Masukkan jari-jari lingkaran: "))
lingkaran = Lingkaran(jari_jari)
luas = lingkaran.hitung_luas()
print("Luas lingkaran dengan jari-jari", jari_jari, "adalah", luas)

