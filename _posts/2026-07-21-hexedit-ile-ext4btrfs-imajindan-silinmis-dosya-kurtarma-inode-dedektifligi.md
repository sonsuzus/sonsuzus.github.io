---
layout: post
title: "Hexedit ile Ext4/Btrfs İmajından Silinmiş Dosya Kurtarma: Inode Dedektifliği"
math: true
categories: 
  - Bilgi
tags: 
  - ext4
  - btrfs
  - forensics
  - hexedit
  - inode
---

Bir dosya silindiğinde çoğu zaman verinin kendisi anında buharlaşmaz; dosya sisteminin “bu alan artık boş” dediği muhasebe kayıtları değişir. İşte ham disk imajını `hexedit` ile açıp inode ve blok adreslerini elle okumak, biraz arkeoloji biraz dedektiflik gibidir: kumların altından byte byte hikâye çıkarırız.
``

> Not: Bu yazı adli analiz ve kendi verinizi kurtarma senaryoları içindir. Gerçek diskte değil, **imaj kopyası** üzerinde çalışın. Yazma işlemi, kurtarılabilir veriyi ezebilir.

## Silinme Ne Demek?

Dosya sistemi bir dosyayı genellikle iki parçayla takip eder: **metadata** ve **data**. Metadata; isim, izin, zaman damgası, inode numarası ve verinin hangi bloklarda durduğunu söyler. Data ise dosyanın gerçek içeriğidir.

Basitleştirilmiş denklem şöyle düşünülebilir:

$$\text{Dosya} = \text{İsim Kaydı} + \text{Inode} + \text{Veri Blokları}$$

Silme sırasında dizin girdisi kaldırılır, inode’un bağlantı sayısı düşer ve bloklar “boş” kabul edilir. Ama bloklar üzerine yeni veri yazılmadıysa hâlâ oradadır.

| Özellik | Ext4 | Btrfs |
|---|---|---|
| Metadata modeli | Inode tablosu ve blok grupları | B-tree tabanlı, COW mimarisi |
| Elle yorumlama | Daha öngörülebilir | Daha karmaşık |
| Silinmiş veri şansı | Üzerine yazılmadıysa iyi | Snapshot/COW varsa bazen çok iyi |
| Zorluk seviyesi | Orta | İleri |

Bu yazıda ana örneği Ext4 üzerinden kuracağız; Btrfs için de mantığı karşılaştıracağız.

## Güvenli Laboratuvar Hazırlığı

Önce diskten ya da bölümden imaj alın:

```bash
sudo dd if=/dev/sdb1 of=disk.img bs=4M status=progress conv=noerror,sync
cp disk.img lab.img
hexedit lab.img
```

`hexedit` içinde gezinirken unutmayın: sayılar çoğu zaman **little-endian** saklanır. Yani ekranda `00 10 00 00` görüyorsanız bu değer `0x00001000`, yani 4096 olabilir.

## Ext4 Inode Adresini Hesaplamak

Ext4’te süperblok genelde bölüm başlangıcından 1024 byte sonra başlar. Buradan blok boyutu, inode boyutu, grup başına inode sayısı gibi bilgiler okunur.

Blok boyutu formülü:

$$\text{block\_size} = 1024 \times 2^{s\_log\_block\_size}$$

Bir inode’un disk üzerindeki konumu için:

$$\text{group} = \left\lfloor \frac{inode - 1}{inodes\_per\_group} \right\rfloor$$

$$\text{index} = (inode - 1) \bmod inodes\_per\_group$$

$$\text{inode\_offset} = inode\_table\_block \times block\_size + index \times inode\_size$$

Örneğin inode numarası 131083, blok boyutu 4096, inode boyutu 256 ve grup başına inode sayısı 8192 ise ilgili blok grubunu ve inode tablosundaki yerini bu formüllerle buluruz.

## Inode İçindeki İpuçları

Ext4 inode yapısında önemli alanlar şunlardır:

| Alan | Tipik offset | Anlamı |
|---|---:|---|
| `i_mode` | `0x00` | Dosya türü ve izinler |
| `i_size_lo` | `0x04` | Dosya boyutu düşük 32 bit |
| `i_links_count` | `0x1A` | Bağlantı sayısı |
| `i_blocks_lo` | `0x1C` | Ayrılmış blok bilgisi |
| `i_block` | `0x28` | Extent veya blok işaretçileri |
| `i_dtime` | `0x14` | Silinme zamanı |

Silinmiş dosyada `i_links_count` sıfır olabilir ve `i_dtime` doludur. Asıl hazine ise `i_block` alanındadır. Modern Ext4 çoğunlukla extent kullanır. `i_block` alanında `0a f3` görürseniz, bu little-endian `0xf30a` extent sihirli değeridir.

Extent başlığı kabaca şöyledir:

```text
struct ext4_extent_header {
  __le16 eh_magic;    // 0xf30a
  __le16 eh_entries;  // kaç kayıt var
  __le16 eh_max;
  __le16 eh_depth;    // 0 ise yaprak
  __le32 eh_generation;
}
```

`eh_depth = 0` ise hemen ardından gerçek extent kayıtları gelir:

```text
struct ext4_extent {
  __le32 ee_block;     // dosya içi mantıksal blok
  __le16 ee_len;       // uzunluk
  __le16 ee_start_hi;  // fiziksel blok üst bitler
  __le32 ee_start_lo;  // fiziksel blok alt bitler
}
```

Fiziksel blok hesabı:

$$\text{physical} = (ee\_start\_hi \ll 32) + ee\_start\_lo$$

Byte offset ise:

$$\text{byte\_offset} = \text{physical} \times \text{block\_size}$$

## Veriyi Çekmek

Diyelim extent bize fiziksel blok `250000`, uzunluk `12`, blok boyutu `4096` dedi. Dosyayı şöyle çıkarabiliriz:

```bash
dd if=lab.img of=recovered.bin bs=4096 skip=250000 count=12 status=progress
```

Bu komut imajdan 12 blok okur ve `recovered.bin` dosyasına yazar. Dosya parçalıysa her extent ayrı çıkarılır, sonra mantıksal blok sırasına göre birleştirilir.

## Btrfs Neden Daha Çetrefilli?

Btrfs’te klasik “inode tablosu” beklentisi boşa düşer. Metadata B-tree yapılarında tutulur; ayrıca Copy-on-Write sayesinde eski sürümlerin izleri kalabilir. Bu harika bir kurtarma şansı sunar ama elle hex ile çözümlemek Ext4’e göre daha zahmetlidir.

| Kavram | Ext4 karşılığı | Btrfs karşılığı |
|---|---|---|
| Inode yeri | Hesaplanabilir tablo | B-tree item |
| Veri adresi | Extent alanı | File extent item |
| Eski veri | Üzerine yazılmadıysa | COW/snapshot ile kalabilir |
| Elle kurtarma | Formülle mümkün | Ağaç yapısı takibi gerekir |

## Sonuç

Ext4’te manuel kurtarma; süperbloktan parametreleri okumak, inode adresini hesaplamak, extent kayıtlarını yorumlamak ve fiziksel blokları `dd` ile çekmekten ibarettir. Btrfs ise daha modern ve güçlüdür ama elle analizde daha fazla ağaç gezmeyi gerektirir. Kısacası: Ext4 düz bir harita, Btrfs ise üç boyutlu labirenttir. İkisi de çözülebilir; yeter ki byte’lar hâlâ yerinde olsun.
