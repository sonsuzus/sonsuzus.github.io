---
layout: post
title: "Sızma Sonrası Güvenli Doğrulama ve Profesyonel Raporlama"
math: true
categories: 
  - Bilgi
tags: 
  - post-exploitation
  - sızma testi
  - siber güvenlik raporlama
---

Bir sızma testinde ilk erişimi elde etmek final değil, yalnızca hikâyenin dönüm noktasıdır. Post-exploitation aşaması; ele geçirilen erişimin etkisini, saldırganın ilerleyebileceği yolları ve kurumun bu hareketleri fark etme kapasitesini **yetkilendirilmiş sınırlar içinde** incelemeyi amaçlar. Buradaki başarı, sisteme gizlice yerleşmekten çok riski güvenli biçimde kanıtlamak, iz bırakmadan değil kontrollü iz bırakarak çalışmak ve test sonunda ortamı başlangıç durumuna döndürmektir.
``
## Post-Exploitation Mantığı

Bu aşamada test uzmanı genellikle erişim seviyesini, hassas veri görünürlüğünü, ağ içi hareket ihtimalini ve kalıcılık kontrollerini değerlendirir. Kalıcılık, bir saldırganın oturum kapansa veya sistem yeniden başlatılsa bile erişimini sürdürebilmesidir. Ancak profesyonel testlerde gerçek ve gizli bir arka kapı bırakmak yerine, tekniklerin uygulanabilirliği **zararsız göstergeler**, geçici test hesapları ya da savunma ekibiyle kararlaştırılmış simülasyonlar üzerinden doğrulanmalıdır.

| İnceleme alanı | Güvenli doğrulama yaklaşımı | Beklenen savunma |
|---|---|---|
| Hesap tabanlı kalıcılık | Süresi sınırlı test hesabı | Yeni hesap alarmı ve MFA |
| Zamanlanmış çalıştırma | Zararsız işaret dosyası üreten görev | Görev oluşturma telemetrisi |
| Başlangıç mekanizmaları | Yalnızca laboratuvarda simülasyon | Dosya ve kayıt değişikliği alarmı |
| Bulut erişimi | Geçici, düşük yetkili anahtar | Anahtar kullanımı ve anomali takibi |

Kalıcılığın riski yalnızca tekniğe bağlı değildir. Basit bir öncelik modeli şu şekilde kurulabilir:

$$R = O \times E \times V$$

Burada $O$ oluşma olasılığını, $E$ erişimin iş etkisini, $V$ ise mekanizmanın görünmeden sürdürülebilme derecesini temsil eder. Örneğin ayrıcalıklı ve denetlenmeyen bir servis hesabı, düşük yetkili ve sürekli izlenen bir hesaptan daha yüksek puan alır.

## Kontrollü Çalışma Akışı

Önce kapsam ve angajman kuralları yeniden kontrol edilir. Ardından mevcut yetkiler belgelenir; erişim yükseltme veya yatay hareket girişimleri yalnızca açık izin varsa gerçekleştirilir. Her değişiklik için zaman, sistem, amaç, sonuç ve geri alma yöntemi kaydedilir. Üretim ortamında hizmet kesintisi oluşturabilecek işlemlerden kaçınılır.

Aşağıdaki örnek, bulguların öncelik puanını hesaplayan zararsız bir raporlama yardımcısıdır:

```python
findings = [
    {"name": "Denetlenmeyen test hesabı", "likelihood": 4, "impact": 5},
    {"name": "Eksik görev alarmı", "likelihood": 3, "impact": 3},
]

for finding in findings:
    finding["score"] = finding["likelihood"] * finding["impact"]
    finding["priority"] = "Kritik" if finding["score"] >= 16 else "Yüksek"
    print(f"{finding['name']}: {finding['score']} - {finding['priority']}")
```

Kod, olasılık ile etkiyi çarparak tutarlı bir ilk sıralama sağlar. Yine de nihai seviye; varlığın önemi, mevcut kontroller ve kurumun risk iştahıyla birlikte değerlendirilmelidir.

## Yönetimsel Dilde Raporlama

Profesyonel rapor iki farklı okuyucuya seslenir. Yönetici özeti; saldırı zincirini, iş etkisini ve yatırım önceliklerini teknik ayrıntıya boğulmadan anlatır. Teknik bölüm ise kanıtları, zaman çizelgesini, etkilenen varlıkları, tekrarlanabilir doğrulama adımlarını ve düzeltme önerilerini içerir.

| Teknik ifade | Yönetimsel karşılığı |
|---|---|
| Ayrıcalıklı erişim elde edildi | Kritik sistemlerde yetkisiz işlem riski oluştu |
| Alarm üretilmedi | Müdahale süresi uzayabilir |
| Kalıcılık mümkün | Erişim, parola değişikliğinden sonra sürebilir |
| Ağ içi hareket doğrulandı | Tek sistemdeki ihlal daha geniş etki yaratabilir |

Her bulguda başlık, önem derecesi, iş etkisi, kanıt, kök neden, öneri ve sorumlu ekip bulunmalıdır. Ekran görüntüleri hassas verileri maskelemeli; hash değerleriyle kanıt bütünlüğü korunmalıdır. Test sonunda oluşturulan hesaplar, dosyalar, görevler ve anahtarlar temizlenmeli, temizlik ikinci bir uzman tarafından doğrulanmalıdır.

İyi bir post-exploitation çalışması “ne kadar içeride kaldık?” sorusuyla değil, “kurum neyi daha iyi savunabilir?” sorusuyla ölçülür. Net kanıt, güvenli temizlik ve yönetimin anlayacağı risk dili; teknik beceriyi gerçek güvenlik kazanımına dönüştüren üçlüdür.
