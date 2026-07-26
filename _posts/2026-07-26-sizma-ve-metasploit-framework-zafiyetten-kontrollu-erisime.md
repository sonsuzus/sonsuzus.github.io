---
layout: post
title: "Sızma ve Metasploit Framework: Zafiyetten Kontrollü Erişime"
math: true
categories: 
  - Bilgi
tags: 
  - Metasploit
  - Sızma Testi
  - Siber Güvenlik
---

Bir zafiyetin tespit edilmesi, sistemin gerçekten ele geçirilebildiği anlamına gelmez; yalnızca araştırılması gereken bir kapı bulunduğunu gösterir. Sızma, bu kapının yetkili ve izole bir laboratuvar ortamında kontrollü biçimde açılmasıdır. Metasploit Framework ise hazır istismar modülleri, payload seçenekleri ve oturum yönetimiyle bu süreci standartlaştıran güçlü bir güvenlik test platformudur.

``

## İstismar sürecinin teorik temeli

Bir istismar, hedef yazılımdaki hatayı sistem davranışını değiştirmek için kullanır. Basitleştirilmiş risk modeli şöyle düşünülebilir:

$$R = O \times E \times I$$

Burada $O$ zafiyetin oluşma olasılığını, $E$ istismar edilebilirliği, $I$ ise muhtemel etkiyi temsil eder. Metasploit çoğunlukla $E$ değerinin pratik olarak doğrulanmasına yardımcı olur. Başarılı bir sonuç, riskin otomatik olarak kritik olduğu anlamına gelmez; erişilen yetki, ağ konumu ve veri etkisi ayrıca değerlendirilmelidir.

Metasploit ekosisteminin temel parçaları şunlardır:

| Bileşen | Görevi | Örnek kullanım |
|---|---|---|
| Exploit | Zafiyeti tetikler | Hatalı serviste kod yürütme |
| Payload | Başarı sonrası davranışı belirler | Kontrollü oturum açma |
| Auxiliary | Tarama ve yardımcı işlemler yapar | Sürüm doğrulama |
| Encoder | Bayt biçimini dönüştürür | Uyumluluk sağlama |
| Post | Açılmış oturumda test yapar | Yetki ve sistem bilgisi kontrolü |

Exploit kapıyı açan mekanizma, payload ise kapı açıldıktan sonra yapılacak iştir. Bu ayrım, yanlış payload seçildiğinde exploit doğru olsa bile neden oturum alınamadığını açıklar.

## Güvenli laboratuvarın hazırlanması

Testler yalnızca açık izin bulunan sistemlerde gerçekleştirilmelidir. Örnek senaryoda saldırı makinesi olarak Kali Linux, hedef olarak özellikle savunmasız bırakılmış Metasploitable 2 kullanılabilir. İki sanal makineyi **host-only** ağa bağlamak, internet erişimini kapatmak ve işlem öncesinde anlık görüntü almak önemlidir.

| Ağ türü | İnternet erişimi | Laboratuvar için uygunluk |
|---|---:|---|
| Bridged | Var | Riskli |
| NAT | Genellikle var | Sınırlı |
| Host-only | Yok | Önerilen |

Aşağıdaki komut Metasploit konsolunu başlatır:

```bash
msfconsole
```

Hedef laboratuvarda eski `vsftpd 2.3.4` servisi bulunduğu önceden doğrulanmışsa ilgili eğitim modülü incelenebilir:

```text
search vsftpd 2.3.4
use exploit/unix/ftp/vsftpd_234_backdoor
info
show options
```

`search` uygun modülleri listeler, `use` modülü seçer, `info` açıklama ve referansları gösterir. Modülü hemen çalıştırmak yerine dokümantasyonu okumak; desteklenen sürümü, yan etkileri ve gerekli seçenekleri anlamayı sağlar.

## Kontrollü doğrulama

Yalnızca izole hedefin IP adresi tanımlanır. Aşağıdaki adres örnektir ve özel laboratuvar aralığındadır:

```text
set RHOSTS 192.168.56.20
set RPORT 21
check
run
```

`check`, modül destekliyorsa hedefin istismara uygunluğunu oturum açmadan değerlendirmeye çalışır. `run` ise istismarı başlatır. Başarılı bir kabuk oluştuğunda kapsamı büyütmeden yalnızca kimlik doğrulaması yapılabilir:

```bash
id
uname -a
exit
```

Bu komutlar erişilen kullanıcıyı ve işletim sistemi bilgisini gösterir; veri değiştirmez. Kanıt için zaman damgası, modül adı, hedef sürümü ve elde edilen yetki seviyesi kaydedilmelidir. Parola dosyalarını okumak, kalıcılık kurmak veya başka sistemlere sıçramak doğrulama için gerekli değildir.

## Sonuçların yorumlanması

Başarısızlık da değerlidir: servis yamalı olabilir, sürüm tespiti hatalı çıkabilir veya ağ filtresi bağlantıyı engelleyebilir. Bulguda kullanılan modül, ön koşullar, gözlenen çıktı, etki ve düzeltme önerisi açıkça yazılmalıdır. Son aşamada oturumlar kapatılmalı, sanal makine anlık görüntüye döndürülmeli ve kayıtlar güvenli biçimde saklanmalıdır. Metasploit’in gerçek gücü “tek tuşla saldırı” değil; tekrarlanabilir, ölçülebilir ve etik sınırlar içindeki güvenlik doğrulamasıdır.
