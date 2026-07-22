---
layout: post
title: "tmpfs ile RAM’de Yaşayan, Kapanınca Unutan Mini Linux"
math: true
categories: 
  - Proje
tags: 
  - tmpfs
  - ramdisk
  - linux
  - initramfs
  - alpine
---

Bilgisayarınız her açılışta tertemiz başlasın, hiçbir iz bırakmasın ve disk yerine RAM hızında çalışsın ister miydiniz? Bu yazıda tmpfs üzerinde bir ramdisk oluşturup, içine minimal bir Linux kök dosya sistemi yerleştirerek tamamen RAM’de çalışan ve güç kesilince sıfırlanan bir sistemin mantığını kuracağız. Bunu bir “kullan-at işletim sistemi” gibi düşünebilirsiniz: hızlı, geçici ve eğlenceli derecede deneysel.
``
Önce temel fikri netleştirelim. `tmpfs`, Linux çekirdeğinin RAM ve gerektiğinde swap alanını kullanarak oluşturduğu geçici bir dosya sistemidir. Normal disk bölümü gibi bağlanır, ama veriler kalıcı değildir. Güç kesildiğinde RAM içeriği kaybolduğu için sistem de fabrika ayarına döner. Matematiksel olarak tmpfs için ayırdığımız güvenli alanı kabaca şöyle düşünebiliriz: $S_{tmpfs} = min(RAM - sistem_ihtiyaci, limit)$. Yani 8 GB RAM’iniz varsa 2 GB’lık bir rootfs mantıklı olabilir; 7 GB ayırırsanız çekirdeğin “bana da yer bırakın” deme ihtimali artar.

| Yaklaşım | Hız | Kalıcılık | Kullanım Alanı |
|---|---:|---:|---|
| Disk üzerindeki Linux | Orta/Yüksek | Var | Günlük kullanım |
| Live ISO | Orta | Genelde yok | Kurtarma, test |
| tmpfs RAM Linux | Çok yüksek | Yok | Kiosk, güvenli oturum, laboratuvar |

Bu proje için Alpine Linux güzel bir adaydır; çünkü küçüktür, hızlı kurulur ve minimal sistemlere yakışır. Fakat mantık Debian `debootstrap`, BusyBox veya kendi initramfs’inizle de aynıdır: çekirdek başlar, initramfs devreye girer, RAM’de bir kök dosya sistemi hazırlanır ve sistem `switch_root` ile oraya geçer.

İlk adımda mevcut çalışan bir Linux üzerinde RAM kök alanı oluşturalım. Bu aşama sistemi gerçekten boot ettirmez; sadece rootfs hazırlama laboratuvarıdır:

```bash
sudo mkdir -p /mnt/ramroot
sudo mount -t tmpfs -o size=2G,mode=0755 tmpfs /mnt/ramroot
```

Burada `size=2G`, tmpfs’in üst sınırıdır. Bu, RAM’in anında 2 GB’ının dolduğu anlamına gelmez; tmpfs kullandıkça büyür. Şimdi Alpine mini rootfs arşivini indirip buraya açabiliriz:

```bash
cd /mnt/ramroot
sudo wget https://dl-cdn.alpinelinux.org/alpine/latest-stable/releases/x86_64/alpine-minirootfs-latest-x86_64.tar.gz
sudo tar xzf alpine-minirootfs-latest-x86_64.tar.gz
sudo rm alpine-minirootfs-latest-x86_64.tar.gz
```

Bu noktada `/mnt/ramroot` içinde küçük ama gerçek bir Linux kullanıcı alanı vardır. DNS, proc, sys ve dev bağlamalarını ekleyip içine chroot ile girebiliriz:

```bash
sudo mount -t proc proc /mnt/ramroot/proc
sudo mount --rbind /sys /mnt/ramroot/sys
sudo mount --rbind /dev /mnt/ramroot/dev
sudo cp /etc/resolv.conf /mnt/ramroot/etc/resolv.conf
sudo chroot /mnt/ramroot /bin/sh
```

Chroot içindeyken temel paketleri ekleyebiliriz. Ama unutmayın: şu an RAM’e yazıyoruz. Kapanınca her şey puf!

```sh
apk update
apk add busybox-openrc openssh vim curl
passwd
```

Asıl sihir boot tarafındadır. Bilgisayar açılırken diskten sadece çekirdek ve initramfs okunur. initramfs içindeki küçük `init` betiği tmpfs’i bağlar, sıkıştırılmış rootfs’i RAM’e açar ve kontrolü oraya devreder. Basitleştirilmiş akış şöyledir:

| Aşama | Ne olur? | Kalıcı mı? |
|---|---|---|
| Bootloader | Kernel ve initramfs yüklenir | Evet, disk/USB üzerinde |
| initramfs | RAM’de tmpfs oluşturur | Hayır |
| rootfs açma | Minimal Linux tmpfs’e kopyalanır | Hayır |
| switch_root | Sistem RAM root’a geçer | Hayır |

Örnek bir init mantığı şu şekildedir:

```sh
#!/bin/sh
mount -t proc proc /proc
mount -t sysfs sys /sys
mount -t devtmpfs dev /dev
mkdir /newroot
mount -t tmpfs -o size=2G tmpfs /newroot
tar -xzf /rootfs.tar.gz -C /newroot
exec switch_root /newroot /sbin/init
```

Burada `/rootfs.tar.gz`, initramfs içine gömülmüş minimal sistem arşividir. Daha üretilebilir bir yapı için rootfs’i SquashFS olarak saklayıp açılışta tmpfs’e kopyalayabilirsiniz. SquashFS daha az yer kaplar; tar.gz ise basitliğiyle kazanır.

Bu mimarinin en güzel yanı güvenlik ve tekrarlanabilirliktir. Bir eğitim laboratuvarında öğrenciler sistemi bozabilir, zararlı yazılım bulaşabilir veya konfigürasyon darmadağın olabilir. Yeniden başlatınca her şey başlangıç haline döner. Dezavantajı ise doğal olarak kalıcılığın olmamasıdır. Log, ayar veya dosya saklamak istiyorsanız ayrı bir kalıcı bölüm bağlamanız gerekir.

Sonuç olarak tmpfs tabanlı RAM Linux; çekirdek, initramfs ve minimal rootfs üçlüsünün dansıdır. Disk sadece kıvılcımı çakar, asıl parti RAM’de döner. Doğru boyutlandırma, küçük dağıtım seçimi ve sade init betiğiyle açılışta doğan, kapanışta hafızalardan silinen sevimli bir işletim sistemi elde edebilirsiniz.
