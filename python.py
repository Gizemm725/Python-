import random

# Asal sayıyı kontrol eden fonksiyon
def asal_mi(sayi):
    if sayi < 2:
        return False 
    for i in range(2, int(sayi**0.5) + 1):  # Performansı artırmak için kökünü alıyoruz
        if sayi % i == 0:
            return False  
    return True  

# Rastgele sayı üreten fonksiyon
def rastgele_sayi_uret(min_deger, max_deger):
    return random.randint(min_deger, max_deger)  

# Oyuncunun sırasını yöneten fonksiyon
def kisi_fonksiyonu(isim):
    piyon = 0
    
    while piyon < 100:  
        zar = rastgele_sayi_uret(1, 6)
        eski_piyon = piyon
        piyon += zar
        print(f"{isim}'ın sırası: {isim} {zar} attı. {eski_piyon}. Kareden {piyon}. Kareye ilerledi.")

        # 5'in katı olan karede geri gitme durumu
        if piyon % 5 == 0:
            eski_piyon = piyon
            piyon = max(0, piyon - 3)  
            print(f"İlerlediği kare 5’in katı olduğu için {isim}, {eski_piyon}. kareden {piyon}. kareye geriledi.")
        
        # Asal karede ekstra zar atma durumu
        if asal_mi(piyon):
            rand2 = rastgele_sayi_uret(1, 6)
            piyon += rand2
            print(f"{isim}, asal bir kareye geldiği için {rand2} kare daha ilerledi. Yeni konumu: {piyon}. kare")
        
        # Oyun bitiş durumu
        if piyon >= 100:
            print(f"{isim} OYUNU BİRİNCİ TAMAMLADI.")
            break

# Oyuncuları sırayla başlat
kisi_fonksiyonu("Aslı")
kisi_fonksiyonu("Barış")
kisi_fonksiyonu("Ceyda")
kisi_fonksiyonu("Deniz")
