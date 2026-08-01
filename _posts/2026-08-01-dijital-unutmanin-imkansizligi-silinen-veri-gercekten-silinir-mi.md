---
layout: post
title: "Dijital Unutmanın İmkânsızlığı: Silinen Veri Gerçekten Silinir mi?"
math: true
categories: 
  - Bilgi
tags: 
  - veri kalıcılığı
  - dijital hafıza
  - veri güvenliği
---

Bir fotoğrafı sildiğimizde onun yok olduğuna inanmak isteriz. Çöp kutusu boşalır, dosya ekrandan kaybolur ve dijital dünya bize unutmuş gibi görünür. Oysa bilgisayarların “unutması”, insan hafızasındaki unutmaya pek benzemez. Çoğu zaman veri ortadan kaldırılmaz; yalnızca ona giden yol tabelası sökülür. Bu teknik ayrıntı, dijital çağın en ilginç felsefi sorularından birini doğurur: Hatırlanabilecek bir şey gerçekten unutulmuş sayılabilir mi?

``

## Silmek neden her zaman yok etmek değildir?

Bir dosya, depolama aygıtında veri blokları ve bu blokların konumunu gösteren dosya sistemi kayıtlarından oluşur. Normal silme işleminde işletim sistemi genellikle blokları hemen temizlemek yerine ilgili alanı “yeniden kullanılabilir” olarak işaretler. Yeni veri yazılana kadar eski bitler yerinde kalabilir.

Basitleştirilmiş biçimde veri kalıcılığını şöyle düşünebiliriz:

$$K = P(B) \times P(E)$$

Burada $P(B)$, veri bloklarının henüz üzerine yazılmamış olma olasılığını; $P(E)$ ise bu blokların doğru biçimde eşleştirilerek okunabilme olasılığını temsil eder. İki değer de sıfır değilse veri kurtarma ihtimali vardır.

| İşlem | Kullanıcıya görünen | Teknik gerçeklik |
|---|---|---|
| Dosyayı silmek | Dosya kaybolur | Dizin kaydı kaldırılabilir |
| Çöp kutusunu boşaltmak | Kalıcı silme hissi oluşur | Bloklar hâlâ durabilir |
| Üzerine yazmak | Eski veri görünmez | Manyetik disklerde kurtarma zorlaşır |
| Kriptografik silme | Anahtar yok edilir | Şifreli veri pratikte anlamsızlaşır |

## İnsan hafızası ve dijital hafıza

İnsan unutması pasif bir veri kaybı değildir. Anılar zamanla yeniden yorumlanır, duygularla biçimlenir ve her hatırlamada bir ölçüde yeniden yazılır. Dijital sistemlerdeyse bir kopya, bağlamını kaybetse bile bit düzeyinde aynı kalabilir.

| İnsan hafızası | Dijital hafıza |
|---|---|
| Seçici ve değişkendir | Kesin kopyalar üretebilir |
| Zamanla bulanıklaşır | Ortam dayanırsa değişmeden kalır |
| Hatırlama anıyı dönüştürebilir | Okuma çoğunlukla veriyi değiştirmez |
| Unutma doğal bir süreçtir | Unutma özel bir işlem gerektirir |

Bu fark, “hafıza” sözcüğünün bilgisayarlarda biraz yanıltıcı olduğunu gösterir. İnsan hafızası yaşayan bir anlatıdır; dijital hafıza ise çoğaltılabilen bir izdir.

## Üzerine yazmak çözüm mü?

Manyetik disklerde dosya alanını rastgele baytlarla doldurmak eski veriyi erişilemez hâle getirebilir. Aşağıdaki Python örneği, bir dosyanın mevcut içeriği üzerine rastgele veri yazar ve ardından dosyayı kaldırır:

```python
import os
from pathlib import Path

def overwrite_and_delete(path):
    target = Path(path)
    size = target.stat().st_size

    with target.open('r+b') as file:
        file.write(os.urandom(size))
        file.flush()
        os.fsync(file.fileno())

    target.unlink()
```

Kod, dosya boyutu kadar rastgele bayt üretir, bunları diske göndermeye çalışır ve son olarak dizin kaydını siler. Ancak bu yöntem SSD’lerde garanti sunmaz. Aşınma dengeleme mekanizması, yeni veriyi aynı fiziksel hücreler yerine başka hücrelere yazabilir. TRIM komutu da temizliği denetleyiciye bırakır. Bu nedenle modern aygıtlarda tam disk şifreleme ve şifreleme anahtarının güvenli biçimde yok edilmesi daha güvenilir bir yaklaşımdır.

## Bulut çağında unutmanın paradoksu

Yerel diski temizlemek yalnızca bir kopyayı etkiler. Bulut yedekleri, e-posta ekleri, mesajlaşma uygulamaları, önbellekler, günlük kayıtları ve başka kullanıcıların cihazları verinin çoğalmış izlerini taşıyabilir. Kopya sayısı $n$ arttıkça, tüm kopyaların silinme olasılığı kabaca şöyle ifade edilebilir:

$$P(T) = p^n$$

Her kopyanın başarıyla silinme olasılığı $p$ ise, $n$ büyüdükçe tam unutma zorlaşır. Dijital kalıcılık yalnızca donanımsal değil, aynı zamanda ağsal ve toplumsal bir problemdir.

## Unutulma hakkı neden önemlidir?

İnsan, geçmişinden uzaklaşarak değişebilme hakkına sahiptir. Fakat arama motorları ve arşivler geçmişi sürekli bugüne çağırdığında kişi, eski hâlinin dijital gölgesine dönüşebilir. Bu yüzden unutulma hakkı sadece gizlilik değil, kimliğin zaman içinde yeniden kurulabilmesi meselesidir.

Sonuçta dijital dünyada silmek tek bir düğmeye basmak değil; bağlantıları, kopyaları, anahtarları ve fiziksel izleri yönetmektir. Bilgisayarlar kendiliğinden unutmaz. Belki de asıl soru, verinin silinip silinmediği değil, makinelerimize merhametli bir unutma yeteneğini nasıl öğreteceğimizdir.
