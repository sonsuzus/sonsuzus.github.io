---
title: Küp şeklinde satranç ve vezirler
author: sonsuz
date: 2025-03-02 19:00:41 +0300
categories: [Program,Algoritma]
tags: [soru,satranç,programlama,python,kontrol,zeka,3d]
image: 8x8x8-satranc.jpg
---

Elimizde 8x8x8 lik bir satranç kübü var. Bu tahtaya birbirini yemeyen maksimum kaç vezir yerleştirilir? (Vezirler derinlemesine de hareket edebilmektedir)

Aşağıdaki program vezirlerinizi sırayla koyduktan sonra tahtanızı ve boş yerleri gösterecektir.

```py
import numpy as np

def vezir_hareketleri(tahta, x, y, z):
    # (Önceki kodların aynısı)
    """
    Üç boyutlu satranç tahtasında vezirin hareketlerini işaretler.
    """
    # Vezirin bulunduğu konumu 2 olarak işaretle
    tahta[x, y, z] = 2

    # Vezirin yatay ve dikey hareketleri
    for i in range(8):
        if i != x:
            tahta[i, y, z] = 1
        if i != y:
            tahta[x, i, z] = 1
        if i != z:
            tahta[x, y, i] = 1

    # Vezirin çapraz hareketleri (xy düzlemi)
    for i in range(1, 8):
        if x + i < 8 and y + i < 8:
            tahta[x + i, y + i, z] = 1
        if x - i >= 0 and y - i >= 0:
            tahta[x - i, y - i, z] = 1
        if x + i < 8 and y - i >= 0:
            tahta[x + i, y - i, z] = 1
        if x - i >= 0 and y + i < 8:
            tahta[x - i, y + i, z] = 1

    # Vezirin çapraz hareketleri (xz düzlemi)
    for i in range(1, 8):
        if x + i < 8 and z + i < 8:
            tahta[x + i, y, z + i] = 1
        if x - i >= 0 and z - i >= 0:
            tahta[x - i, y, z - i] = 1
        if x + i < 8 and z - i >= 0:
            tahta[x + i, y, z - i] = 1
        if x - i >= 0 and z + i < 8:
            tahta[x - i, y, z + i] = 1

    # Vezirin çapraz hareketleri (yz düzlemi)
    for i in range(1, 8):
        if y + i < 8 and z + i < 8:
            tahta[x, y + i, z + i] = 1
        if y - i >= 0 and z - i >= 0:
            tahta[x, y - i, z - i] = 1
        if y + i < 8 and z - i >= 0:
            tahta[x, y + i, z - i] = 1
        if y - i >= 0 and z + i < 8:
            tahta[x, y - i, z + i] = 1

    # Vezirin üç boyutlu çapraz hareketleri
    for i in range(1, 8):
        if x + i < 8 and y + i < 8 and z + i < 8:
            tahta[x + i, y + i, z + i] = 1
        if x - i >= 0 and y - i >= 0 and z - i >= 0:
            tahta[x - i, y - i, z - i] = 1
        if x + i < 8 and y - i >= 0 and z + i < 8:
            tahta[x + i, y - i, z + i] = 1
        if x - i >= 0 and y + i < 8 and z - i >= 0:
            tahta[x - i, y + i, z - i] = 1
        if x + i < 8 and y + i < 8 and z - i >= 0:
            tahta[x + i, y + i, z - i] = 1
        if x - i >= 0 and y - i >= 0 and z + i < 8:
            tahta[x - i, y - i, z + i] = 1
        if x + i < 8 and y - i >= 0 and z - i >= 0:
            tahta[x + i, y - i, z - i] = 1
        if x - i >= 0 and y + i < 8 and z + i < 8:
            tahta[x - i, y + i, z + i] = 1


# 8x8x8 boyutunda bir satranç tahtası oluştur
tahta = np.zeros((8, 8, 8), dtype=int)
while True:


    # Kullanıcıdan koordinatları al
    try:
        vezir_x = int(input("Vezirin x koordinatını girin (0-7, çıkmak için 8): "))
        if vezir_x == 8:
            break
        vezir_y = int(input("Vezirin y koordinatını girin (0-7): "))
        vezir_z = int(input("Vezirin z koordinatını girin (0-7): "))

        if not (0 <= vezir_x < 8 and 0 <= vezir_y < 8 and 0 <= vezir_z < 8):
            print("Geçersiz koordinatlar! Lütfen 0-7 arasında değerler girin.")
            continue

    except ValueError:
        print("Geçersiz giriş! Lütfen sayısal değerler girin.")
        continue

    # Vezirin hareketlerini tahtada işaretle
    vezir_hareketleri(tahta, vezir_x, vezir_y, vezir_z)

    # Sonucu yazdır
    print(tahta)

print("Program sonlandırıldı.")
```