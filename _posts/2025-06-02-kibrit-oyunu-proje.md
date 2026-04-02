---
layout: post
title: Kibrit Oyunu Projesi
categories:
  - Proje
tags:
  - program
  - oyun
  - tübitak
  - tübitak4006
  - kibrit
  - asal sayılar
  - asal üsler
  - random
redirect_from:
  - /posts/kibrit-oyunu-proje/
---

Seçilen bir p asal sayısı ve n doğal sayısı sonrası sırayla oynanan ve 1.000.000 kibrit çöpünden en son kim yerde kalanları toplayacak şeklinde olan bir programlama oyunu. Oyunumuz bilgisayar veya cep telefonu gibi dijital bir ortamda oynanacaktır. İnsan-insan seçeneği olduğu gibi İnsan-Yapayzeka seçeneği de olacaktır. Oyunumuz sanal olarak 1 milyon kibrit çöpü ile başlayacaktır. Sırası gelen oyuncu p bir asal sayı ve n bir doğal sayı olmak üzere iki sayı girecektir (program ikisini de kontrol edecektir). Bilgisayar ortada kalan kibrit çöplerinden p^n adedini çıkaracaktır. Tam olarak yerdeki kibrit çöplerini bir asalın üssü olarak söyleyen kişi oyunu kazanacaktır. (örneğin yerde 125 kibrit çöpü kaldıysa p = 5 ve n = 3 diyen kişi oyunu kazanacaktır. veya 16 kibrit çöpü kaldıysa 2^4 diyen kişi oyunu kazanır. 4^2 diyemez çünkü 4 bir asal sayı değildir) İki insan oynarken hakemlik yapacak programımızın insana karşı yapay zeka modülü de olacaktır. Program görsel olarak windows ve linux tabanlı sistemlerde sorunsuz çalışacaktır. Python tk kütüphanesi kullanılacaktır.

Projemizin amacı, asal sayılar ve özellikleri hakkında bilgileri bir bilgisayar oyunu aracılığıyla kullanıcıya aktarmaktır. Oyun, kullanıcıların asal sayılarla ilgili işlemleri yapma, problem çözme ve birkaç hamle sonrasını düşünme becerilerini geliştirmeyi hedeflemektedir. Ayrıca, yapay zeka destekli bir modül ile insan ve yapay zeka düşünme biçimlerini karşılaştırma imkanı sunulacaktır. Bu modül, kullanıcıların stratejik düşünme becerilerini analiz ederken, yapay zekanın farklı yaklaşımlarını anlamalarına da olanak tanıyacaktır. Oyun, hem eğitici hem de eğlenceli bir platform sunarak matematiksel düşünme ve teknolojik farkındalık oluşturmayı amaçlar.

Oyunu oynayanların asal sayılar hakkında bilgi edinmesini sağlamak ve asal sayı işlemleri konusunda temel beceri kazandırmak. 

Oyunu oynayan kişilerin bir kaç hamle ilerisini hesaplamasını sağlamak ve mantık , düşünme becerilerini arttırmak. 

Kodlamaya veya programlamaya meraklı kişilerin "basit bir yapay zeka sistemi nasıl oluşturulur" konusunda ilgisini çekmek. 

Büyük asalları bulma ve kullanma konusunda beceriler kazandırmak beklediğimiz sonuçlardandır.

Aynı zamanda oyunla matematikteki asal sayların birleştirilmesi oyunu oynayan kişiler açısından bir farkındalık yaratacağı beklenen sonuçlar arasındadır.

Projenin kodu aşağıdadır.

```python
import tkinter as tk
from tkinter import font, messagebox
import asalusliste # asal_us = [[p, n, p^n], ...] formatında olmalı
import numpy as np
import random

cop = 1000000  # Başlangıç çöp sayısı
oyuncu_sira = "insan"  # İlk sıra insanda

# Orijinal p^n listesini yükle ve bir kopyasını oluştur
try:
    asal_us_deger_orjinal = np.array(asalusliste.asal_us)
    if asal_us_deger_orjinal.ndim != 2 or asal_us_deger_orjinal.shape[1] != 3:
        messagebox.showerror("Dosya Hatası", "asalusliste.asal_us beklenen formatta değil (Nx3 olmalı).")
        exit()
    if not np.any(asal_us_deger_orjinal[:, 1] == 0): # p^0 = 1 kontrolü
        messagebox.showwarning("Uyarı: asalusliste",
                               "asalusliste.asal_us dosyasında p^0=1 (n=0) şeklinde değerler bulunamadı.\n"
                               "Örneğin: [2, 0, 1], [3, 0, 1] gibi.\n"
                               "Bu değerler olmadan oyun belirli durumlarda kilitlenebilir.")
except AttributeError:
    messagebox.showerror("Dosya Hatası", "asalusliste.py dosyasında 'asal_us' listesi bulunamadı.")
    exit()
except Exception as e:
    messagebox.showerror("Dosya Yükleme Hatası", f"asalusliste yüklenirken bir hata oluştu: {e}")
    exit()

asal_us_deger = np.copy(asal_us_deger_orjinal) # Üzerinde çalışılacak kopya

def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def tablo_kucult(copler):
    global asal_us_deger
    if copler <= 0:
        asal_us_deger = np.array([])
        return
    mask = asal_us_deger_orjinal[:, -1] <= copler
    asal_us_deger = asal_us_deger_orjinal[mask]

def sistem_sayi_sec(copler_suanki):
   global asal_us_deger

   if len(asal_us_deger) == 0:
       return None, None, None

   # Strateji 1: Kazanma Hamlesi
   kazanma_indexleri = np.where(asal_us_deger[:, -1] == copler_suanki)[0]
   if len(kazanma_indexleri) > 0:
       secilen_index = kazanma_indexleri [0]
       return asal_us_deger [secilen_index][0], asal_us_deger [secilen_index][1], asal_us_deger [secilen_index][2]

   # Strateji 2: Rakibe asal üssü bırakmamaya çalış
   tercih_edilen_hamleler = []
   gecerli_hamleler = []

   for hamle_detayi in asal_us_deger:
       p_val, n_val, alinacak_cop_val = hamle_detayi
       gecerli_hamleler.append(hamle_detayi)
       kalan_sonrasi = copler_suanki - alinacak_cop_val
       # Kalanın asal üssü olup olmadığını kontrol et
       asal_ussu_mu = np.any(asal_us_deger_orjinal[:, -1] == kalan_sonrasi)
       if kalan_sonrasi > 0 and not asal_ussu_mu:
           tercih_edilen_hamleler.append(hamle_detayi)
       elif kalan_sonrasi == 0:
           tercih_edilen_hamleler.append(hamle_detayi) # Kazanma hamlesini de tercih et

   if tercih_edilen_hamleler:
       secilen_hamle = random.choice(tercih_edilen_hamleler)
       return secilen_hamle [0], secilen_hamle [1], secilen_hamle [2]
   elif gecerli_hamleler:
       # Tercih edilen hamle yoksa, geçerli hamlelerden rastgele birini seç
       secilen_hamle = random.choice(gecerli_hamleler)
       return secilen_hamle [0], secilen_hamle [1], secilen_hamle [2]
   else:
       return None, None, None


def oyun_bitti_mi(kalan_cop, kim_oynadi_son_hamleyi):
    if kalan_cop == 0:
        if kim_oynadi_son_hamleyi == "insan":
            messagebox.showinfo("Oyun Bitti 🎉", "Tebrikler, SİZ KAZANDINIZ!")
        else:
            messagebox.showinfo("Oyun Bitti 🤖", "Bilgisayar kazandı!")
        p_entry.config(state=tk.DISABLED)
        n_entry.config(state=tk.DISABLED)
        hesapla_button.config(state=tk.DISABLED)
        sira_label.config(text="Oyun Bitti!")
        return True
    return False

def bilgisayar_oyna():
    global cop
    global oyuncu_sira

    sira_label.config(text="Sıra: Bilgisayar Düşünüyor... 🤔")
    window.update_idletasks()

    tablo_kucult(cop) 
    p_comp, n_comp, sonuc_comp = sistem_sayi_sec(cop)

    if sonuc_comp is None or sonuc_comp <= 0:
        messagebox.showinfo("Oyun Durumu", "Bilgisayar geçerli bir hamle bulamadı.\nSiz kazandınız!")
        p_entry.config(state=tk.DISABLED)
        n_entry.config(state=tk.DISABLED)
        hesapla_button.config(state=tk.DISABLED)
        sira_label.config(text="Oyun Bitti! (Bilgisayar Hamle Yapamadı)")
        result_label1.config(text=f"Bilgisayar: Hamle yapamadı!")
        result_label2.config(text=f"Kalan Çöp: {cop}")
        return

    cop -= sonuc_comp
    
    result_label1.config(text=f"Bilgisayar Aldı: {p_comp} ^ {n_comp} = {sonuc_comp}")
    result_label2.config(text=f"Kalan Çöp: {cop}")
    bilgisayar_hamle_label.config(text=f"🤖 Bilgisayar: p={p_comp}, n={n_comp} (Aldı: {sonuc_comp})")
    insan_hamle_label.config(text="")

    if oyun_bitti_mi(cop, "bilgisayar"):
        return

    oyuncu_sira = "insan"
    sira_label.config(text="Sıra: Sizde 😊")
    p_entry.config(state=tk.NORMAL)
    n_entry.config(state=tk.NORMAL)
    hesapla_button.config(state=tk.NORMAL)
    p_entry.focus()
    tablo_kucult(cop)

def insan_oyna():
    global cop
    global oyuncu_sira

    if oyuncu_sira != "insan": return

    try:
        p_val_str = p_entry.get()
        n_val_str = n_entry.get()

        if not p_val_str or not n_val_str:
            messagebox.showwarning("Giriş Hatası", "Lütfen p ve n değerlerini girin.")
            return

        p = int(p_val_str)
        n = int(n_val_str)

        if not is_prime(p):
            messagebox.showerror("Geçersiz Giriş", f"{p} bir asal sayı değildir!")
            return
        if n < 0:
            messagebox.showerror("Geçersiz Giriş", "n negatif olmayan bir tam sayı olmalıdır (n ≥ 0)!")
            return

        sonuc_insan = p ** n
        if sonuc_insan <= 0:
            messagebox.showerror("Geçersiz Hamle", "Alınan çöp sayısı pozitif olmalıdır.")
            return
        if sonuc_insan > cop:
            messagebox.showerror("Geçersiz Hamle", f"Kalan çöpten ({cop}) daha fazla ({sonuc_insan}) alamazsınız!")
            return

        cop -= sonuc_insan
        result_label1.config(text=f"Siz Aldınız: {p} ^ {n} = {sonuc_insan}")
        result_label2.config(text=f"Kalan Çöp: {cop}")
        insan_hamle_label.config(text=f"😊 Siz: p={p}, n={n} (Aldınız: {sonuc_insan})")
        bilgisayar_hamle_label.config(text="")
        p_entry.delete(0, tk.END)
        n_entry.delete(0, tk.END)

        if oyun_bitti_mi(cop, "insan"):
            return

        oyuncu_sira = "bilgisayar"
        p_entry.config(state=tk.DISABLED)
        n_entry.config(state=tk.DISABLED)
        hesapla_button.config(state=tk.DISABLED)
        
        # Bilgisayarın oynaması için 5 saniye bekle
        window.after(5000, bilgisayar_oyna) # 5000 milisaniye = 5 saniye

    except ValueError:
        messagebox.showerror("Giriş Hatası", "Lütfen p ve n için geçerli tam sayılar girin.")
    except Exception as e:
        messagebox.showerror("Beklenmedik Hata", f"Bir hata oluştu: {e}")

# --- Arayüz Kurulumu (Öncekiyle aynı, sadece başlık güncellendi) ---
window = tk.Tk()
window.title("Stratejik Kibrit Çöpü Oyunu 🔥 v2.0") # Başlık güncellendi
window.geometry("450x550")
window.resizable(False, False)

font_label = font.Font(family="Arial", size=12)
font_entry = font.Font(family="Arial", size=12)
font_button = font.Font(family="Arial", size=12, weight="bold")
font_result = font.Font(family="Arial", size=14, weight="bold")
font_info = font.Font(family="Arial", size=11)
font_status = font.Font(family="Arial", size=12, weight="bold")

status_frame = tk.Frame(window)
status_frame.pack(pady=10)
tk.Label(status_frame, text=f"Başlangıç Çöpü: {cop}", font=font_info).pack(side=tk.LEFT, padx=10)
sira_label = tk.Label(status_frame, text="Sıra: Sizde 😊", font=font_status, fg="darkblue")
sira_label.pack(side=tk.LEFT, padx=10)

input_frame = tk.Frame(window)
input_frame.pack(pady=10)
tk.Label(input_frame, text="p (asal sayı):", font=font_label).grid(row=0, column=0, padx=5, pady=5, sticky="e")
p_entry = tk.Entry(input_frame, font=font_entry, width=10)
p_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Label(input_frame, text="n (doğal sayı ≥ 0):", font=font_label).grid(row=1, column=0, padx=5, pady=5, sticky="e")
n_entry = tk.Entry(input_frame, font=font_entry, width=10)
n_entry.grid(row=1, column=1, padx=5, pady=5)

hesapla_button = tk.Button(window, text="Oyna!", command=insan_oyna, font=font_button, bg="#4CAF50", fg="white", relief=tk.RAISED, borderwidth=3)
hesapla_button.pack(pady=15, ipadx=10, ipady=5)

results_frame = tk.Frame(window, pady=10)
results_frame.pack(fill="x", padx=20)
result_label1 = tk.Label(results_frame, text="", font=font_result, fg="#007bff")
result_label1.pack(pady=5)
result_label2 = tk.Label(results_frame, text=f"Kalan Çöp: {cop}", font=font_result, fg="#dc3545")
result_label2.pack(pady=5)

hamle_detay_frame = tk.Frame(window)
hamle_detay_frame.pack(pady=10, fill="x", padx=20)
insan_hamle_label = tk.Label(hamle_detay_frame, text="", font=font_info, wraplength=400)
insan_hamle_label.pack(pady=2)
bilgisayar_hamle_label = tk.Label(hamle_detay_frame, text="", font=font_info, wraplength=400)
bilgisayar_hamle_label.pack(pady=2)

tablo_kucult(cop)
p_entry.focus()
window.mainloop()
```
