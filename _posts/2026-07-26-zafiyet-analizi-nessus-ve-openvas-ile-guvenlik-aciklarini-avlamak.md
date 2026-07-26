---
layout: post
title: "Zafiyet Analizi: Nessus ve OpenVAS ile Güvenlik Açıklarını Avlamak"
math: true
categories: 
  - Bilgi
tags: 
  - zafiyet-analizi
  - nessus
  - openvas
  - siber-guvenlik
  - cvss
---

Bir ağdaki güvenlik açıklarını elle bulmaya çalışmak, karanlık bir odada LEGO parçası aramaya benzer: mutlaka bir şeye basarsın ama acı biraz geç gelir. Zafiyet analizi, Nessus veya OpenVAS gibi entegre tarayıcılarla sistemlerdeki bilinen güvenlik açıklarının otomatik tespit edilmesi, önceliklendirilmesi ve raporlanması sürecidir. Amaç saldırmak değil; saldırganlardan önce eksikleri görmek, ölçmek ve kapatmaktır.
``

## Zafiyet Analizi Tam Olarak Neyi Ölçer?

Zafiyet, bir varlığın tehdit tarafından istismar edilebilecek zayıf noktasıdır. Bu bir eski OpenSSL sürümü, yanlış yapılandırılmış SSH servisi, varsayılan parola, açık bir yönetim paneli veya eksik güvenlik yaması olabilir. Tarayıcılar genellikle şu mantıkla çalışır: önce hedefi keşfeder, portları ve servisleri belirler, servis sürümlerini parmak iziyle tanır, sonra bunları CVE veritabanları ve test eklentileriyle eşleştirir.

Basit risk düşüncesi şu formülle özetlenebilir: $Risk = Olasılık \times Etki$. CVSS puanı da bu fikri standardize eder. Örneğin CVSS 9.8 olan uzaktan kod çalıştırma açığı, CVSS 4.3 olan bilgi sızıntısından genellikle daha acildir. Ancak bağlam kritiktir: internete açık bir düşük puanlı açıklık, iç ağdaki yüksek puanlı ama erişilemeyen açıklıktan daha riskli olabilir.

| Kavram | Anlamı | Pratik Etkisi |
|---|---|---|
| CVE | Açığın evrensel kimliği | Aynı açıklığı herkes aynı adla takip eder |
| CVSS | Açığın teknik şiddet puanı | Önceliklendirme için başlangıç sağlar |
| False Positive | Var sanılan ama gerçekte olmayan açık | Zaman kaybettirir, doğrulama gerekir |
| Remediation | Açığı giderme aksiyonu | Yama, yapılandırma veya erişim kısıtı uygulanır |

## Nessus ve OpenVAS: İki Popüler Tarayıcı

Nessus, ticari dünyada güçlü eklenti ekosistemi ve kullanıcı dostu raporlarıyla bilinir. OpenVAS, Greenbone Community Edition altında açık kaynak yaklaşımıyla öne çıkar. İkisi de tarama profilleri, kimlik bilgili tarama, raporlama ve zafiyet doğrulama özellikleri sunar.

| Özellik | Nessus | OpenVAS |
|---|---|---|
| Lisans | Ticari seçenekler ağırlıklı | Açık kaynak topluluk sürümü mevcut |
| Kullanım Kolaylığı | Arayüz ve raporlar oldukça olgun | Kurulum ve bakım biraz daha emek ister |
| Eklenti Güncellemeleri | Hızlı ve düzenli | Feed güncellemelerine bağlı |
| Uygun Senaryo | Kurumsal raporlama, denetim | Laboratuvar, eğitim, bütçe dostu analiz |

## Tarama Süreci Nasıl İlerler?

Tipik akış dört adımdır: kapsam belirleme, tarama, doğrulama ve iyileştirme. Kapsamda hangi IP aralıklarının, alan adlarının veya uygulamaların taranacağı netleştirilir. İzinsiz tarama hukuki ve etik sorun doğurur; bu yüzden her zaman yazılı izin ve zaman penceresi belirlenmelidir.

| Aşama | Soru | Çıktı |
|---|---|---|
| Keşif | Hangi varlıklar var? | IP, port, servis listesi |
| Eşleştirme | Hangi sürüm neye açık? | CVE ve bulgu listesi |
| Önceliklendirme | Önce ne kapanmalı? | Kritik-yüksek-orta sıralaması |
| Takip | Açık kapandı mı? | Yeniden tarama raporu |

Kimlik bilgili tarama özellikle değerlidir. Tarayıcı sisteme SSH, WinRM veya agent benzeri yöntemlerle giriş yapabildiğinde yalnızca dışarıdan görünen servisleri değil, kurulu paketleri, eksik yamaları ve yerel yapılandırmaları da denetler. Bu, röntgen ile fotoğraf arasındaki fark gibidir.

## Raporları Makineyle Okumak

Tarayıcıların CSV veya XML raporları otomasyon için harika malzemedir. Aşağıdaki Python örneği, CSV raporundaki bulguları CVSS puanına göre sıralar ve kritik olanları öne çıkarır. Amaç saldırı yapmak değil, iyileştirme kuyruğunu yönetmektir.

```python
import csv

with open('vulnerability_report.csv', newline='', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))

findings = []
for row in rows:
    cvss = float(row.get('CVSS', 0) or 0)
    findings.append({
        'host': row.get('Host'),
        'name': row.get('Name'),
        'cvss': cvss,
        'solution': row.get('Solution')
    })

for item in sorted(findings, key=lambda x: x['cvss'], reverse=True):
    if item['cvss'] >= 7.0:
        print(f"[{item['cvss']}] {item['host']} - {item['name']}")
```

Bu kod, güvenlik ekibinin önce yüksek riskli bulgulara odaklanmasına yardım eder. Gerçek ortamda buna varlık kritiklik değeri de eklenebilir: $Öncelik = CVSS \times VarlıkKritikliği$. Böylece ödeme sistemi ile test sunucusu aynı kefeye konmaz.

## İyi Analizin Sırrı: Tarayıcıya Körü Körüne Güvenmemek

Zafiyet tarayıcıları çok güçlüdür ama sihirli değnek değildir. Yanlış pozitifler, eksik envanter, kapalı portlar, WAF etkisi veya hatalı kimlik bilgileri sonuçları bozabilir. Bu yüzden raporlar mutlaka doğrulanmalı, iş etkisiyle yorumlanmalı ve düzeltmeler yeniden taramayla teyit edilmelidir.

Sonuç olarak Nessus ve OpenVAS, güvenlik açıklarını görünür kılan radar sistemleridir. Radar düşmanı durdurmaz; ama nereden geldiğini gösterir. Düzenli tarama, doğru önceliklendirme ve disiplinli iyileştirme döngüsüyle zafiyet analizi, kurum güvenliğinin en pratik ve ölçülebilir alışkanlıklarından biri haline gelir.
