#!/usr/bin/env python
# coding: utf-8

# In[1]:


class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        luas = self.panjang * self.lebar
        return luas

panjang = float(input("Masukkan panjang persegi panjang: "))
lebar = float(input("Masukkan lebar persegi panjang: "))

persegi_panjang = PersegiPanjang(panjang, lebar)
luas = persegi_panjang.hitung_luas()

print("Luas persegi panjang dengan panjang", panjang, "dan lebar", lebar, "adalah", luas)

