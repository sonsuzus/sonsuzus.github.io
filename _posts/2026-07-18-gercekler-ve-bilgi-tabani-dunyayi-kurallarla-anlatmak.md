---
layout: post
title: "Gerçekler ve Bilgi Tabanı: Dünyayı Kurallarla Anlatmak"
math: true
categories: 
  - Bilgi
tags: 
  - bilgi-tabanı
  - yapay-zeka
  - mantıksal-programlama
---

Bir yazılıma dünyayı öğretmek isteseydik nereden başlardık? Kedilerin memeli olduğu, Ankara’nın Türkiye’nin başkenti olduğu, suyun 0°C’de donduğu gibi kesin kabul ettiğimiz küçük bilgi parçacıklarıyla. İşte bu küçük, değişmez ve doğrulanabilir ifadelere yapay zekâ ve mantıksal sistemlerde “gerçek” denir. Gerçekler bir araya geldiğinde ise yazılımın akıl yürütebileceği bir bilgi tabanı oluşur.
``
Bilgi tabanı, klasik veritabanından biraz farklı düşünülmelidir. Bir veritabanı genellikle “ne saklıyorum?” sorusuna odaklanır; bilgi tabanı ise “bu saklananlardan ne çıkarabilirim?” sorusunu da önemser. Örneğin `insan(Ayşe)` ve `insanlar ölümlüdür` bilgilerini biliyorsak, sistem `Ayşe ölümlüdür` sonucuna ulaşabilir. Bu, ham veri depolamaktan daha fazlasıdır: kurallar üzerinden anlam üretmektir.

Teorik olarak bir gerçek, çoğu zaman özne-yüklem-nesne üçlüsüyle ifade edilir. Mesela “Pamuk bir kedidir” cümlesi şu şekilde modellenebilir:

$kedi(Pamuk)$

“Nesne A, nesne B ile ilişkilidir” demek için de iki değişkenli yüklemler kullanılır:

$sahibi(Pamuk, Zeynep)$

Burada `sahibi` ilişkiyi, `Pamuk` ve `Zeynep` ise ilişkiye katılan nesneleri temsil eder. Bilgi tabanının gücü, bu küçük ifadelerin net ve tutarlı olmasından gelir. Çünkü mantıksal çıkarımda belirsizlik sevmez; yanlış ya da çelişkili gerçekler, sistemin tuhaf sonuçlar üretmesine neden olabilir.

| Kavram | Açıklama | Örnek |
|---|---|---|
| Nesne | Dünyadaki varlık | `Pamuk`, `Ankara` |
| Özellik | Nesnenin niteliği | `beyaz(Pamuk)` |
| İlişki | İki veya daha çok nesne arasındaki bağ | `başkentidir(Ankara, Türkiye)` |
| Kural | Gerçeklerden yeni sonuç çıkarma şablonu | `kedi(X) -> memeli(X)` |

Basit bir bilgi tabanını kodla hayal edelim. Aşağıdaki Python örneği, gerçekleri üçlü yapılar halinde tutar ve belirli bir ilişkiyi sorgular:

```python
facts = {
    ('Pamuk', 'tür', 'kedi'),
    ('Köpük', 'tür', 'köpek'),
    ('Ankara', 'başkentidir', 'Türkiye'),
    ('Pamuk', 'renk', 'beyaz')
}

def sorgula(özne=None, ilişki=None, nesne=None):
    sonuçlar = []
    for fact in facts:
        o, r, n = fact
        if özne is not None and o != özne:
            continue
        if ilişki is not None and r != ilişki:
            continue
        if nesne is not None and n != nesne:
            continue
        sonuçlar.append(fact)
    return sonuçlar

print(sorgula(özne='Pamuk'))
```

Bu kodun amacı, bilgi tabanındaki gerçekleri filtrelemektir. `Pamuk` hakkında ne biliyoruz diye sorduğumuzda sistem, onun türünü ve rengini döndürür. Henüz akıl yürütme yoktur; yalnızca kayıtlı gerçekler aranır. Ancak bu temel yapı üzerine kurallar eklendiğinde işler eğlenceli hale gelir.

Bir kuralı matematiksel olarak şöyle düşünebiliriz:

$kedi(x) \Rightarrow memeli(x)$

Bu ifade “Eğer x bir kediyse, x memelidir” der. `Pamuk` için $kedi(Pamuk)$ gerçeği varsa, sistem $memeli(Pamuk)$ sonucunu çıkarabilir. Buna çıkarım denir. Bilgi tabanı + kurallar = basit bir mantık motoru.

| Veri Tabanı | Bilgi Tabanı |
|---|---|
| Kayıt saklamaya odaklanır | Anlam ve çıkarıma odaklanır |
| Sorgular çoğunlukla doğrudandır | Sorgular kurallarla genişleyebilir |
| `SELECT * FROM hayvanlar` | `kedi(X) -> memeli(X)` |
| Daha çok operasyonel sistemlerde kullanılır | Yapay zekâ, uzman sistemler ve semantik web’de kullanılır |

Gerçeklerin kesin ve değişmez olması özellikle önemlidir. “Bugün hava sıcak” gibi bağlama bağlı ifadeler bilgi tabanına eklenebilir ama zaman, yer veya koşul belirtilmezse sorun çıkarır. Daha sağlam bir ifade şöyle olur: `sıcaklık(İstanbul, 2026-07-11, 30)`. Böylece gerçek, ölçülebilir ve izlenebilir hale gelir.

Bilgi tabanları; uzman sistemlerde hastalık teşhisi, oyun yapay zekâsında karakter davranışları, semantik aramada kavram ilişkileri ve robotikte çevre modelleme için kullanılır. Bir robotun “masa mutfaktadır” ve “bardak masanın üzerindedir” bilgilerini bilmesi, bardağı bulmak için mutfağa gitmesini sağlayabilir.

Özetle gerçekler, yazılıma dünyanın LEGO parçalarını verir. Kurallar ise bu parçaları nasıl birleştireceğini anlatır. İyi tasarlanmış bir bilgi tabanı, sadece bilgi depolayan değil, bildiklerinden sonuç çıkarabilen sistemlerin temelidir. Yani küçük gerçekler, doğru kurallarla birleştiğinde oldukça zeki davranışların kapısını aralar.
