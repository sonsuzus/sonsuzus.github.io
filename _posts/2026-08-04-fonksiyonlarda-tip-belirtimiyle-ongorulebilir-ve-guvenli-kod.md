---
layout: post
title: "Fonksiyonlarda Tip Belirtimiyle Öngörülebilir ve Güvenli Kod"
math: true
categories: 
  - Bilgi
tags: 
  - tip güvenliği
  - fonksiyonlar
  - modüler programlama
---

Bir fonksiyonun yalnızca ne yaptığını değil, hangi verileri kabul edip hangi türde sonuç ürettiğini bilmek, yazılım geliştirmeyi tahmin oyunundan çıkarır. Parametre ve dönüş tipi belirtimleri; modüller arasındaki sözleşmeyi görünür kılar, hataları erkenden yakalar ve kod tamamlama araçlarını daha kullanışlı hâle getirir. Kısacası tipler, fonksiyonların kapısındaki “Giriş şartları ve çıkış garantisi” tabelasıdır.

``

## Fonksiyon sözleşmesi nedir?

Bir fonksiyonu matematiksel olarak $f: A \rightarrow B$ biçiminde düşünebiliriz. Burada $A$, fonksiyonun kabul ettiği değerler kümesini; $B$ ise üretebileceği sonuçlar kümesini temsil eder. Örneğin iki tam sayıyı toplayan bir fonksiyon şu sözleşmeye sahiptir:

$$topla: \mathbb{Z} \times \mathbb{Z} \rightarrow \mathbb{Z}$$

Bu ifade, iki tam sayı verildiğinde sonucun da tam sayı olacağını söyler. Programlama dillerindeki tip belirtimleri aynı fikri kaynak koda taşır. Böylece fonksiyonun davranışını anlamak için gövdesindeki her satırı okumak gerekmez.

TypeScript ile basit bir örnek:

```typescript
function topla(a: number, b: number): number {
  return a + b;
}

const sonuc = topla(12, 8);
```

Buradaki `a: number` ve `b: number` parametre sınırlarını, son `: number` ise dönüş garantisini belirtir. `topla("12", 8)` çağrısı çalışma aşamasına ulaşmadan hata verir. Böylece JavaScript’in sürprizli birleştirme davranışı yerine öngörülebilir toplama işlemi elde edilir.

## Tipli ve tipsiz yaklaşım

Tip belirtimi yalnızca sözdizimsel bir süs değildir. Özellikle birçok modülün ve geliştiricinin bulunduğu projelerde iletişim aracına dönüşür.

| Özellik | Belirtimsiz fonksiyon | Tipleri belirtilmiş fonksiyon |
|---|---|---|
| Hata zamanı | Genellikle çalışma zamanı | Çoğunlukla derleme veya analiz zamanı |
| Editör desteği | Sınırlı tahmin | Güçlü tamamlama ve uyarılar |
| Yeniden düzenleme | Daha riskli | Daha kontrollü |
| Dokümantasyon | Gövdeyi okumak gerekebilir | İmza önemli bilgi sağlar |
| Esneklik | Yüksek fakat belirsiz | Sınırları tanımlı |

Dinamik dillerde de aynı avantajlardan yararlanılabilir. Python tip ipuçları çalışma zamanında zorunlu doğrulama yapmasa da `mypy` ve benzeri araçlar tarafından denetlenebilir:

```python
def indirimli_fiyat(fiyat: float, oran: float) -> float:
    """Fiyata belirtilen oranda indirim uygular."""
    return fiyat * (1 - oran)

sonuc: float = indirimli_fiyat(250.0, 0.20)
```

Hesaplama $y = x(1-r)$ formülünü uygular. İmza sayesinde `fiyat` ve `oran` değerlerinin ondalıklı sayı, sonucun da `float` olması beklendiği hemen anlaşılır.

## Daha kesin modeller kurmak

Her şeyi `string`, `number` veya `object` olarak işaretlemek yeterli değildir. Alan modelini temsil eden özel tipler, geçersiz durumların oluşturulmasını zorlaştırır.

```typescript
type Kullanici = {
  id: number;
  ad: string;
  aktif: boolean;
};

function gorunenAd(kullanici: Kullanici): string {
  return kullanici.aktif
    ? kullanici.ad
    : `${kullanici.ad} (pasif)`;
}
```

Bu fonksiyon rastgele bir nesne değil, gerekli alanları taşıyan bir `Kullanici` ister. Dönüş değerinin daima metin olduğu da garanti edilir. Başka bir modül fonksiyonu kullanırken iç uygulamaya değil bu sözleşmeye bağımlı olur.

## Aşırı katılığa dikkat

Tip güvenliği, her fonksiyonu gereksiz ölçüde daraltmak anlamına gelmez. Aynı mantık farklı türlerle çalışıyorsa generic tipler kullanılabilir:

```typescript
function ilkEleman<T>(liste: T[]): T | undefined {
  return liste[0];
}
```

Buradaki `T`, esnekliği korurken giriş ve çıkış arasındaki ilişkiyi kaybetmez. Sayı listesi sayı, metin listesi metin döndürür. Boş liste ihtimali ise `undefined` ile açıkça modellenir.

Sonuç olarak iyi tip belirtimi, “Bu fonksiyon muhtemelen ne döndürür?” sorusunu ortadan kaldırır. Küçük projelerde okunabilirlik, büyük projelerde modüler güvenlik sağlar. En iyi yaklaşım; anlamlı alan tipleri oluşturmak, belirsiz `any` kullanımını azaltmak ve hata ihtimallerini dönüş tipinde açıkça ifade etmektir. Tipler kelepçe değil, kodun korkuluklarıdır: hareketi engellemez, uçurumdan düşmeyi önler.
