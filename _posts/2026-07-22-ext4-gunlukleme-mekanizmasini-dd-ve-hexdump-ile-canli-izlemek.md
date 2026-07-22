---
layout: post
title: "ext4 Günlükleme Mekanizmasını dd ve hexdump ile Canlı İzlemek"
math: true
categories: 
  - Proje
tags: 
  - ext4
  - linux
  - dd
  - hexdump
  - dosya-sistemi
---

ext4 dosya sisteminde bir dosya yazdığınızda verinin diske “hop diye” gitmediğini bilmek, Linux’un perde arkasını anlamak için harika bir başlangıçtır. Bu yazıda güvenli bir loop imaj üzerinde ext4 günlük bölgesini bulup, yazma işlemi sırasında `dd` ve `hexdump` ile anlık izleyen küçük bir Bash betiği hazırlayacağız. Gerçek diskinize dokunmadan, dosya sisteminin kalp atışlarını dinleyeceğiz.
``

ext4’ün günlükleme mekanizması, özellikle sistem çökmesi veya elektrik kesintisi gibi durumlarda dosya sisteminin tutarlı kalmasını sağlar. Basit fikir şudur: Kritik meta veri değişiklikleri önce “journal” denen özel bir alana yazılır, ardından asıl konumlarına uygulanır. Böylece sistem yarıda kesilirse ext4, günlüğe bakarak işlemi tamamlayabilir veya geri alabilir.

Teorik olarak bunu küçük bir işlem sırası gibi düşünebiliriz:

$$T = \{metadata\ write, commit\ block, checkpoint\}$$

Burada `commit block`, “bu işlem grubu tamamlandı” damgası gibidir. ext4 varsayılan olarak genellikle `data=ordered` kipinde çalışır: dosya verisi asıl yerine yazılır, meta veri ise journal üzerinden güvenceye alınır.

| Kip | Veri journal’a yazılır mı? | Meta veri journal’a yazılır mı? | Performans |
|---|---:|---:|---:|
| `data=journal` | Evet | Evet | Daha yavaş, daha güvenli |
| `data=ordered` | Hayır, önce diske gider | Evet | Dengeli |
| `data=writeback` | Hayır | Evet | Hızlı, sıralama garantisi zayıf |

Journal alanı ext4 içinde çoğunlukla özel bir inode olarak tutulur: inode `8`. Biz bu inode’un fiziksel bloklarını `debugfs` ile bulacağız. Bir blok numarası $P$, blok boyutu $B$ ise byte cinsinden konum:

$$offset = P \times B$$

`dd` komutu bu ofsete gidip blokları okuyacak, `hexdump` da bize ham içeriği gösterecek.

Önce güvenli bir laboratuvar oluşturalım:

```bash
truncate -s 256M ext4-lab.img
mkfs.ext4 -F ext4-lab.img
mkdir -p mnt-lab
sudo mount -o loop ext4-lab.img mnt-lab
```

Şimdi izleme betiğimiz gelsin. Bu betik imaj dosyasından blok boyutunu öğrenir, journal inode’unun ilk extent’ini bulur ve belirli aralıklarla o bölgeden veri okuyup hexadecimal biçimde gösterir.

```bash
#!/usr/bin/env bash
set -euo pipefail

IMG="${1:-ext4-lab.img}"
BLOCKS_TO_READ="${2:-4}"
INTERVAL="${3:-1}"

if [[ ! -f "$IMG" ]]; then
  echo "İmaj bulunamadı: $IMG" >&2
  exit 1
fi

BS=$(dumpe2fs -h "$IMG" 2>/dev/null | awk -F: '/Block size/ {gsub(/ /,"",$2); print $2}')

JOURNAL_RANGE=$(debugfs -R 'stat <8>' "$IMG" 2>/dev/null \
  | awk '
    match($0, /\):([0-9]+)-([0-9]+)/, a) { print a[1], a[2]; exit }
    match($0, /\):([0-9]+)/, a) { print a[1], a[1]; exit }
  ')

START_BLOCK=$(echo "$JOURNAL_RANGE" | awk '{print $1}')
END_BLOCK=$(echo "$JOURNAL_RANGE" | awk '{print $2}')

if [[ -z "${START_BLOCK:-}" ]]; then
  echo "Journal blokları bulunamadı. debugfs çıktısını kontrol edin." >&2
  exit 1
fi

OFFSET=$((START_BLOCK * BS))

printf "Blok boyutu      : %s byte\n" "$BS"
printf "Journal başlangıcı: blok %s\n" "$START_BLOCK"
printf "Journal bitişi    : blok %s\n" "$END_BLOCK"
printf "Okunan offset     : %s byte\n\n" "$OFFSET"

while true; do
  clear
  date
  echo "Journal bölgesinden $BLOCKS_TO_READ blok okunuyor..."
  dd if="$IMG" bs="$BS" skip="$START_BLOCK" count="$BLOCKS_TO_READ" status=none \
    | hexdump -C | head -n 40
  sleep "$INTERVAL"
done
```

Kaydedip çalıştırın:

```bash
chmod +x watch-ext4-journal.sh
./watch-ext4-journal.sh ext4-lab.img 8 1
```

Başka bir terminalde dosya sistemine yazma yapalım:

```bash
for i in {1..20}; do
  sudo dd if=/dev/urandom of=mnt-lab/file-$i.bin bs=1M count=2 status=none
  sync
  sleep 1
done
```

İzleme ekranında bazı byte dizilerinin değiştiğini göreceksiniz. Bunlar her zaman “dosya içeriği” değildir; çoğunlukla inode, dizin girdisi, blok bitmap’i gibi meta veri değişikliklerinin journal kayıtlarıdır.

| Araç | Görevi | Neden kullanıyoruz? |
|---|---|---|
| `dumpe2fs` | ext4 süper blok bilgisini okur | Blok boyutunu öğrenmek için |
| `debugfs` | ext dosya sistemini inceler | Journal inode’unun bloklarını bulmak için |
| `dd` | Ham blok okur/yazar | Journal bölgesini doğrudan okumak için |
| `hexdump` | Byte’ları okunabilir gösterir | Değişimleri gözlemlemek için |

Buradaki önemli nokta şudur: ext4 journal’ı bir metin günlüğü değildir; insanlar için değil, dosya sisteminin kendisi için tasarlanmış ikili bir yapıdır. Yani ekranda anlamlı cümleler değil, işlem kayıtlarının ham temsillerini görürsünüz. Yine de yazma yaptıkça bu alanın değiştiğini izlemek, journal fikrini soyut bir kavram olmaktan çıkarır.

Deney bitince temizleyin:

```bash
sudo umount mnt-lab
rmdir mnt-lab
rm ext4-lab.img
```

Bu küçük proje sayesinde ext4’ün “önce not al, sonra uygula” mantığını canlı gözlemledik. Dosya sistemleri sessiz çalışır; ama doğru araçlarla bakınca oldukça konuşkandırlar.
