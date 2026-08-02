---
layout: post
title: "Yazılımda Teknik Borcun Ahlakı: Bugünün Kolaycılığı Yarının Kimin Sorumluluğu?"
math: true
categories: 
  - Bilgi
tags: 
  - teknik borç
  - yazılım etiği
  - sürdürülebilir yazılım
---

Teknik borç çoğu zaman eski kod, eksik test veya aceleyle verilmiş mimari kararlar şeklinde tanımlanır. Ancak mesele yalnızca kod kalitesi değildir. Bugün birkaç saat kazanmak için seçtiğimiz kestirme yol, aylar sonra sistemi devralan başka bir geliştiricinin gecesini, dikkatini ve hatta sağlığını tüketebilir. Bu nedenle teknik borç, ekonomik bir metafor olmanın ötesinde, yazılım ekiplerinin farklı kuşakları arasında aktarılan etik bir yükümlülüktür.
``

## Borç metaforu bize ne anlatır?

Ward Cunningham’ın popülerleştirdiği teknik borç kavramı, hızlı teslimat uğruna gelecekte ek maliyet doğuracak kararları anlatır. Finansal borçta olduğu gibi burada da bir **ana para** ve **faiz** vardır. Ana para, sorunu bugün düzgün biçimde çözmek için gereken emektir. Faiz ise kötü karar nedeniyle her değişiklikte ödediğimiz ek süredir.

Basitleştirilmiş bir model şöyle kurulabilir:

$$B(t) = B_0 + \sum_{i=1}^{t} F_i$$

Burada $B_0$ başlangıçtaki teknik borcu, $F_i$ ise her geliştirme döneminde ödenen faiz maliyetini temsil eder. Kod tabanı büyüdükçe bağımlılıklar çoğalır ve faiz doğrusal olmaktan çıkabilir:

$$B(t) = B_0(1+r)^t$$

Yani küçük görünen bir kestirme, yeterince uzun süre görmezden gelindiğinde minik bir TODO’dan kurumsal bir korku filmine dönüşebilir.

## Her teknik borç ahlaksızlık mıdır?

Hayır. Bazen pazara çıkmak, kritik bir hatayı durdurmak veya belirsizliği test etmek için bilinçli borç almak mantıklıdır. Etik sorun, borcun varlığından çok **gizlenmesi**, **kaydının tutulmaması** ve bedelinin karar sürecine katılmayan insanlara aktarılmasıdır.

| Karar türü | Etik açıdan kabul edilebilir yaklaşım | Sorunlu yaklaşım |
|---|---|---|
| Hızlı geçici çözüm | Riskleri belgelemek ve düzeltme tarihi belirlemek | Geçici çözümü kalıcıymış gibi sunmak |
| Testleri ertelemek | Kapsamı ve olası etkileri ekiple paylaşmak | Başarı ölçümlerini korumak için eksikleri saklamak |
| Eski sistemi kullanmak | Göç maliyetini gerçekçi biçimde planlamak | Bakım yükünü yeni çalışanlara bırakmak |
| Teslim baskısı | Ürün, yönetim ve teknik ekibin ortak karar vermesi | Geliştiriciyi sessizce kaliteyi düşürmeye zorlamak |

Bu ayrım niyet kadar yönetişimle de ilgilidir. Kim karar verdi, kim fayda sağladı ve faturayı kim ödeyecek? Etik değerlendirme bu üç soruyu birlikte sormalıdır.

## Kodda görünmeyen sorumluluk

Aşağıdaki örnek çalışır, fakat hatayı sessizce yutarak gelecekteki geliştiriciye belirsizlik bırakır:

```python
def kullaniciyi_getir(veritabani, kullanici_id):
    try:
        return veritabani.find(kullanici_id)
    except Exception:
        return None
```

`None` sonucunun kullanıcının bulunamadığı mı, bağlantının koptuğu mu, yoksa programlama hatası mı olduğu bilinmez. Daha sorumlu yaklaşım, beklenen durumları ayırır ve beklenmeyen hataları görünür kılar:

```python
class KullaniciBulunamadi(Exception):
    pass

def kullaniciyi_getir(veritabani, kullanici_id):
    kayit = veritabani.find(kullanici_id)
    if kayit is None:
        raise KullaniciBulunamadi(kullanici_id)
    return kayit
```

Bu sürüm biraz daha fazla kod içerir; fakat davranışın anlamını açıklar. Temiz kod yalnızca estetik değildir: Başka insanların zamanı üzerinde kurduğumuz etkinin sınırlandırılmasıdır.

## Nesiller arası adalet için pratikler

Teknik borcu etik biçimde yönetmek için borç kayıtları tutulmalı, mimari kararlar gerekçeleriyle belgelenmeli ve refaktör çalışmaları planlamada görünür olmalıdır. Kod incelemelerinde yalnızca “çalışıyor mu?” değil, “bunu altı ay sonra devralan kişi anlayabilecek mi?” sorusu da sorulmalıdır. Ayrıca bakım işi görünmez kahramanlık olarak değil, ürün geliştirme faaliyetinin parçası olarak değerlendirilmelidir.

Sonuçta hiçbir kod sonsuza kadar temiz kalmaz. Etik sorumluluk kusursuz sistemler üretmek değil; aldığımız kestirmelerin bedelini dürüstçe göstermek, faydayı bugün toplarken maliyeti yarının isimsiz geliştiricilerine bırakmamaktır. Git geçmişi unutabilir, ekip değişebilir; fakat kötü kararların faizi düzenli çalışır.
