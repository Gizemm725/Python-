# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 14:26:59 2025

@author: user
"""
import random

def asal_mi(sayi):  
    if sayi < 2:
        return False 
    for i in range(2, sayi):  
        if sayi % i == 0:
            return False  
    return True  

def rastgele_sayi_uret(min_deger, max_deger):
    return random.randint(min_deger, max_deger)  

def kisi_fonksiyonu(oyuncular):
    piyonlar = {oyuncu: 0 for oyuncu in oyuncular}  
    oyun_bitti = False  

    while not oyun_bitti:
        for oyuncu in oyuncular:  
            eski_pozisyon = piyonlar[oyuncu]  
            zar = rastgele_sayi_uret(1, 6) 
            piyonlar[oyuncu] += zar 

            yeni_pozisyon = piyonlar[oyuncu]

            if yeni_pozisyon >= 100:  
                print("{} OYUNU BİRİNCİ TAMAMLADI.".format(oyuncu))
                oyun_bitti = True
                break

            print("{} {} attı. {}. kareden {}. kareye ilerledi.".format(oyuncu, zar, eski_pozisyon, yeni_pozisyon))

           
            if yeni_pozisyon % 5 == 0:
                eski_piyon = yeni_pozisyon
                piyonlar[oyuncu] -= 3  
                if piyonlar[oyuncu] < 0:
                    piyonlar[oyuncu] = 0  

                print("{} 5’in katına geldiği için 3 kare geriye gitti. {}. kareden {}. kareye geriledi.".format(oyuncu, eski_piyon, piyonlar[oyuncu]))

          
            if asal_mi(piyonlar[oyuncu]):
                rand2 = rastgele_sayi_uret(1, 6)
                eski_pozisyon = piyonlar[oyuncu]
                piyonlar[oyuncu] += rand2
                print("{} asal bir kareye geldiği için {} kare daha ilerledi. Yeni konumu: {}. kare".format(oyuncu, rand2, piyonlar[oyuncu]))


oyuncular = ["Aslı", "Ceyda", "Barış", "Deniz"]
kisi_fonksiyonu(oyuncular)
