---
layout: post
title: "Compiler Optimizasyonlarının Görünmez Eli: Yazdığın Kod ile Çalışan Kod Arasındaki Fark"
math: true
categories: 
  - Bilgi
tags: 
  - compiler
  - optimizasyon
  - soyutlama
---

Bir programcı kaynak koda bakar ve bilgisayarın satırları sırayla uyguladığını hayal eder. Oysa modern bir compiler, kodu harfiyen yerine getiren sadık bir tercüman değil; davranışı koruduğu sürece programı yeniden düzenleyebilen son derece girişken bir mühendistir. Yazdığımız kod niyetimizi, çalışan makine kodu ise compiler’ın bu niyetten çıkardığı sonucu temsil eder.
``
## Kaynak Kod Bir Sözleşmedir

C, C++, Rust veya Java gibi dillerde kaynak kod çoğunlukla işlemcinin doğrudan uygulayacağı talimatlar listesi değildir. Dil standardı tarafından tanımlanan bir **soyut makineye** verilmiş tariftir. Compiler bu tarifi ara temsillere dönüştürür; sabitleri hesaplar, gereksiz işlemleri siler, döngüleri açar ve komutların sırasını değiştirebilir.

Bunu mümkün kılan temel yaklaşım **as-if kuralıdır**: Dışarıdan gözlemlenebilen davranış değişmiyorsa dönüşüm serbesttir. Basitleştirilmiş biçimiyle compiler şu hedefi arar:

$$P_{kaynak}(x) \equiv P_{makine}(x)$$

Buradaki eşitlik, iki programın aynı komutları çalıştırmasını değil, tanımlı girdiler için aynı gözlemlenebilir sonucu üretmesini ifade eder. Aradaki yöntem tamamen farklı olabilir.

| Programcının gördüğü | Compiler’ın görebileceği |
|---|---|
| Değişkenler | Register değerleri ve veri akışı |
| Fonksiyon çağrısı | Inline edilmiş ifadeler |
| Döngü | Vektör komutları veya kapalı formül |
| Yazılı işlem sırası | Bağımlılıkların izin verdiği yeni sıra |
| Kullanılmayan hesaplama | Silinebilir kod |

## Bir Döngü Nereye Kaybolur?

Aşağıdaki C fonksiyonu, ilk `n` doğal sayının toplamını döngüyle hesaplıyor:

```c
unsigned sum(unsigned n) {
    unsigned result = 0;

    for (unsigned i = 0; i < n; ++i) {
        result += i;
    }

    return result;
}
```

Optimize edilmemiş çıktıda toplama ve karşılaştırma komutlarını görmek mümkündür. Güçlü optimizasyonda compiler, döngünün matematiksel anlamını keşfedip onu şu ifadeye yaklaştırabilir:

$$\sum_{i=0}^{n-1} i = \frac{n(n-1)}{2}$$

Böylece $O(n)$ adımlık görünen iş, birkaç makine komutuna dönüşebilir. Kaynak koddaki döngü gerçektir; fakat çalışma zamanında var olmak zorunda değildir. Bu durum hata değil, sözleşmenin başarıyla uygulanmasıdır.

## Güvenin Kırıldığı Yer: Tanımsız Davranış

Soyutlama katmanına duyulan güven, dil kurallarını bildiğimiz varsayımına dayanır. Özellikle C ve C++ dünyasındaki **tanımsız davranış**, compiler’a beklenmedik çıkarımlar yapma fırsatı verir:

```c
int greater_after_increment(int x) {
    return x + 1 > x;
}
```

Matematikte bu ifade her zaman doğrudur. Ancak sabit genişlikte işaretli tamsayı taşabilir. C standardında signed overflow tanımsız olduğu için compiler, tanımlı bir programda taşma gerçekleşmeyeceğini varsayıp fonksiyonu doğrudan `1` döndürecek şekilde optimize edebilir.

| Durum | Programcı sezgisi | Compiler varsayımı |
|---|---|---|
| Signed overflow | Değer başa sarar | Gerçekleşemez; davranış tanımsızdır |
| Kullanılmayan sonuç | İşlem yine yapılır | Yan etkisi yoksa silinebilir |
| Eşzamanlı erişim | Komut sırası yeterlidir | Bellek modeli ve atomiklik belirleyicidir |
| Boş pointer erişimi | Belki hata döner | Geçerli program bunu yapmaz |

## Soyutlama Güveni Nasıl Şekillendirir?

Yüksek seviyeli diller bizi register tahsisinden ve komut zamanlamasından kurtarır. Bu özgürlük üretkenliği artırırken kontrol hissini azaltabilir. Debug derlemesinde çalışan, release derlemesinde bozulan kod genellikle compiler’ın “fazla akıllı” olmasından değil; programın gizli bir varsayımının optimizasyonla görünür hâle gelmesinden kaynaklanır.

Sağlıklı güven, compiler’ın hiçbir şeyi değiştirmeyeceğine inanmak değildir. Dil standardı, bellek modeli ve gözlemlenebilir davranış sınırlarını anlayarak compiler’ın **hangi değişiklikleri yapabileceğini** bilmektir. Assembly çıktısını incelemek, sanitizers kullanmak ve farklı optimizasyon seviyelerinde test yapmak bu zihinsel modeli güçlendirir.

Sonuçta compiler görünmez bir eldir; fakat mistik değildir. Kaynak kod niyet, dil standardı sözleşme, makine kodu ise pazarlık sonunda ortaya çıkan üründür. İyi programcı yalnızca kod yazmaz; hangi soyutlama katmanına neden güvendiğini de bilir.
