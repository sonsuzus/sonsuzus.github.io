---
layout: post
title: "Kabuk Betikleriyle Mini Konteyner Motoru: Namespace ve Cgroup Atölyesi"
math: true
categories: 
  - Program
tags: 
  - linux
  - container
  - bash
  - namespace
  - cgroup
---

Konteyner denince akla hemen Docker gelir; ama sahnenin arkasında sihirli bir ejderha değil, Linux çekirdeğinin çok ciddi iki mekanizması çalışır: ad alanları ve kontrol grupları. Bu yazıda hazır bir konteyner motoru kullanmadan, kabuk betikleriyle küçük ama öğretici bir motor kuracağız. Amaç üretim ortamına rakip çıkarmak değil; kaputun altındaki pistonları tek tek görmek.
``

Önce teoriyi netleştirelim. Linux namespace, bir sürece gerçek sistemin yalnızca belirli bir görünümünü verir. Yani süreç kendini ayrı bir makinedeymiş gibi hisseder. Cgroup ise o sürecin ne kadar CPU, bellek veya süreç sayısı kullanabileceğini sınırlar. Basit denklemle: konteyner hissi = izolasyon + kaynak limiti + ayrı dosya sistemi. Bunu şöyle yazabiliriz: $K = N + C + R$, burada $N$ namespace, $C$ cgroup, $R$ rootfs anlamına gelir.

| Mekanizma | Ne yapar? | Günlük benzetme |
|---|---|---|
| PID namespace | Süreç numaralarını izole eder | Her sınıfta ayrı yoklama listesi |
| Mount namespace | Bağlama noktalarını ayırır | Her odanın kendi raf düzeni |
| UTS namespace | Hostname bilgisini ayırır | Her evin farklı kapı tabelası |
| Network namespace | Ağ arayüzlerini ayırır | Ayrı mahalle yolları |
| Cgroup v2 | Kaynak tüketimini sınırlar | Elektrik, su, internet kotası |

Bir konteynerin kök dosya sistemine ihtiyacı vardır. Debian tabanlı küçük bir rootfs hazırlamak için örnek:

```bash
sudo debootstrap --variant=minbase bookworm ./rootfs http://deb.debian.org/debian
sudo mkdir -p ./rootfs/{proc,sys,tmp}
```

Burada `rootfs`, konteynerin kendi dünyasıdır. `chroot` ile bir sürecin kök dizinini buraya çevirebiliriz; fakat tek başına `chroot` güvenlik sınırı değildir. Asıl izolasyonu `unshare` komutu ile namespace oluşturarak sağlarız.

Şimdi küçük motorumuzun iskeletini yazalım:

```bash
cat > mini-run.sh <<'SH'
#!/usr/bin/env bash
set -euo pipefail

ROOTFS=${ROOTFS:-./rootfs}
ID=${1:-demo}
CG=/sys/fs/cgroup/mini-$ID

mkdir -p $CG
echo +cpu +memory +pids > /sys/fs/cgroup/cgroup.subtree_control 2>/dev/null || true
echo '50000 100000' > $CG/cpu.max
echo $((128*1024*1024)) > $CG/memory.max
echo 64 > $CG/pids.max

unshare --fork --pid --mount --uts --ipc --net --mount-proc \
  chroot $ROOTFS /bin/bash -lc 'hostname mini; mount -t proc proc /proc; exec /bin/bash' &

CHILD=$!
echo $CHILD > $CG/cgroup.procs
wait $CHILD
rm -rf $CG
SH

chmod +x mini-run.sh
sudo ./mini-run.sh ilk-konteyner
```

Bu betik birkaç kritik şey yapar. Önce cgroup dizini açar, sonra CPU, bellek ve süreç sayısı sınırı koyar. `cpu.max` satırındaki `50000 100000`, her 100000 mikrosaniyelik periyotta 50000 mikrosaniye CPU hakkı demektir. Yani $oran = 50000 / 100000 = 0.5$; kabaca yarım CPU çekirdeği. Bellek sınırı ise $128 * 1024 * 1024$ bayt, yani 128 MB olur.

`unshare` tarafı daha eğlenceli. `--pid` ile içerideki kabuk kendini yeni bir süreç ağacında görür. `--mount` sayesinde mount değişiklikleri dışarı sızmaz. `--uts` hostname değiştirmeye izin verir. `--net` yeni ve boş bir ağ namespace açar; bu yüzden konteyner ilk anda internetsizdir. Gerçek motorlar burada veth çifti, bridge ve NAT kurar.

| Eksik parça | Bizde durum | Docker gibi motorlarda |
|---|---|---|
| Image katmanları | Yok, tek rootfs | OverlayFS katmanları |
| Ağ | Boş namespace | Bridge, veth, iptables veya nftables |
| Güvenlik | Temel izolasyon | Seccomp, AppArmor, capability azaltma |
| Yaşam döngüsü | Basit wait | start, stop, logs, exec |

Ağ eklemek istersen fikir şudur: host tarafında bir bridge oluşturulur, konteyner namespace içine bir veth ucu taşınır, IP verilir ve NAT açılır. Bunu elle yapmak öğreticidir ama dağıtıma göre komutlar değişebilir.

Önemli uyarı: Bu betiği root yetkisiyle çalıştırırsın ve bu bir öğrenme aracıdır. Güvenli konteyner motoru yazmak; capability düşürme, salt okunur mount, kullanıcı namespace, seccomp profili ve dikkatli cleanup gerektirir.

Sonuç olarak konteyner, gizemli bir kutu değil; iyi düzenlenmiş bir Linux illüzyonudur. Namespace sürece ayrı bir evren gösterir, cgroup o evrende ne kadar kaynak yakabileceğini belirler, rootfs ise dekoru tamamlar. Docker veya Podman kullandığında artık sadece komut çalıştırmış olmayacaksın; çekirdeğin hangi düğmelerine basıldığını da zihninde göreceksin.
