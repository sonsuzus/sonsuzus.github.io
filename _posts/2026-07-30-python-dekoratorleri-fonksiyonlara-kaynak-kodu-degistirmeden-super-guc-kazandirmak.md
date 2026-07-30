---
layout: post
title: "Python Dekoratörleri: Fonksiyonlara Kaynak Kodu Değiştirmeden Süper Güç Kazandırmak"
math: true
categories: 
  - Bilgi
tags: 
  - Python
  - Dekoratörler
  - İleri Düzey Fonksiyonlar
---

Bir fonksiyona zaman ölçümü, yetki kontrolü veya kayıt tutma özelliği eklemek istediğinizi düşünün. Aynı kodları her fonksiyonun içine yerleştirmek çalışır; ancak kısa sürede bakım kâbusuna dönüşür. Python dekoratörleri, mevcut fonksiyonun kaynak kodunu değiştirmeden onu başka bir fonksiyonla sarar ve yeni davranışlar kazandırır. Kısacası dekoratör, fonksiyonunuzun üzerine giydirilen akıllı bir monttur.
``
## Teorik temel: Fonksiyonlar da birer nesnedir

Python'da fonksiyonlar **birinci sınıf nesnelerdir**. Bir değişkene atanabilir, başka bir fonksiyona argüman olarak gönderilebilir ve sonuç olarak döndürülebilirler. Başka fonksiyonlarla çalışan bu yapılara **yüksek mertebeden fonksiyonlar** denir.

Matematiksel olarak bir dekoratörü şöyle gösterebiliriz:

$$D(f) = g$$

Burada $f$ orijinal fonksiyon, $D$ dekoratör ve $g$ ek davranışlarla donatılmış yeni fonksiyondur. Kullanıcı $g(x)$ çağırdığında, sarmalayıcı gerekli işlemleri yapar ve çoğunlukla içeride $f(x)$ çağrısını gerçekleştirir.

```python
def selamla(isim):
    return f'Merhaba, {isim}!'

fonksiyon = selamla
print(fonksiyon('Ada'))
```

Bu örnekte fonksiyon çalıştırılmadan `fonksiyon` değişkenine aktarılır. Parantez kullanılsaydı fonksiyonun kendisi değil, ürettiği sonuç atanırdı.

| İfade | Anlamı | Sonuç |
|---|---|---|
| `selamla` | Fonksiyon nesnesi | Taşınabilir veya sarılabilir |
| `selamla('Ada')` | Fonksiyon çağrısı | Bir değer üretir |
| `dekorator(selamla)` | Fonksiyonu dönüştürme | Yeni bir fonksiyon döndürür |
| `@dekorator` | Sözdizimsel kısayol | Otomatik sarma sağlar |

## İlk dekoratörümüz

Bir dekoratör genellikle dış fonksiyon ve onun içindeki `wrapper` fonksiyonundan oluşur. İç fonksiyonun dış kapsamdaki `fonksiyon` değişkenini hatırlamasına **closure**, yani kapanış denir.

```python
from functools import wraps
from time import perf_counter

def sure_olc(fonksiyon):
    @wraps(fonksiyon)
    def wrapper(*args, **kwargs):
        baslangic = perf_counter()
        sonuc = fonksiyon(*args, **kwargs)
        sure = perf_counter() - baslangic
        print(f'{fonksiyon.__name__}: {sure:.6f} saniye')
        return sonuc
    return wrapper

@sure_olc
def kareler_toplami(n):
    return sum(i * i for i in range(n))

print(kareler_toplami(100_000))
```

`*args` konumsal, `**kwargs` ise isimlendirilmiş argümanları yakalar. Böylece dekoratör yalnızca belirli imzaya sahip fonksiyonlarla sınırlı kalmaz. `return sonuc` satırı da kritiktir; unutulursa orijinal fonksiyon değer üretse bile dışarıya `None` döner.

`@wraps`, sarılan fonksiyonun `__name__` ve dokümantasyon gibi metaverilerini korur. Onsuz hata kayıtlarında sürekli `wrapper` adını görmek, aynı kostümü giymiş oyuncuları ayırt etmeye çalışmaya benzer.

## Parametre alan dekoratörler

Dekoratörün kendisine ayar vermek için bir katman daha gerekir. Aşağıdaki yapı, fonksiyonun kaç kez çalıştırılacağını belirler:

```python
from functools import wraps

def tekrarla(adet):
    def dekorator(fonksiyon):
        @wraps(fonksiyon)
        def wrapper(*args, **kwargs):
            sonuc = None
            for _ in range(adet):
                sonuc = fonksiyon(*args, **kwargs)
            return sonuc
        return wrapper
    return dekorator

@tekrarla(3)
def bildirim(mesaj):
    print(mesaj)

bildirim('Sunucu ayakta!')
```

Buradaki değerlendirme sırası $tekrarla(3) \rightarrow dekorator \rightarrow wrapper$ şeklindedir. Yani önce yapılandırılmış dekoratör üretilir, ardından hedef fonksiyon sarılır.

## Dekoratör mü, normal fonksiyon mu?

| İhtiyaç | Dekoratör | Normal yardımcı fonksiyon |
|---|---:|---:|
| Birçok çağrıda ortak kontrol | Çok uygun | Tekrar oluşturabilir |
| Fonksiyon davranışını şeffafça genişletme | Uygun | Çağrı biçimini değiştirir |
| Basit ve tek seferlik işlem | Gereksiz olabilir | Daha okunaklıdır |
| Loglama, önbellekleme, yetkilendirme | İdeal | Dağınık kod üretebilir |

Birden fazla dekoratör üst üste kullanılabilir. `@A` satırının altında `@B` varsa dönüşüm $A(B(f))$ biçimindedir; dolayısıyla çalışma sırası her zaman dikkatle değerlendirilmelidir.

Dekoratörler güçlüdür ama sihir değildir. Gizli yan etkiler, aşırı katman ve belirsiz isimler hata ayıklamayı zorlaştırır. En iyi dekoratör; tek sorumluluğu olan, metaveriyi koruyan, sonucu doğru döndüren ve davranışını isminden belli eden dekoratördür. Doğru kullanıldığında fonksiyonları değiştirmek yerine yeteneklerini zarifçe genişletir.
