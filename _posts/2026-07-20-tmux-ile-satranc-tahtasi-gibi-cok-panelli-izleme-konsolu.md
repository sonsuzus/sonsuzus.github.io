---
layout: post
title: "tmux ile Satranç Tahtası Gibi Çok Panelli İzleme Konsolu"
math: true
categories: 
  - Proje
tags: 
  - tmux
  - bash
  - devops
  - terminal
  - izleme
---

Bir sunucuda log, kuyruk, API, veritabanı ve sistem metriklerini aynı anda izlemek bazen dedektiflik oyunu gibidir: ipucu bir yerde akar, hata başka yerde patlar. Bu yazıda kabuk betikleri ve tmux kullanarak ekranı satranç tahtası gibi bölen, her bölmede ayrı bir sürecin canlı çıktısını gösteren eğlenceli ama işe yarar bir izleme konsolu hazırlayacağız.
``

## Fikir: Terminali Tahtaya Çevirmek

tmux, tek terminal içinde birden fazla pencere ve bölme yönetmemizi sağlayan terminal multiplexer aracıdır. Mantık basittir: bir tmux oturumu açarız, ekranı satır ve sütunlara böleriz, sonra her bölmeye farklı komut göndeririz.

Bir satranç tahtası 8x8 olabilir ama izleme konsolunda genelde 2x2, 2x3 veya 3x3 daha okunabilirdir. Matematiksel olarak toplam panel sayısını şöyle düşünebiliriz:

$P = r \times c$

Burada $r$ satır sayısı, $c$ sütun sayısıdır. Örneğin 3 satır ve 2 sütun için $P = 3 \times 2 = 6$ panel elde ederiz. Panel sayısı arttıkça görünürlük azalır; bu yüzden amaç “her şeyi göstermek” değil, “kritik şeyleri aynı anda okumak” olmalıdır.

| Düzen | Panel Sayısı | Kullanım Senaryosu | Okunabilirlik |
|---|---:|---|---|
| 2x2 | 4 | Küçük servis izleme | Çok iyi |
| 2x3 | 6 | API + worker + DB + log | İyi |
| 3x3 | 9 | Yoğun geliştirme ortamı | Orta |
| 4x4 | 16 | Gösterişli demo | Zayıf |

## İzlenecek Süreçleri Tanımlamak

Önce her panelde çalışacak komutları düşünelim. Bunlar gerçek servis komutları olabileceği gibi geliştirme sırasında kullanılan basit izleyiciler de olabilir.

| Panel | Komut | Amaç |
|---|---|---|
| API Log | `tail -f logs/api.log` | HTTP isteklerini izleme |
| Worker | `npm run worker` | Kuyruk tüketicisini çalıştırma |
| Sistem | `htop` | CPU ve RAM gözlemi |
| Docker | `docker stats` | Container kaynak kullanımı |
| Test | `watch -n 2 npm test` | Testleri periyodik koşturma |
| Disk | `watch -n 5 df -h` | Disk doluluğu kontrolü |

Bu yaklaşımın güzelliği şudur: tmux sadece ekranı böler; asıl zeka kabuk betiğinde hangi komutun nereye gideceğini tarif etmektedir.

## Betik: monitor.sh

Aşağıdaki betik 2x3 benzeri karo düzeninde bir tmux oturumu oluşturur ve her bölmeye ayrı komut yollar. Kod orta seviyededir: tmux komutlarını fonksiyonlaştırır, oturum zaten varsa yeniden bağlanır.

```bash
#!/usr/bin/env bash
set -euo pipefail

SESSION='watchboard'

commands=(
  'echo API log; tail -f logs/api.log'
  'echo Worker; npm run worker'
  'echo System; htop'
  'echo Docker; docker stats'
  'echo Tests; watch -n 2 npm test'
  'echo Disk; watch -n 5 df -h'
)

if tmux has-session -t "$SESSION" 2>/dev/null; then
  tmux attach -t "$SESSION"
  exit 0
fi

tmux new-session -d -s "$SESSION" -n board

# İlk panel zaten var. Diğer panelleri oluştur.
for i in 1 2 3 4 5; do
  tmux split-window -t "$SESSION":0
  tmux select-layout -t "$SESSION":0 tiled
done

# Komutları panellere gönder.
for i in "${!commands[@]}"; do
  tmux send-keys -t "$SESSION":0.$i "${commands[$i]}" C-m
done

tmux select-layout -t "$SESSION":0 tiled
tmux attach -t "$SESSION"
```

Çalıştırmak için:

```bash
chmod +x monitor.sh
./monitor.sh
```

Burada `split-window` yeni bölme açar, `select-layout tiled` bölmeleri otomatik olarak karo düzene sokar, `send-keys` ise seçilen bölmeye klavyeden yazıyormuşuz gibi komut gönderir. Yani betik aslında görünmez bir operatör gibi davranır.

## Neden tmux, Neden Sadece Terminal Değil?

Normalde altı terminal penceresi açabilirsiniz; fakat bu hem dağınıktır hem de uzak sunucuda çalışırken kullanışsızdır. tmux tek SSH bağlantısı içinde bütün panelleri korur. Bağlantınız koparsa süreçler yaşamaya devam eder.

| Özellik | Çoklu Terminal | tmux Konsolu |
|---|---|---|
| SSH kopunca durum | Genelde kaybolur | Oturum korunur |
| Düzen tekrarı | Elle yapılır | Betikle otomatik |
| Taşınabilirlik | Düşük | Yüksek |
| Klavye odaklı kullanım | Orta | Çok iyi |

## Küçük İyileştirmeler

Panel başlıklarını renklendirmek için komutların başına `printf` ekleyebilirsiniz. Ayrıca kritik loglarda `grep --line-buffered ERROR` kullanarak sadece hataları gösterebilirsiniz. Eğer panel sayınız $P > 9$ oluyorsa, okunabilirlik maliyeti artar; bunu kabaca $O(P)$ dikkat yükü gibi düşünebiliriz. Yani panel sayısı arttıkça beyninizin sekme yönetimi de artar.

## Sonuç

Kabuk betikleri ve tmux birleşince terminal basit bir siyah ekran olmaktan çıkıp canlı bir kontrol paneline dönüşür. Bu yapı özellikle mikroservis geliştirme, worker takibi, Docker izleme ve hızlı hata ayıklama için harikadır. En güzel tarafı da şu: Bir kez yazarsınız, sonra her sabah kahvenizi alıp `./monitor.sh` dersiniz; satranç tahtanız açılır ve hamle sırası artık sizdedir.
