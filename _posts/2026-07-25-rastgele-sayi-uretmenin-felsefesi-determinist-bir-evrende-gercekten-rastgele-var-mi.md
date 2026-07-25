---
layout: post
title: "Rastgele Sayı Üretmenin Felsefesi: Determinist Bir Evrende Gerçekten Rastgele Var mı?"
math: true
categories: 
  - Bilgi
tags: 
  - rastgelelik
  - algoritmalar
  - felsefe
  - kriptografi
---

Bilgisayarların zar atabildiğini düşünmek tatlı bir yanılsamadır; çünkü işlemcinin içinde minik bir kumarbaz yoktur. Bir programın ürettiği sayı çoğu zaman, sadece iyi gizlenmiş bir düzenin sonucudur. İşte bu yüzden rastgele sayı üretimi, hem yazılım mühendisliğinin pratik bir konusu hem de ‘evren gerçekten öngörülebilir mi?’ sorusuna açılan küçük ama derin bir kapıdır.
``

## Rastgelelik Ne Demek?

Gündelik hayatta rastgelelik, sonucu önceden bilememek demektir. Ancak bilgisayar biliminde bu tanım yetmez. Bir sayı dizisinin rastgele görünmesi, onun gerçekten nedensiz olduğu anlamına gelmez. Determinist bir sistemde aynı başlangıç koşulları aynı sonucu üretir. Yani bir algoritmaya aynı tohumu, yani seed değerini verirseniz, aynı sayı dizisini tekrar alırsınız.

Matematiksel olarak birçok sözde rastgele sayı üreteci şu fikre dayanır:

$X_{n+1} = (aX_n + c) \bmod m$

Bu formül, Linear Congruential Generator yani LCG adı verilen klasik yöntemin kalbidir. Burada $X_n$ mevcut durum, $a$ çarpan, $c$ artış ve $m$ mod değeridir. Sonuçta kaotik görünen ama tamamen hesaplanabilir bir dizi oluşur.

| Kavram | Gerçek Rastgelelik | Sözde Rastgelelik |
|---|---|---|
| Kaynak | Fiziksel olaylar | Algoritma |
| Tekrar üretilebilir mi? | Genelde hayır | Evet, aynı seed ile |
| Hız | Daha yavaş olabilir | Çok hızlıdır |
| Kullanım | Kriptografi, güvenlik | Simülasyon, oyun, test |
| Felsefi tat | Evrenin cilvesi | Determinizmin makyajı |

## Seed: Kaderin Küçük Başlangıç Noktası

Seed, algoritmanın başlangıç koşuludur. Determinist felsefede evrenin tüm anları, ilk koşullardan zorunlu olarak çıkıyorsa; PRNG de bunun cep boy versiyonudur. Seed değerini bilirseniz geleceği bilirsiniz. Bu, Laplace’ın şeytanı fikrine benzer: Evrenin tüm parçacıklarının konumunu ve hızını bilen bir zihin, geçmişi ve geleceği hesaplayabilir miydi?

Basit bir PRNG örneği görelim:

```python
class LCG:
    def __init__(self, seed):
        self.state = seed
        self.a = 1664525
        self.c = 1013904223
        self.m = 2**32

    def next_int(self):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state

    def random(self):
        return self.next_int() / self.m

rng = LCG(42)
numbers = [rng.random() for _ in range(5)]
```

Bu kodda `random()` metodu 0 ile 1 arasında sayı üretir. Fakat sihir yoktur; her şey `state` değişkeninin dönüşümünden ibarettir. `42` seed değeriyle çalıştırırsanız, diziniz her seferinde aynı olur. Yani bilgisayar ‘şaşırmaz’, sadece bizi şaşırtır.

## Entropi: Bilgisayarın Kaos Arayışı

Gerçek rastgeleliğe yaklaşmak için işletim sistemleri fare hareketleri, klavye zamanlamaları, disk erişim gecikmeleri veya donanımsal gürültüler gibi kaynaklardan entropi toplar. Entropi, kabaca belirsizlik miktarıdır. Bilgi kuramında şu şekilde ifade edilir:

$H(X)=-\sum p(x)\log_2 p(x)$

Bir olay ne kadar öngörülemezse entropisi o kadar yüksektir. Adil bir yazı-tura atışında iki sonuç da eşit olasılıklıdır ve belirsizlik maksimumdur. Ama hileli bir paranın sonucu daha tahmin edilebilirdir; entropisi düşer.

| Kullanım Senaryosu | Hangi Rastgelelik Yeterli? | Neden? |
|---|---|---|
| Oyunlarda loot düşürme | PRNG | Hızlı ve kontrol edilebilir |
| Bilimsel simülasyon | Kaliteli PRNG | Tekrar edilebilir deney gerekir |
| Şifreleme anahtarı | Kriptografik RNG | Tahmin edilemezlik şarttır |
| Sanatsal üretim | PRNG veya fiziksel RNG | Estetik amaç baskındır |

## Metafizik Soru: Rastgelelik Cehalet mi, Gerçek mi?

Eğer evren tamamen deterministse, rastgelelik sadece bizim bilgisizliğimiz olabilir. Zarın sonucu, hava direnci, atış açısı, yüzey sürtünmesi ve kuvvet bilinse hesaplanabilir. Bu bakışa göre rastgelelik epistemiktir: Bilginin eksikliğinden doğar.

Ama kuantum mekaniği sahneye çıkınca işler karışır. Bazı yorumlara göre parçacıkların davranışı temelde olasılıksaldır. Bu durumda rastgelelik ontolojik olabilir: Yani sadece bilmiyoruz değil, gerçekten belirlenmemiştir. Bilgisayarlar bu tartışmayı çözmez; sadece onu kod yazarken masamıza getirir.

## Sonuç: Rastgelelik Bir Araç, Bir Ayna ve Bir Şaka

Programcı için rastgele sayı üretimi, test verisi hazırlamak, oyun tasarlamak, simülasyon yapmak ve güvenlik sağlamak için vazgeçilmezdir. Filozof içinse aynı konu, özgür irade ve determinizm tartışmasının dijital bir modelidir. Bilgisayarların ürettiği çoğu rastgelelik aslında sözde rastgeleliktir; ama yeterince iyi tasarlandığında pratikte harika çalışır.

Belki de en güzel cevap şudur: Bilgisayar rastgeleliği üretmez, rastgelelik hissini mühendislik eder. Ve bazen, yazılım dünyasında ihtiyacımız olan şey tam olarak budur.
