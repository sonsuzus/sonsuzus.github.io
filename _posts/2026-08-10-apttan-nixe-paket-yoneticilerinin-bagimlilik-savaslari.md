---
layout: post
title: "apt’tan Nix’e: Paket Yöneticilerinin Bağımlılık Savaşları"
math: true
categories: 
  - Bilgi
tags: 
  - paket yöneticileri
  - apt
  - nix
  - bağımlılık yönetimi
  - linux
---

Bir yazılımı çalıştırmak eskiden “dosyayı kopyala ve aç” kadar basitti. Sonra kütüphaneler, sürüm beklentileri, derleyiciler ve işletim sistemi paketleri sahneye çıktı. Bugün bir projenin çalışması için yalnızca kodun değil, kodun konuştuğu bütün çevrenin de doğru biçimde kurulması gerekir. Paket yöneticilerinin tarihi, aslında bu görünmez bağımlılık ağını evcilleştirme girişimlerinin kısa ama oldukça hareketli tarihidir.
``

## Sorun: Aynı Makinede Herkesin İstediği Sürüm

Bir uygulama `libssl`in eski sürümünü isterken diğeri yeni sürümünü isteyebilir. Üçüncü uygulama ise Python 3.10 ile çalışır, ancak sistemin varsayılan Python’ını değiştirmek istemezsiniz. Bu durum, bağımlılık çözümleyicisinin şu soruya cevap vermesini gerektirir: “Tüm sürüm kısıtlarını aynı anda sağlayan bir kurulum var mı?”

Teorik olarak bu, sürüm seçimi değişkenleri içeren bir kısıt tatmin problemidir. Her bağımlılık yeni kısıtlar ekler:

$$
\text{Uygun çözüm} = \bigcap_{i=1}^{n} \text{SürümKısıtı}_i
$$

Kesişim boşsa ünlü hata mesajı gelir: *dependency conflict*. Üstelik bağımlılıklar çoğunlukla ağaç değil, ortak paketlerin bulunduğu yönlü bir graf oluşturur. Küçük görünen bir güncelleme, grafın uzak bir köşesindeki paketi bozabilir.

| Dönem | Temel yaklaşım | Ana problem |
|---|---|---|
| Elle kurulum | Dosya ve kaynak kod kopyalama | Tekrarlanamaz kurulumlar |
| apt/yum | Sistem genelinde paket veritabanı | Sürüm çakışmaları |
| npm/pip | Proje tabanlı bağımlılıklar | Kilit dosyası ve transitif karmaşa |
| Nix | İzole, içerik-adresli paketler | Öğrenme eğrisi |

## apt: Dağıtım Merkezli Düzen

Debian ekosisteminin `apt` aracı, paket yönetimini merkezi depolara ve sistem genelindeki bir veritabanına bağladı. Bir paket, başka paketleri `Depends`, `Recommends` veya `Conflicts` alanlarıyla tarif eder. `apt`, uygun `.deb` paketlerini indirir, kurar ve hangi dosyanın hangi pakete ait olduğunu kaydeder.

```bash
sudo apt update
sudo apt install curl build-essential
apt-cache depends curl
```

Bu komutlar depoyu günceller, `curl` ile derleme araçlarını kurar ve `curl`ün bağımlılıklarını gösterir. Yaklaşım kullanıcı dostudur: işletim sistemi tek, tutarlı bir paket dünyası gibi davranır. Ancak bunun bedeli paylaşılmış durumdur. Sistem genelindeki bir yükseltme, başka bir aracın beklediği sürümü değiştirebilir.

## Dil Ekosistemleri: node_modules ve Sanal Ortamlar

Uygulama geliştirme hızlandıkça işletim sistemi paketleri yetersiz kaldı. JavaScript için `npm`, Python için `pip`, Ruby için `Bundler` gibi araçlar bağımlılıkları proje düzeyinde tanımlamaya başladı. Böylece iki proje farklı sürümleri birlikte kullanabildi.

```bash
python -m venv .venv
source .venv/bin/activate
pip install requests==2.32.3
pip freeze > requirements.txt
```

Buradaki sanal ortam, Python paketlerini sistemden ayırır; `requirements.txt` ise kurulumu tarif etmeye çalışır. Fakat “çalışan makinede” oluşan dosya, her zaman “başka makinede” aynı sonucu üretmez. İşletim sistemi kütüphaneleri, platform farkları ve gevşek sürüm aralıkları hâlâ denklemdedir.

| Özellik | apt | npm/pip | Nix |
|---|---|---|---|
| İzolasyon | Sistem geneli | Genellikle proje bazlı | Paket ve ortam bazlı |
| Sürüm çoğaltma | Zor | Kısmen mümkün | Doğal olarak mümkün |
| Tekrarlanabilirlik | Depoya bağlı | Kilit dosyasına bağlı | Bildirime ve hash’e bağlı |
| Geri alma | Sınırlı | Manuel | Nesil tabanlı kolay |

## Nix: Paketi Dosya Değil, Fonksiyon Gibi Düşünmek

Nix’in dikkat çekici fikri, bir paketin sonucunu girdilerinden üretmesidir. Derleyici, kaynak kod, yamalar ve bağımlılıklar değişirse sonuç da değişir. Paketler `/nix/store` altında girdilerinin karmasına göre saklanır. Basitleştirilmiş biçimde:

$$
\text{storePath} = H(\text{source}, \text{dependencies}, \text{build instructions})
$$

Bu nedenle aynı makinede iki farklı `openssl` sürümü çakışmadan bulunabilir. Nix ifadesi de niyeti açıkça bildirir:

```nix
{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  packages = [ pkgs.python312 pkgs.python312Packages.requests ];
}
```

Bu geliştirme kabuğu, belirli Python sürümünü ve `requests` paketini tanımlar. `nix-shell` veya modern akışta `nix develop`, bu çevreyi projeye özel biçimde kurar. Nix sihirli değildir: paketleme dili, önbellek mantığı ve “saflık” kavramı ilk başta zorlayıcıdır. Buna rağmen bağımlılık grafını açık, izole ve yeniden üretilebilir hale getirmesi; CI sistemleri, ekip çalışması ve uzun ömürlü projeler için güçlü bir karşılıktır.

Paket yöneticilerinin evrimi, daha çok paket indirmekten çok daha fazlasıdır. Amaç, “benim bilgisayarımda çalışıyor” cümlesini ölçülebilir bir yapı tarifine dönüştürmektir.
