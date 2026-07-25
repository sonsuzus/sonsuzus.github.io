---
layout: post
title: "Kod Arkeolojisi: Terk Edilmiş Repolardan Algoritma Hazinesi Çıkarmak"
math: true
categories: 
  - Bilgi
tags: 
  - açık kaynak
  - algoritmalar
  - kod arkeolojisi
  - refactoring
---

Terk edilmiş açık kaynak repoları, yazılım dünyasının tozlu tavan araları gibidir: kırık README’ler, çalışmayan CI rozetleri ve arada bir “Bunu kim, nasıl düşünmüş?” dedirten parlak fikirler. Kod arkeolojisi tam da burada başlar; amaç eski kodu kutsamak değil, içindeki zekice çözümü bugünün diliyle yeniden anlamaktır.
``
Bir repoya yıllardır commit gelmemiş olması, içindeki fikrin bayatladığı anlamına gelmez. Hatta bazen eski projeler, güncel framework kalabalığından uzakta, problemi çıplak haliyle çözer. Yeni kütüphaneler katman eklerken, eski kodlar çoğu zaman doğrudan algoritmanın kalbine gider. Bu yüzden kod arkeoloğunun ilk sorusu “Bu proje hâlâ çalışıyor mu?” değil, “Burada hangi problem, hangi kısıt altında çözülmüş?” olmalıdır.

Teorik altyapı için üç şeyi ayırmak çok işe yarar: veri yapısı, karmaşıklık ve bağlam. Bir algoritma hilesi genellikle bu üçlünün kesişiminde saklanır. Örneğin eski bir arama aracında tam metin arama yerine bit maskeleri kullanılmış olabilir. Eğer belge sayısı $n$, kelime sayısı $m$ ise klasik yaklaşımda sorgu maliyeti kabaca $O(n \cdot m)$ gibi büyürken, bit kümeleriyle kesişim almak $O(n / w)$ seviyesine iner; burada $w$ makine kelimesi genişliğidir. Yani 64 bitlik işlemcide tek hamlede 64 olasılık süzülür. Bu, küçük bir sihir değil; donanımı algoritmaya dahil etmektir.

| Bulgu | Eski Kodda Görünümü | Güncel Dille Yorumu |
|---|---|---|
| Bit maskesi | `flags & 8` gibi gizemli kontroller | Bellek dostu durum modeli |
| LRU listesi | Çift bağlı liste + hash tablo | $O(1)$ cache stratejisi |
| Sentinel değer | `-1`, `NULL_NODE` | Sınır kontrolünü sadeleştirme |
| Ön hesaplama | Büyük sabit tablolar | Zaman-bellek takası |

Arkeolojik kazıda en sevdiğim örneklerden biri, eski oyun motorlarında görülen “kirli dikdörtgen” tekniğidir. Ekranın tamamını yeniden çizmek yerine sadece değişen bölgeler işaretlenir. Bugün bunu “incremental rendering” diye daha havalı anlatıyoruz. Mantık basittir: Eğer ekran alanı $A$, değişen alan $d$ ise ve $d \ll A$ ise, çizim maliyeti dramatik biçimde düşer. Formül gibi söyleyelim: toplam iş $T \approx c \cdot d$ olur, $c \cdot A$ değil.

Aşağıdaki örnek, terk edilmiş bir GUI kütüphanesinde görebileceğiniz fikri modern Python ile sadeleştirir. Amaç, çakışan kirli bölgeleri birleştirip gereksiz çizimi azaltmaktır:

```python
from dataclasses import dataclass

@dataclass
class Rect:
    x: int
    y: int
    w: int
    h: int

    def overlaps(self, other):
        return not (
            self.x + self.w < other.x or other.x + other.w < self.x or
            self.y + self.h < other.y or other.y + other.h < self.y
        )

    def merge(self, other):
        x1 = min(self.x, other.x)
        y1 = min(self.y, other.y)
        x2 = max(self.x + self.w, other.x + other.w)
        y2 = max(self.y + self.h, other.y + other.h)
        return Rect(x1, y1, x2 - x1, y2 - y1)

def compact_dirty_regions(regions):
    result = []
    for rect in regions:
        for i, old in enumerate(result):
            if rect.overlaps(old):
                result[i] = old.merge(rect)
                break
        else:
            result.append(rect)
    return result
```

Bu kod kusursuz bir geometri motoru değildir; fakat fikri net gösterir. Eski projelerde sıkça karşılaşılan değer de budur: üretim seviyesinde paketlenmiş bir çözüm değil, doğru problemi doğru yerinden yakalayan küçük bir mekanizma.

Kod arkeolojisi yaparken commit geçmişi, issue tartışmaları ve test dosyaları altın değerindedir. Kod “ne” yaptığını söyler, testler “neden” yaptığını fısıldar, issue’lar ise “hangi acı yüzünden” yazıldığını bağırır. Özellikle performansla ilgili yamalarda şu izi arayın: Önce basit çözüm vardır, sonra kullanıcı şikâyeti gelir, ardından küçük ama keskin bir optimizasyon eklenir.

| Kazı Aracı | Ne Aranır? | Tehlike |
|---|---|---|
| `git blame` | Kararın tarihi | Kişiyi suçlama tuzağı |
| Testler | Kenar durumlar | Eksik senaryo sanmak |
| Benchmark | Gerçek darboğaz | Mikro optimizasyona kapılmak |
| README | Tasarım niyeti | Güncel sanmak |

Sonuçta terk edilmiş repolar birer mezarlık değil, fikir fosili yatağıdır. Her eski hileyi bugüne taşımak gerekmez; bazıları sadece döneminin kısıtlarına uygundur. Ama iyi bir kod arkeoloğu, paslı satırların arasından şu soruyu çıkarır: “Bu çözüm hangi basit ilkeye dayanıyor?” Cevap çoğu zaman hâlâ değerlidir: daha az iş yap, veriyi doğru biçimde tut, sınır durumunu baştan tasarla ve algoritmanın matematiğini unutma.
