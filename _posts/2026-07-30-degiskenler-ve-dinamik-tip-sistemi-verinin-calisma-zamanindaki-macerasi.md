---
layout: post
title: "Değişkenler ve Dinamik Tip Sistemi: Verinin Çalışma Zamanındaki Macerası"
math: true
categories: 
  - Bilgi
tags: 
  - değişkenler
  - dinamik tipleme
  - bellek yönetimi
---

Dinamik tip sistemine sahip bir dilde değişken oluşturmak, boş bir kutunun üzerine etiket yapıştırmaya benzer. Kutunun içine önce sayı, ardından metin koyabiliriz; dil, içeriğin türünü çalışma zamanında kendisi belirler. Bu rahatlığın arkasında ise tip etiketleri, nesne başlıkları, referanslar ve çöp toplama gibi oldukça hareketli bir bellek düzeni bulunur.
``
## Değişken, değer ve tip birbirinden farklıdır

Python, JavaScript ve Ruby gibi dinamik tipli dillerde değişkenin kendisi çoğunlukla belirli bir veri türüne sahip değildir. Değişken, bellekte bulunan bir **değere referans** taşır; veri türü ise o değerle ilişkilendirilir.

```python
veri = 42          # veri, bir tam sayı nesnesine bağlanır
veri = "Merhaba"  # artık bir metin nesnesine bağlanır
```

İkinci atama sırasında aynı bellek bölgesinin sihirli biçimde metne dönüştürülmesi gerekmez. Çalışma zamanı yeni bir metin nesnesi oluşturur ve `veri` adının referansını bu nesneye yönlendirir. Eski `42` nesnesine başka bir referans yoksa nesne daha sonra bellekten temizlenebilir.

| Özellik | Statik tip sistemi | Dinamik tip sistemi |
|---|---|---|
| Tip kontrolü | Genellikle derleme sırasında | Çalışma sırasında |
| Değişken bildirimi | Tip çoğunlukla açıkça belirtilir | Tip yazmak genellikle gerekmez |
| Tip değiştirme | Sınırlı veya açık dönüşüm ister | Aynı ad farklı türlere bağlanabilir |
| Hata zamanı | Daha erken yakalanabilir | İlgili satır çalışınca görülebilir |
| Esneklik | Daha kontrollü | Hızlı ve esnek |

## Bellekte gerçekte ne saklanır?

Basitleştirilmiş bir dinamik dil nesnesini şu şekilde düşünebiliriz:

$$Nesne = TipEtiketi + Deger + YonetimBilgisi$$

Tip etiketi, çalışma zamanına verinin sayı mı, metin mi veya başka bir nesne mi olduğunu söyler. Yönetim bilgisi; nesnenin boyutu, referans sayısı ya da çöp toplayıcının kullandığı işaretler olabilir. Bu nedenle yalnızca `5` değerini saklayan dinamik bir nesne, ham makine tamsayısından daha fazla bellek tüketebilir.

Bir değişkenin nesneye bağlanmasını ise kavramsal olarak şöyle gösterebiliriz:

$$degisken \rightarrow referans \rightarrow nesne$$

Aynı nesneye birden fazla değişken işaret edebilir:

```python
a = [10, 20]
b = a
b.append(30)
print(a)  # [10, 20, 30]
```

Burada liste kopyalanmamıştır. `a` ve `b`, aynı liste nesnesine referans verir. Bu davranış performans kazandırırken beklenmedik değişikliklere de yol açabilir. Gerçek bir kopya gerekiyorsa dilin kopyalama araçları kullanılmalıdır.

## Sayısal veriler nasıl işlenir?

Bir ifade çalıştırıldığında çalışma zamanı operandların tiplerini inceler ve uygun işlemi seçer:

```python
sonuc = 8 + 4       # sayısal toplama: 12
metin = "8" + "4"  # metin birleştirme: "84"
```

İşlem sembolü aynı olsa da uygulanan davranış farklıdır. Bu yaklaşıma operatör aşırı yükleme veya tipe göre gönderim denebilir. Farklı türlerin karıştırılması ise dilin kurallarına bağlıdır. Python, `8 + "4"` ifadesinde hata verirken JavaScript bazı durumlarda otomatik dönüşüm gerçekleştirir.

| İfade | Olası yorum | Sonuç |
|---|---|---|
| `8 + 4` | Sayısal toplama | `12` |
| `"8" + "4"` | Metin birleştirme | `"84"` |
| `int("8") + 4` | Açık tip dönüşümü | `12` |

Açık dönüşüm, niyeti görünür kıldığı için sürprizleri azaltır.

## Metinler ve değişmezlik

Metinler birçok dilde **değişmez** nesnelerdir. Bir metni güncellediğimizi düşündüğümüzde çoğunlukla yeni bir nesne üretilir:

```python
mesaj = "Merhaba"
mesaj = mesaj + " dünya"
```

İkinci satır yeni bir metin oluşturur ve `mesaj` referansını ona bağlar. Çok sayıda metni döngü içinde `+` ile birleştirmek bu nedenle maliyetli olabilir. Parçaları listede toplayıp `join` kullanmak genellikle daha verimlidir.

## Esnekliğin bedeli

Dinamik tipleme hızlı prototipleme, kısa kod ve esnek veri işleme sağlar. Buna karşılık tip hataları çalışma zamanına kalabilir ve her işlemde tip kontrolü ek maliyet oluşturabilir. Modern yorumlayıcılar; önbellekleme, çalışma zamanı uzmanlaştırması ve JIT derleme sayesinde bu maliyeti azaltır.

Sonuç olarak dinamik tip sistemi “tipsiz” değildir; tip bilgisini değişkenden değere ve derleme anından çalışma zamanına taşır. Bu ayrımı anlamak, hem bellek davranışlarını çözmeyi hem de daha güvenli, hızlı ve şaşırtmayan programlar yazmayı kolaylaştırır.
