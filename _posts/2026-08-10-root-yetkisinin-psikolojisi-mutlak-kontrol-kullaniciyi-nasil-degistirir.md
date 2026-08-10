---
layout: post
title: "Root Yetkisinin Psikolojisi: Mutlak Kontrol Kullanıcıyı Nasıl Değiştirir?"
math: true
categories: 
  - Bilgi
tags: 
  - siber güvenlik
  - root yetkisi
  - sistem yönetimi
  - insan faktörleri
  - psikoloji
---

Root yetkisi teknik olarak bir erişim seviyesi, psikolojik olarak ise kararların sonuçlarını doğrudan üretme gücüdür. Bir dosyayı silmek, servisi durdurmak veya güvenlik politikasını değiştirmek için onay beklemeyen kişi, zamanla sistemi yalnızca yönetilen bir yapı değil, kendi iradesinin uzantısı gibi algılayabilir. Bu algı verimliliği artırırken dikkat, sorumluluk ve risk değerlendirmesi üzerinde beklenmedik etkiler yaratır.
``

Unix dünyasında root, erişim kontrolünün tepesindedir: izin denetimlerini aşabilir, süreçleri sonlandırabilir ve çekirdek davranışını dolaylı biçimde etkileyebilir. Bu güç teknik açıdan `UID=0` ile temsil edilse de davranışsal sonuçları daha geniştir. Kullanıcının algıladığı kontrol seviyesi yükseldikçe, bir işlemin geri döndürülemez maliyetini küçümseme riski de artabilir.

Bunu basit bir risk modeliyle düşünebiliriz:

$$R = P(hata) \times E(etki)$$

Root kullanıcısında küçük bir komut hatasının etki değeri yüksektir. Örneğin normal kullanıcıyla yanlış dizini silmek kişisel çalışma alanını etkileyebilir; root ile aynı hata tüm sistemin kullanılmaz hâle gelmesine yol açabilir. Buna rağmen deneyimli yöneticilerde $P(hata)$ her zaman sıfıra yaklaşmaz; çünkü rutinleşme dikkati azaltabilir.

| Davranış boyutu | Standart kullanıcı | Root/yönetici kullanıcı |
|---|---|---|
| İşlem kapsamı | Kendi alanıyla sınırlı | Sistem geneline yayılabilir |
| Hata geri alma | Genellikle daha kolay | Yedek, kurtarma ve kesinti gerektirebilir |
| Kontrol hissi | Kısıtlı ve görünür | Yüksek, bazen yanıltıcı |
| Karar hızı | Onay ve izinlerle yavaşlar | Hızlıdır; aceleciliğe açık olabilir |
| Sorumluluk | Dağıtılmış | Teknik ve etik olarak yoğunlaşmış |

Psikolojideki **kontrol yanılsaması**, kişinin sonuçlar üzerindeki etkisini olduğundan büyük değerlendirmesidir. Root yetkisi bu yanılsamayı besleyebilir: Kullanıcı birçok sorunu tek komutla çözebildiği için, her sistem davranışını aynı açıklıkla öngördüğünü düşünebilir. Oysa dağıtık servisler, bağımlılıklar, yarış koşulları ve yanlış yapılandırmalar kontrolün her zaman tam olmadığını hatırlatır.

Bu nedenle iyi sistem yöneticiliği, “her şeyi yapabilirim” yaklaşımı değil, “yapabiliyorum; ama önce etkisini modellemeliyim” disiplinidir. Özellikle üretim ortamında komut öncesi duraklama, bilişsel bir emniyet kemeridir. Aşağıdaki kabuk örneği, yıkıcı olabilecek işlemler öncesinde hedefi görünür kılar ve açık onay ister:

```bash
#!/usr/bin/env bash
# Silme işleminden önce hedefi doğrular ve kullanıcıdan açık onay alır.
target="$1"

if [[ $EUID -ne 0 ]]; then
  echo "Bu işlem yönetici yetkisi gerektirir."
  exit 1
fi

read -r -p "Silinecek hedef: $target. Devam? (EVET): " answer
if [[ "$answer" == "EVET" ]]; then
  rm -rf -- "$target"
  echo "İşlem tamamlandı."
else
  echo "İşlem iptal edildi."
fi
```

Bu betik kusursuz koruma sağlamaz; yanlış hedef girildiyse root yine siler. Ancak otomatik pilotu keser. Dikkat araştırmalarında kritik olan, kararın yavaşlatılması değil, riskli kararın bilinçli hâle getirilmesidir. Başka bir deyişle amaç sürtünme yaratmak değil, doğru noktada sürtünme yaratmaktır.

| Koruma yaklaşımı | Psikolojik etkisi | Teknik katkısı |
|---|---|---|
| `sudo` ile geçici yetki | Gücün sürekli olmadığını hatırlatır | Yetki süresini sınırlar |
| Komut kaydı/audit log | Hesap verebilirlik oluşturur | Olay incelemesini kolaylaştırır |
| Ayrı yönetici hesabı | Günlük alışkanlığı böler | Yanlışlıkla yapılan işlemleri azaltır |
| Eşli inceleme | Aşırı güveni dengeler | Kritik değişiklikleri doğrular |

Sorumluluk algısı, yetki arttığında otomatik olarak artmaz; süreçlerle desteklenmelidir. İyi yönetici, root kabuğunu bir ödül veya statü simgesi olarak değil, yüksek etkili bir araç olarak görür. En güvenli refleks çoğu zaman komutu hemen çalıştırmak değil; ortamı, hedefi, geri dönüş planını ve logları önce kontrol etmektir. Mutlak kontrolün olgun kullanımı, sınırsız hareket etmek değil, sınırların neden gerekli olduğunu bilmektir.
