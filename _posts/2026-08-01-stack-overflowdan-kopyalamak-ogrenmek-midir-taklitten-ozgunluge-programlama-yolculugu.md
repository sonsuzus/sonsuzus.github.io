---
layout: post
title: "Stack Overflow’dan Kopyalamak Öğrenmek midir? Taklitten Özgünlüğe Programlama Yolculuğu"
math: true
categories: 
  - Bilgi
tags: 
  - programlama öğrenme
  - Stack Overflow
  - yazılım pedagojisi
---

Bir hata mesajını arama motoruna yapıştırıp Stack Overflow’daki en yüksek oylu cevabı koda eklemek, yazılımcıların gizli kabul töreni gibidir. Kod çalışınca kısa süreliğine dâhi hissederiz; fakat aynı sorun ertesi gün geri döndüğünde büyü bozulur. Öyleyse kopyalamak gerçekten öğrenmek midir, yoksa yalnızca çalışan bir sonuca ulaşmanın hızlı yolu mudur?

<!--more-->

## Taklit neden öğrenmenin doğal bir parçasıdır?

İnsanlar konuşmayı, müzik çalmayı ve problem çözmeyi önce örnekleri taklit ederek öğrenir. Programlama da farklı değildir. Yeni başlayan biri, bir döngünün nasıl kurulduğunu veya bir API isteğinin nasıl gönderildiğini mevcut örneklerden görerek zihinsel modeller oluşturur.

Pedagojide buna **modelleme** denir. Öğrenci, uzman tarafından üretilmiş bir çözümü inceler; çözümün parçalarını tanır ve zamanla benzer durumlarda kullanır. Bu açıdan kopyalama tek başına kötü değildir. Sorun, kodun davranışı sorgulanmadan alınmasıdır.

Öğrenmeyi basitleştirilmiş biçimde şöyle düşünebiliriz:

$$Öğrenme = Taklit + Açıklama + Değiştirme + Geri\ Bildirim$$

Bu denklemde yalnızca taklit varsa sonuç öğrenme değil, geçici bağımlılıktır. Açıklama ve değiştirme aşamaları eklendiğinde ise alınan kod, zihinsel bir araca dönüşür.

## Kopyalama ile öğrenme arasındaki fark

| Davranış | Kısa vadeli sonuç | Uzun vadeli etkisi |
|---|---|---|
| Kodu doğrudan yapıştırmak | Hata hızla çözülebilir | Benzer hatada tekrar arama gerekir |
| Kodu satır satır açıklamak | Daha fazla zaman alır | Kavramsal model oluşur |
| Örneği değiştirip denemek | Yeni hatalar çıkarabilir | Bilginin sınırları keşfedilir |
| Çözümü sıfırdan yeniden yazmak | Başlangıçta zordur | Hatırlama ve transfer güçlenir |

Buradaki kritik kavram **transfer**dir: Öğrenilen bilginin farklı bir probleme uygulanabilmesi. Bir Stack Overflow cevabını yalnızca kendi bağlamında kullanabiliyorsanız çözümü edinmiş, fakat ilkeyi öğrenmemiş olabilirsiniz.

## Aynı kodu deney laboratuvarına çevirmek

Örneğin bir listedeki tekrarları kaldırmak için şu Python cevabını bulduğunuzu düşünelim:

```python
sayilar = [3, 1, 3, 2, 1]
benzersiz = list(dict.fromkeys(sayilar))
print(benzersiz)
```

Bu kod, sözlük anahtarlarının benzersiz olmasından ve modern Python sürümlerinde eklenme sırasını korumasından yararlanır. Sadece yapıştırmak yerine şu soruları deneyebilirsiniz:

- Neden `set(sayilar)` kullanılmadı?
- Liste sayılar yerine sözlükler içerirse ne olur?
- Sıralamanın korunması gerekli değilse hangi çözüm daha okunaklıdır?

Alternatif çözümü çalıştırmak karşılaştırmayı somutlaştırır:

```python
sayilar = [3, 1, 3, 2, 1]
benzersiz = list(set(sayilar))
print(benzersiz)  # Eleman sırası garanti edilmez.
```

İki kod da tekrarları kaldırabilir; ancak davranış sözleşmeleri farklıdır. Öğrenme tam olarak bu farkı fark ettiğiniz anda başlar.

## Verimli taklit için dört adımlı yöntem

**1. Tahmin et:** Kodu çalıştırmadan önce çıktısını yaz. Tahmin ile gerçek sonuç arasındaki fark, bilgi açığını gösterir.

**2. Açıkla:** Her satırı kendi kelimelerinle anlat. “Bu satır ne yapıyor?” kadar “Neden burada?” sorusunu da sor.

**3. Boz:** Değişken türünü, girdiyi veya koşulu değiştir. Kodun hangi noktada kırıldığını gözlemle. Hatalar, çözümün sınırlarını görünür kılar.

**4. Yeniden üret:** Kaynağı kapatıp aynı fikri sıfırdan uygula. Hatırlama çabası öğrenmeyi güçlendirir. Bunu kabaca $Kalıcılık \propto Aktif\ Hatırlama$ şeklinde ifade edebiliriz.

## Özgünlük sıfırdan icat etmek değildir

Yazılımda özgünlük, her algoritmayı yeniden keşfetmek anlamına gelmez. Usta geliştiriciler de dokümantasyon okur, açık kaynak kodları inceler ve geçmiş çözümlerden yararlanır. Farkları; aldıkları parçayı bağlama uyarlamaları, güvenlik ve performans sonuçlarını değerlendirmeleri ve gerekirse kaynağı belirtmeleridir.

Stack Overflow bir cevap makinesi değil, örneklerle dolu bir laboratuvar olarak kullanıldığında güçlü bir öğretmendir. Kopyalamak öğrenmenin başlangıcı olabilir; fakat öğrenme, kodu çalıştırdığınızda değil, neden çalıştığını açıklayıp başka bir probleme uyarlayabildiğinizde tamamlanır.
