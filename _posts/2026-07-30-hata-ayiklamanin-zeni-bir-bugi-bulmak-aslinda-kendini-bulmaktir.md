---
layout: post
title: "Hata Ayıklamanın Zen'i: Bir Bug'ı Bulmak Aslında Kendini Bulmaktır"
math: true
categories: 
  - Bilgi
tags: 
  - debugging
  - problem çözme
  - yazılım geliştirme
---

Kod çalışmadığında ilk şüphelimiz çoğu zaman bilgisayardır. Oysa bilgisayar, talimatlarımızı rahatsız edici bir sadakatle uygulamıştır. Bug; beklentimiz, varsayımımız ve gerçek davranış arasındaki çatlakta yaşar. Bu nedenle hata ayıklamak yalnızca bozuk satırı bulmak değil, düşünme biçimimizi gözlemlemektir: Neyi bildiğimizi sandık, neyi kontrol etmedik ve hangi sonuca gereğinden hızlı âşık olduk?

``

## Bug, beklenti ile gerçeklik arasındaki farktır

Bir programın beklenen çıktısını $E$, gözlenen çıktısını $O$ ile gösterelim. İncelediğimiz sapma kabaca şöyle düşünülebilir:

$$D = |E - O|$$

Buradaki asıl mesele $D$ değerini sıfırlamak değil, farkın hangi koşulda doğduğunu açıklayabilmektir. Açıklayamadığımız ama geçici olarak susturduğumuz hata, genellikle daha dramatik bir kostümle geri döner.

İyi bir hata ayıklama süreci bilimsel yönteme benzer:

1. Belirtiyi gözlemle.
2. Hatayı güvenilir biçimde yeniden üret.
3. Bir hipotez kur.
4. Tek bir değişkeni değiştirerek hipotezi test et.
5. Sonucu kaydet ve kapsamı daralt.

Bu yaklaşımın içe dönük tarafı şudur: Her hipotez, kod kadar zihnimiz hakkında da bilgi verir. “Veritabanı bozuktur” demeden önce, neden ilk olarak dış dünyayı suçlamaya eğilimli olduğumuzu fark ederiz.

## Tepki vermek ile araştırmak

| İçgüdüsel yaklaşım | Sistematik yaklaşım | Zihinsel karşılığı |
|---|---|---|
| Rastgele satır değiştirmek | Minimum örnek oluşturmak | Sabırsızlık yerine merak |
| Hata mesajını görmezden gelmek | Mesajı ve yığını okumak | Rahatsızlıktan kaçmamak |
| Aynı anda beş şeyi düzeltmek | Tek değişkeni test etmek | Kontrol yanılsamasını bırakmak |
| “Bende çalışıyor” demek | Ortam farklarını karşılaştırmak | Kendi bakış açısını mutlak saymamak |
| Belirtiyi bastırmak | Kök nedeni bulmak | Kısa rahatlama yerine kalıcı anlayış |

## Önce hatayı görünür kıl

Aşağıdaki Python fonksiyonu, indirimli fiyat hesaplıyor. Ancak `oran` değerinin yüzde mi, ondalık mı olduğu belirsiz:

```python
def indirimli_fiyat(fiyat, oran):
    print(f"DEBUG fiyat={fiyat}, oran={oran}")
    assert fiyat >= 0, "Fiyat negatif olamaz"
    assert 0 <= oran <= 1, "Oran 0 ile 1 arasında olmalı"
    return fiyat * (1 - oran)

print(indirimli_fiyat(100, 0.20))
```

`print`, programın o andaki durumunu görünür yapar; `assert` ise sessiz bir varsayımı çalıştırılabilir kurala dönüştürür. Formülümüz $P_{son} = P(1-r)$ olduğuna göre `20` değil, `0.20` beklenir. Böylece sorun yalnızca yanlış değer olmaktan çıkar, açıkça tanımlanmış bir sözleşme ihlaline dönüşür.

Gerçek projelerde günlük kayıtları, debugger durak noktaları ve otomatik testler aynı amaca hizmet eder: Zihnimizde kurduğumuz hikâyeyi ölçülebilir kanıtlarla karşılaştırmak.

## İkiye böl, sakinleş, tekrar et

Hatanın yüz satırlık bir alanda bulunduğunu düşünelim. Her adımda alanı ikiye bölersek gereken yaklaşık inceleme sayısı:

$$k = \lceil \log_2 n \rceil$$

$n=100$ için yalnızca $k=7$ adım yeterlidir. `git bisect`, modülleri devre dışı bırakma ve girdiyi küçültme teknikleri bu mantığı kullanır. Panik bütün sistemi aynı anda görmeye çalışır; yöntem ise soruyu küçültür.

## Debug günlüğü tut

Kısa bir kayıt, dairesel düşünmeyi engeller:

```text
Belirti: Sepet toplamı bazı siparişlerde negatif.
Tekrar: İki kupon aynı anda uygulanınca oluşuyor.
Hipotez: İndirimler sırayla değil, toplam olarak düşülüyor.
Deney: İkinci kuponu kapat.
Sonuç: Negatif değer kayboldu.
```

Bu günlük gelecekteki ekip arkadaşına yardım ederken geçmişteki hâlinizle de dürüst bir konuşma kurar.

Sonunda iyi debugger, hiç hata yapmayan kişi değildir. Yanıldığını hızlı, sakin ve kanıta dayanarak fark edebilen kişidir. Bug düzeldiğinde yalnızca program değişmez; varsayımlarını sınamayı öğrenen geliştirici de küçük bir sürüm yükseltmesi yaşar.
