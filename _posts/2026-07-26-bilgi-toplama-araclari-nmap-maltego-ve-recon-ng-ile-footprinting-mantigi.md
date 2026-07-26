---
layout: post
title: "Bilgi Toplama Araçları: Nmap, Maltego ve Recon-ng ile Footprinting Mantığı"
math: true
categories: 
  - Bilgi
tags: 
  - siber güvenlik
  - information gathering
  - nmap
  - osint
---

Bir sistemi güvenli hâle getirmenin ilk adımı, saldırgan gözüyle ne kadar görünür olduğunu anlamaktır. Bilgi toplama, yani footprinting, hedef hakkında alan adları, IP aralıkları, açık portlar, kullanılan teknolojiler, ilişkili e-posta adresleri ve organizasyon yapısı gibi ipuçlarını sistemli biçimde toplamaktır. Elbette bu süreç yalnızca izinli testlerde, kendi laboratuvarında veya kurum içi güvenlik çalışmalarında yapılmalıdır; çünkü aynı teknikler savunma kadar kötüye kullanım için de değerlidir.
``

Bilgi toplama iki ana aileye ayrılır: pasif ve aktif. Pasif toplamada hedef sisteme doğrudan dokunmadan açık kaynaklardan veri çekilir; arama motorları, WHOIS kayıtları, sertifika şeffaflığı kayıtları ve sosyal ağlar buna örnektir. Aktif toplamada ise hedefe paket gönderilir; port taraması, servis sürüm tespiti ve ağ haritalama bu gruba girer. Basit bir zihinsel model kurarsak, görünür risk yaklaşık şöyle düşünülebilir: $R = A \times E \times V$. Burada $A$ saldırı yüzeyi, $E$ erişilebilirlik, $V$ ise zafiyet olasılığıdır. Bilgi toplama, bu üç değişkeni daha net ölçmeye yarar.

| Yaklaşım | Hedefe temas | Tipik araç | Avantaj | Risk |
|---|---:|---|---|---|
| Pasif OSINT | Yok veya çok az | Maltego, Recon-ng | Sessiz ve geniş kapsamlı | Veri eski olabilir |
| Aktif tarama | Var | Nmap | Güncel teknik sonuç verir | Log bırakır, izin gerekir |
| Hibrit analiz | Kontrollü | Üçü birlikte | Daha doğru korelasyon | Yanlış yorum maliyeti artar |

Nmap, aktif keşif tarafının İsviçre çakısı gibidir. Bir ağı haritalamak, açık portları görmek ve servislerin sürümlerini tahmin etmek için kullanılır. Örneğin kendi test makinenizde şu komut, yaygın portları ve servis bilgilerini listeler:

```bash
nmap -sV -O 192.168.56.10
```

Burada `-sV` servis sürüm tespiti yapar, `-O` işletim sistemi tahminini dener. Sonuçta 22/tcp üzerinde OpenSSH, 80/tcp üzerinde Nginx gibi bilgiler görebilirsiniz. Ancak çıktıyı büyülü kehanet gibi değil, olasılık tablosu gibi okumak gerekir. Nmap paket davranışlarından tahmin yapar; güvenlik duvarları, ters proxyler veya honeypotlar sonuçları yanıltabilir.

Maltego ise ilişkileri görselleştirme konusunda parlıyor. Bir alan adından başlayıp DNS kayıtlarına, alt alan adlarına, e-posta desenlerine, sosyal medya izlerine ve şirket bağlantılarına uzanan bir grafik çıkarabilir. Maltego’nun gücü tek bir veriden çok, düğümler arasındaki ilişkiyi göstermesidir. Örneğin bir e-posta adresinin aynı zamanda sızmış veri kümelerinde, GitHub commitlerinde ve kurum sayfalarında görünmesi, savunma ekibine farkındalık eğitimi veya erişim politikası açısından sinyal verebilir.

Recon-ng, terminal sevenler için modüler bir OSINT çatısıdır. Metasploit benzeri bir çalışma akışı vardır: workspace oluştur, modül seç, kaynak ekle, sonucu tabloya yaz. Kendi alan adınız üzerinde pasif keşif yaparken şöyle bir akış kullanılabilir:

```bash
recon-ng
workspaces create lab
marketplace search domains
modules load recon/domains-hosts/hackertarget
options set SOURCE example.com
run
show hosts
```

Bu komutlar, seçilen modül destekliyorsa `example.com` için host kayıtlarını toplar ve veritabanında saklar. Recon-ng’nin güzel tarafı, çıktıları düzenli tutmasıdır; böylece bulunan alt alan adlarını daha sonra Nmap ile doğrulayabilir veya Maltego grafiğine aktarabilirsiniz.

Pratikte iyi bir bilgi toplama süreci sırayla ilerler: kapsamı belirle, pasif kaynaklardan veri topla, veriyi temizle, aktif taramayı yalnızca izinli aralıkta çalıştır, sonuçları ilişkilendir ve raporla. En sık yapılan hata, araç çıktısını doğrudan gerçek kabul etmektir. Oysa aynı IP üzerinde CDN, paylaşımlı hosting veya bulut yük dengeleyici olabilir. Bu yüzden her bulguya güven puanı vermek faydalıdır: $G = \frac{D}{T}$ gibi basit bir oran düşünebiliriz; burada $D$ doğrulanan kaynak sayısı, $T$ toplam iddia sayısıdır.

Sonuç olarak Nmap sana teknik kapıları, Maltego ilişkisel haritayı, Recon-ng ise tekrarlanabilir OSINT akışını sunar. Üçünü birlikte kullandığında hedefin dijital siluetini daha net görürsün. Ama unutma: iyi bir güvenlik uzmanını araç listesi değil, etik sınırları, metodolojisi ve bulguları doğru yorumlama becerisi güçlü yapar.
