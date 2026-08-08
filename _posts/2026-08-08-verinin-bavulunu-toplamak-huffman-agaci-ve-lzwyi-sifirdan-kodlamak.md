---
layout: post
title: "Verinin Bavulunu Toplamak: Huffman Ağacı ve LZW’yi Sıfırdan Kodlamak"
math: true
categories: 
  - Proje
tags: 
  - Huffman
  - LZW
  - veri sıkıştırma
---

Bir metin dosyasını küçültmek sihir değil; tekrarları ve olasılıkları akıllıca temsil etme sanatıdır. Bu projede kayıpsız sıkıştırmanın iki klasiğini, Huffman ağacını ve LZW algoritmasını Python ile sıfırdan kuracağız. Böylece hazır kütüphanelerin düğmesine basmak yerine makinenin veriyi nasıl “katladığını” göreceğiz.

``

## Kayıpsız sıkıştırma neyi amaçlar?

Kayıpsız algoritmalarda açılan veri, başlangıçtaki veriyle birebir aynıdır. Temel hedef, sık görülen örüntülere daha kısa; seyrek görülenlere daha uzun temsiller vermektir. Bir sembolün olasılığı $p(x)$ ise taşıdığı teorik bilgi miktarı:

$$I(x)=-\log_2 p(x)$$

olarak ifade edilir. Çok sık görülen bir karakterin sürpriz değeri düşük, ideal kodu da kısadır. Bir kodlamanın ortalama bit maliyeti ise

$$L=\sum_x p(x)\,l(x)$$

formülüyle hesaplanır. Buradaki $l(x)$, sembolün kod uzunluğudur.

| Özellik | Huffman | LZW |
|---|---|---|
| Temel fikir | Karakter sıklıkları | Tekrarlanan diziler |
| Veri yapısı | İkili ağaç | Dinamik sözlük |
| Ön analiz | Gerekir | Gerekmez |
| Güçlü olduğu veri | Sıklık dağılımı dengesiz metin | Çok tekrar içeren metin ve desenler |
| Çıktı | Değişken uzunluklu bit kodları | Sözlük indeksleri |

## Huffman ağacını oluşturmak

Huffman algoritması her karakterin frekansını sayar. En düşük frekanslı iki düğümü birleştirir ve bu işlemi tek kök kalana kadar sürdürür. Sol dallara `0`, sağ dallara `1` verdiğimizde hiçbir kod diğerinin öneki olmaz. Bu özellik, bit akışının ayraç kullanılmadan çözülebilmesini sağlar.

```python
from collections import Counter
import heapq
from itertools import count

def huffman_codes(text):
    frequencies = Counter(text)
    order = count()
    heap = []

    for char, frequency in frequencies.items():
        heapq.heappush(heap, (frequency, next(order), char))

    if len(heap) == 1:
        return {heap[0][2]: '0'}

    while len(heap) > 1:
        f1, _, left = heapq.heappop(heap)
        f2, _, right = heapq.heappop(heap)
        node = (left, right)
        heapq.heappush(heap, (f1 + f2, next(order), node))

    codes = {}

    def walk(node, prefix=''):
        if isinstance(node, str):
            codes[node] = prefix
            return
        walk(node[0], prefix + '0')
        walk(node[1], prefix + '1')

    walk(heap[0][2])
    return codes

text = 'muz kabuğu muz'
codes = huffman_codes(text)
encoded = ''.join(codes[ch] for ch in text)
print(codes)
print(encoded)
```

Öncelik kuyruğu, en hafif iki düğümü verimli biçimde seçer. Algoritmanın zaman karmaşıklığı, $k$ farklı sembol için yaklaşık $O(k\log k)$ olur. Gerçek bir dosya biçiminde kod tablosunun da çıktıyla birlikte saklanması gerektiğini unutmayın.

## LZW ile dizileri sözlüğe çevirmek

LZW karakter olasılıklarını ölçmez. Başlangıçta tek karakterlerden oluşan bir sözlük kurar; okuma sırasında karşılaştığı yeni dizileri sözlüğe ekler. Böylece `ABABABA` gibi tekrarlar, zamanla tek bir indeksle temsil edilir.

```python
def lzw_encode(text):
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256
    current = ''
    output = []

    for char in text:
        candidate = current + char
        if candidate in dictionary:
            current = candidate
        else:
            output.append(dictionary[current])
            dictionary[candidate] = next_code
            next_code += 1
            current = char

    if current:
        output.append(dictionary[current])
    return output

print(lzw_encode('TOBEORNOTTOBEORTOBEORNOT'))
```

Kod, bilinen en uzun diziyi `current` içinde büyütür. Bilinmeyen bir birleşim görüldüğünde mevcut dizinin indeksini çıktıya yollar ve yeni birleşimi öğrenir. Unicode metinlerde başlangıç sözlüğünü doğrudan karakterlerden üretmek veya metni önce UTF-8 baytlarına çevirmek daha güvenlidir.

## Hangisini seçmeliyiz?

Huffman tekil sembollerin dağılımından, LZW ise dizisel tekrarlardan yararlanır. Üstelik rakip olmak zorunda değillerdir: Bazı formatlar önce tekrarları sözlük yaklaşımıyla azaltıp ardından oluşan değerleri Huffman benzeri kodlamayla paketler. Deneyinizi büyütmek için sıkıştırılmış bit sayısını özgün boyutla karşılaştırın:

$$\text{oran}=\frac{\text{sıkıştırılmış boyut}}{\text{özgün boyut}}$$

Oranın $1$ değerinden küçük olması kazanç demektir; ancak sözlük, ağaç ve başlık maliyetlerini hesaba katmadan zafer ilan etmeyin. Sıkıştırma dünyasında bavulu küçültmek kadar, bavulun anahtarını yanında taşımak da önemlidir.
