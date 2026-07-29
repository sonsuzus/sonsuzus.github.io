---
layout: post
title: "Derleyicilerin Sabrı: Bir Program Kaç Kez Reddedilerek Öğrenilir?"
math: true
categories: 
  - Bilgi
tags: 
  - derleyiciler
  - hata mesajları
  - programlama eğitimi
---

Programlama öğrenirken derleyicinin kırmızı hata mesajları bazen kişisel bir eleştiri gibi hissedilir: “Yine olmadı!” Oysa derleyici öfkeli bir kapı görevlisi değil, son derece katı kuralları olan bir dil öğretmenidir. Programımızı her reddedişinde neyi henüz doğru ifade edemediğimizi gösterir. Bu nedenle başarılı bir program, çoğu zaman ilk denemede kabul edilen değil; geri bildirimlerle adım adım düzeltilen programdır.

``

## Reddedilmek neden öğrenmenin parçasıdır?

Derleyici, kaynak kodu makinenin çalıştırabileceği bir biçime dönüştürmeden önce sözdizimi ve tür kuralları gibi koşulları denetler. Bir koşul sağlanmadığında hata üretir. Bu süreç pedagojik açıdan bir **geri bildirim döngüsü** oluşturur:

1. Öğrenci bir çözüm tahmini geliştirir.
2. Tahmini kod biçiminde ifade eder.
3. Derleyici bu ifadeyi sınar.
4. Hata mesajı, tahmin ile dilin kuralları arasındaki farkı gösterir.
5. Öğrenci zihinsel modelini günceller.

Bunu basitçe şöyle gösterebiliriz:

$$\text{Kod} \rightarrow \text{Geri Bildirim} \rightarrow \text{Düzeltme} \rightarrow \text{Yeni Kod}$$

Öğrenme açısından önemli olan hata sayısını sıfırlamak değil, her denemeden elde edilen bilgiyi artırmaktır. Kabaca bir öğrenme verimi tanımlarsak:

$$V = \frac{\text{Kazanılan yeni bilgi}}{\text{Tekrarlanan deneme sayısı}}$$

Aynı değişikliği düşünmeden on kez yapmak düşük; hata mesajını okuyup varsayımı sınamak ise yüksek verimlidir.

## Bütün hatalar aynı değildir

| Hata türü | Derleyicinin söylediği | Öğrencinin öğrenebileceği |
|---|---|---|
| Sözdizimi hatası | “Bu cümle dil bilgisine uymuyor.” | Parantez, noktalı virgül ve anahtar kelime kuralları |
| Tür hatası | “Bu değer burada kullanılamaz.” | Veri türleri ve işlemlerin sınırları |
| Bağlama hatası | “Bu adı bulamıyorum.” | Kapsam, bildirim ve modül ilişkileri |
| Mantık hatası | Derleyici çoğunlukla sessizdir. | Test yazma, problem çözme ve algoritmik düşünme |

İlk üç grupta derleyici doğrudan yardımcı olabilir. Mantık hatalarında ise program geçerli olduğu hâlde yanlış sonuç üretir. Yani “derlendi” demek, “doğru çalışıyor” demek değildir.

## Bir hata mesajını laboratuvar notuna çevirmek

Aşağıdaki C++ kodunda bilinçli bir tür uyuşmazlığı vardır:

```cpp
#include <iostream>
#include <string>

int main() {
    std::string yas = "18";
    int gelecekYas = yas + 1;
    std::cout << gelecekYas;
}
```

Derleyici, `std::string` ile `int` değerlerinin bu şekilde toplanamayacağını söyler. Mesaj ilk bakışta uzun ve ürkütücü olabilir; ancak temel soru basittir: **Toplama işleminin iki tarafındaki türler nedir?** Metni önce sayıya dönüştürerek sorun çözülür:

```cpp
int gelecekYas = std::stoi(yas) + 1;
```

Burada yalnızca bir satır düzeltilmedi. Öğrenci, metin olarak saklanan `"18"` ile sayısal `18` arasındaki farkı keşfetti. İyi hata analizi, yamadan çok kavram üretir.

## Pedagojik olarak daha iyi hata alışkanlıkları

Hata mesajını görür görmez kodu rastgele değiştirmek yerine şu yöntem uygulanabilir:

- Önce mesajdaki **ilk hatayı** okuyun; sonraki hatalar onun zincirleme sonucu olabilir.
- Dosya ve satır numarasını bulun, fakat problemin bir önceki satırdan kaynaklanabileceğini unutmayın.
- “Derleyici ne bekliyordu, ne buldu?” sorusunu yazılı olarak cevaplayın.
- Aynı hatayı küçük bir örnekte yeniden üretin.
- Çözümden sonra hangi kuralı öğrendiğinizi tek cümleyle kaydedin.

| Verimsiz yaklaşım | Öğretici yaklaşım |
|---|---|
| Mesajı okumadan kodu değiştirmek | Hatanın anahtar bölümünü ayıklamak |
| Çözümü doğrudan kopyalamak | Çözümün neden çalıştığını açıklamak |
| Tüm dosyayı birden düzenlemek | Tek değişkeni değiştirip yeniden derlemek |
| Hatayı başarısızlık saymak | Hatayı sınanabilir geri bildirim saymak |

## Derleyicinin gerçek sabrı

Derleyici aslında sonsuz sabırlıdır: Aynı programı yüzüncü kez de aynı tarafsızlıkla inceler. Sabrı tükenen genellikle öğrencidir. Bu yüzden amaç, kaç kez reddedildiğimizi saymak değil, her ret ile sorumuzu daha kesin hâle getirmektir. Programlama ustalığı hatasız kod yazmak değil; hata ile karşılaşıldığında paniği yönteme, mesajı bilgiye ve reddedilmeyi yeni bir deneye dönüştürebilmektir.
