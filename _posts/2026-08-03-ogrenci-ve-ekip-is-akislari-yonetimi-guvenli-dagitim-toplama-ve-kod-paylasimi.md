---
layout: post
title: "Öğrenci ve Ekip İş Akışları Yönetimi: Güvenli Dağıtım, Toplama ve Kod Paylaşımı"
math: true
categories: 
  - Proje
tags: 
  - iş akışı yönetimi
  - Git
  - rol tabanlı erişim
---

Kalabalık bir sınıfta yüz ödevi toplamak veya büyük bir geliştirici ekibinde ortak kod tabanını yönetmek, yalnızca dosya paylaşmak değildir. Kim neyi görebilir, hangi değişikliği yapabilir ve teslim edilen çalışma nasıl doğrulanır? Sağlam bir iş akışı; hiyerarşi, otomasyon, izlenebilirlik ve en az yetki ilkelerini birlikte kullanarak dijital koridordaki kargaşayı düzenli bir üretim hattına dönüştürür.
``
## Önce hiyerarşiyi tasarlayın

İyi bir sistemde yetki, kişiye rastgele verilmez; role bağlanır. Bu yaklaşım **Rol Tabanlı Erişim Kontrolü**, yani RBAC olarak bilinir. Bir üniversitede yönetici, öğretim görevlisi, asistan ve öğrenci; yazılım takımında ise organizasyon yöneticisi, takım lideri, geliştirici ve gözlemci rolleri bulunabilir.

Bir kullanıcının etkin izin kümesini basitçe şöyle gösterebiliriz:

$$P(u)=\bigcup_{r \in R(u)} P(r)$$

Burada $R(u)$ kullanıcının rollerini, $P(r)$ ise ilgili rolün izinlerini temsil eder. Ancak güvenli tasarımda amaç, bu kümenin mümkün olduğunca küçük tutulmasıdır. Buna **en az yetki ilkesi** denir: Öğrenci ana dalı değiştirememeli, geliştirici de ihtiyaç duymadığı üretim sunucusuna erişememelidir.

| Rol | Okuma | Değişiklik gönderme | Birleştirme | Yetki yönetimi |
|---|---:|---:|---:|---:|
| Öğrenci / Geliştirici | Evet | Kendi dalına | Hayır | Hayır |
| Asistan / Takım lideri | Evet | Evet | Kontrollü | Hayır |
| Eğitmen / Yönetici | Evet | Evet | Evet | Evet |
| Otomasyon hesabı | Sınırlı | Sonuç ve rapor | Koşullu | Hayır |

## Dağıtım modeli: Şablondan kişisel alana

Ödev veya proje dağıtılırken herkesin aynı ortak klasörde çalışması, yanlışlıkla dosya silme yarışmasına dönüşebilir. Bunun yerine bir **şablon depo** hazırlanmalı ve her öğrenci ya da ekip için özel depo üretilmelidir. Takımların ortak çalışması gerekiyorsa her takıma ayrı alan açılmalıdır.

Önerilen yapı şöyledir:

1. Eğitmen veya lider, salt okunur başlangıç şablonunu hazırlar.
2. Otomasyon, kullanıcı ya da takım başına depo oluşturur.
3. Katılımcılar korumalı ana dal yerine özellik dallarında çalışır.
4. Değişiklikler pull request üzerinden incelemeye girer.
5. Testler başarılı olmadan birleştirme engellenir.

Bu model hem kopya veya bilgi sızıntısı riskini azaltır hem de kimin hangi satırı ne zaman değiştirdiğini gösterir.

## Teslimat kapısı olarak CI

Sürekli entegrasyon sistemi, yorulmayan bir dijital asistan gibi davranır. Kod derlenir, testler çalıştırılır, biçim denetlenir ve sonuç raporlanır. Örneğin aşağıdaki GitHub Actions iş akışı, her gönderimde Python testlerini çalıştırır:

```yaml
name: Otomatik Kontrol
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - run: pip install -r requirements.txt
      - run: pytest --junitxml=test-sonuclari.xml
```

Bu kod, depoyu geçici bir makineye alır, bağımlılıkları kurar ve test raporu üretir. Otomasyon hesabına yazma veya yönetici izni vermek yerine yalnızca gereken okuma ve raporlama izinleri tanınmalıdır.

## Toplama ve değerlendirme stratejisi

Teslim anı yalnızca son dosyanın alınması değildir. Commit geçmişi, test sonucu, inceleme konuşmaları ve teslim etiketi birlikte saklanmalıdır. Son tarih geldiğinde depo silinmemeli; yazma izni kaldırılmalı veya belirli commit kimliği kayıt altına alınmalıdır. Böylece sonradan yapılan değişiklikler özgün teslimi etkileyemez.

İş yükünü tahmin etmek için toplam inceleme süresi yaklaşık olarak

$$T = N \times (t_k + t_g)$$

şeklinde hesaplanabilir. Burada $N$ teslim sayısı, $t_k$ otomatik kontrol sonrası kalan kod inceleme süresi, $t_g$ ise geri bildirim süresidir. Otomasyon $t_k$ değerini düşürür; fakat tasarım kalitesini ve açıklamaları değerlendiren insan incelemesinin yerini tamamen alamaz.

## Küçük ama kritik güvenlik listesi

- Ana dallarda doğrudan gönderimi kapatın.
- En az bir onay ve başarılı test koşulu belirleyin.
- API anahtarlarını depoya değil, şifreli secret kasasına koyun.
- Mezun olan veya ekipten ayrılan kişilerin erişimini otomatik kaldırın.
- Yedekleme, arşivleme ve veri saklama sürelerini önceden tanımlayın.
- Denetim kayıtlarını düzenli olarak inceleyin.

Doğru iş akışı insanları kısıtlayan bir bürokrasi değil, hataların etkisini küçülten güvenlik ağıdır. Roller açık, depolar ayrılmış, teslimler etiketlenmiş ve testler otomatik olduğunda yüz kişilik bir sınıf da hızlı büyüyen bir yazılım ekibi de düzenini koruyabilir.
