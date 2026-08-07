---
layout: post
title: "Sıfırdan Mini Çekirdek: Bootloader’dan Çoklu Göreve Yolculuk"
math: true
categories: 
  - Proje
tags: 
  - işletim sistemi
  - kernel geliştirme
  - multitasking
---

Bilgisayar açıldığında bizi masaüstü, pencereler ve uygulamalar karşılamadan önce oldukça ilkel bir dünya vardır. İşlemci, bellekteki belirli bir adresten komut yürütmeye başlar; ne dosya sistemi ne süreçler ne de yardım isteyebileceğimiz bir işletim sistemi bulunur. Bu projede x86 mimarisi üzerinde küçük bir çekirdek geliştirerek bootloader, korumalı kip, kesmeler ve çoklu görev arasındaki zinciri kuracağız.

``

## Açılış zinciri nasıl çalışır?

BIOS tabanlı klasik bir sistemde ilk sektör, yani 512 baytlık boot sektörü, bellekte `0x7C00` adresine yüklenir. Son iki baytın `0x55AA` olması BIOS’a sektörün önyüklenebilir olduğunu bildirir. Bootloader’ın görevi çekirdeği diskten belleğe taşımak, uygun işlemci kipini hazırlamak ve denetimi çekirdeğin giriş noktasına bırakmaktır.

| Aşama | İşlemci durumu | Temel sorumluluk |
|---|---|---|
| Boot sektörü | 16-bit gerçek kip | Donanımı tanımak ve çekirdeği yüklemek |
| Korumalı kipe geçiş | 32-bit | GDT kurmak ve segmentleri ayarlamak |
| Çekirdek başlangıcı | 32-bit C/Assembly | Bellek, ekran ve kesmeleri hazırlamak |
| Zamanlayıcı | Kesme destekli | Görevler arasında bağlam değiştirmek |

Boot sektörünün sonunu hazırlayan minimal NASM kodu şöyledir:

```nasm
bits 16
org 0x7C00

cli                 ; Hazırlık sırasında kesmeleri kapat
xor ax, ax
mov ds, ax
mov ss, ax
mov sp, 0x7C00      ; Geçici yığın oluştur

hang:
    hlt
    jmp hang

times 510-($-$$) db 0
dw 0xAA55
```

Buradaki `$` mevcut adresi, `$$` ise bölümün başlangıcını gösterir. Dolgu miktarı matematiksel olarak $510-(\text{mevcut konum}-\text{başlangıç})$ biçiminde hesaplanır.

## Korumalı kip ve çekirdeğe geçiş

32-bit korumalı kip için önce Global Descriptor Table oluşturulur. GDT, kod ve veri segmentlerinin taban adresi, sınırı ve erişim haklarını tanımlar. Ardından `CR0` yazmacındaki PE biti etkinleştirilir:

```nasm
cli
lgdt [gdt_descriptor]
mov eax, cr0
or eax, 1
mov cr0, eax
jmp 0x08:protected_mode
```

Uzak atlama, işlemcinin komut kuyruğunu temizler ve yeni kod segmentini yükler. Çekirdeği C ile yazmak geliştirmeyi kolaylaştırır; ancak standart kütüphane kullanılamaz. Bu nedenle `memcpy`, `memset` ve ekran çıktısı gibi araçları kendimiz üretiriz.

```c
volatile unsigned short *vga = (unsigned short *)0xB8000;

void put_char(char c, int position) {
    vga[position] = (0x0F << 8) | c;
}

void kernel_main(void) {
    put_char('K', 0); /* VGA metin belleğine doğrudan yazar */
    for (;;) __asm__ volatile("hlt");
}
```

## Kesme olmadan çoklu görev olmaz

Çekirdeğin düzenli aralıklarla kontrolü geri alması için PIT zamanlayıcısı ve Interrupt Descriptor Table gerekir. PIT frekansı yaklaşık $1{,}193{,}182$ Hz’dir. İstenen kesme frekansı $f$ ise gönderilecek bölen

$$d=\frac{1{,}193{,}182}{f}$$

olarak hesaplanır. Örneğin 100 Hz için yaklaşık `11931` kullanılır. Her zamanlayıcı kesmesinde çalışan görevin yazmaçları saklanır ve sıradaki görevin bağlamı yüklenir.

```c
typedef struct {
    unsigned int esp;
    unsigned int id;
    int active;
} task_t;

int current = 0;
task_t tasks[2];

void schedule(void) {
    current = (current + 1) % 2;
    switch_stack(tasks[current].esp);
}
```

Bu basit yöntem round-robin zamanlamadır. Her görev eşit zaman dilimi alır; $n$ görev ve $T$ uzunluğunda dilim için aynı göreve yaklaşık $nT$ sonra dönülür. Gerçek bir bağlam değişiminde `ESP` dışında genel yazmaçlar, bayraklar ve gerekirse adres uzayı da korunmalıdır.

| Yaklaşım | Avantaj | Dezavantaj |
|---|---|---|
| İşbirlikçi görev | Basit ve öngörülebilir | Görev kontrolü bırakmazsa sistem donar |
| Kesintili görev | Daha adil ve dayanıklı | Kesme ve bağlam yönetimi karmaşıktır |
| Ayrı adres uzayı | Güçlü süreç yalıtımı | Sayfalama ve TLB maliyeti getirir |

Projeyi QEMU üzerinde çalıştırmak, fiziksel donanımı yanlışlıkla kilitlemeden seri port günlüklerini ve işlemci durumunu incelemeyi sağlar. İlk hedefiniz ekrana iki görevin dönüşümlü karakter yazması olabilir. Bu küçük başarı, modern işletim sistemlerinin arkasındaki görünmez orkestrayı elle kurduğunuz anlamına gelir.
