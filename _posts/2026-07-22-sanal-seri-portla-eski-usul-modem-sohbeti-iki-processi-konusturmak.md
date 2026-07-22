---
layout: post
title: "Sanal Seri Portla Eski Usul Modem Sohbeti: İki Process’i Konuşturmak"
math: true
categories: 
  - Proje
tags: 
  - seri-port
  - socat
  - python
  - modem
  - process-communication
---

Bir zamanlar internete bağlanmak, kulak tırmalayan bir modem serenadı eşliğinde gerçekleşirdi. Bugün TCP soketleri, REST API’leri ve mesaj kuyruklarıyla yaşıyoruz; ama iki process arasında sanal seri port çifti kurup bir taraftan AT komutları gönderirken diğer taraftan cevap okumak, haberleşmenin temel mantığını anlamak için hâlâ şahane bir laboratuvar deneyidir.
``

## Fikir: Kablo Yok, Ama Seri Hat Var

Seri port haberleşmesi temelde baytların sırayla akmasıdır. Bir uç yazar, diğer uç okur. Gerçek dünyada bu iki ucu RS-232 kablosu bağlar; sanal dünyada ise işletim sistemi içinde oluşturulan bir port çifti bağlar. Linux’ta bunun için en pratik araçlardan biri `socat`tır. Windows tarafında benzer fikir için com0com, macOS/Linux tarafında ise `socat` veya `tty0tty` kullanılabilir.

Seri haberleşmede sık duyulan `9600 8N1` ifadesi şunu anlatır: saniyede 9600 bit, 8 veri biti, parity yok, 1 stop biti. Aslında her karakter yalnızca 8 bit değildir; start ve stop bitleriyle birlikte yaklaşık 10 bit taşınır. Bu yüzden teorik karakter hızı yaklaşık $9600 / 10 = 960$ byte/s olur. Genel olarak $R_{byte} \approx \frac{baud}{start + data + parity + stop}$ diyebiliriz.

| Kavram | Eski modem dünyası | Sanal seri port dünyası |
|---|---|---|
| Fiziksel hat | Telefon kablosu | İşletim sistemi içi PTY |
| Komut dili | AT komutları | Bizim taklit ettiğimiz metin protokolü |
| Gecikme | Hat kalitesi ve modem | Process zamanlaması |
| Hata kaynağı | Gürültü, kopma | Buffer, timeout, yanlış ayar |

## Sanal Port Çiftini Kurmak

Linux’ta iki uçlu sahte bir seri kabloyu şöyle oluşturabiliriz:

```bash
socat -d -d pty,raw,echo=0,link=/tmp/ttyV0 pty,raw,echo=0,link=/tmp/ttyV1
```

Bu komut `/tmp/ttyV0` ve `/tmp/ttyV1` adında iki sanal uç üretir. Birine yazılan veri diğerinden okunur. `raw` modu karakterleri pişirmeden geçirir, `echo=0` ise yazdığımız karakterlerin aynı uçtan geri dönmesini engeller. Gerekirse ayarları klasik terminal aracıyla da sabitleyebiliriz:

```bash
stty -F /tmp/ttyV0 9600 cs8 -cstopb -parenb raw -echo
stty -F /tmp/ttyV1 9600 cs8 -cstopb -parenb raw -echo
```

## Process 1: Komut Gönderen Terminal

Aşağıdaki Python betiği kendini eski bir terminal programı gibi davranmaya zorlar. `ATZ`, `ATI` ve `ATD5551234` komutlarını sırayla yollar, gelen cevapları okur.

```python
import serial
import time

port = serial.Serial('/tmp/ttyV0', 9600, timeout=1)

commands = [b'ATZ\r', b'ATI\r', b'ATD5551234\r']

for cmd in commands:
    print('Gonderiliyor:', cmd)
    port.write(cmd)
    time.sleep(0.2)
    response = port.read(128)
    print('Cevap:', response)

port.close()
```

Burada önemli nokta satır sonudur. Modemler genellikle komutun bittiğini carriage return, yani `\r` ile anlar. Modern metin dosyalarındaki `\n` alışkanlığı seri dünyada her zaman yeterli değildir.

## Process 2: Modem Rolü Yapan Okuyucu

İkinci process diğer ucu dinler. Gelen komutu buffer’a alır, `\r` görünce işler ve uygun cevabı üretir.

```python
import serial

modem = serial.Serial('/tmp/ttyV1', 9600, timeout=1)
buffer = b''

while True:
    b = modem.read(1)
    if not b:
        continue

    buffer += b
    if b == b'\r':
        command = buffer.strip().upper()
        print('Komut alindi:', command)

        if command == b'ATZ':
            modem.write(b'OK\r\n')
        elif command == b'ATI':
            modem.write(b'VIRTUAL MODEM 1.0\r\nOK\r\n')
        elif command.startswith(b'ATD'):
            modem.write(b'CONNECT 9600\r\n')
        else:
            modem.write(b'ERROR\r\n')

        buffer = b''
```

Bu küçük döngü aslında protokol tasarımının minyatür hâlidir: veri birikir, ayraç görülür, mesaj çözümlenir, cevap üretilir. TCP’de paketler, HTTP’de header’lar, MQTT’de frame’ler neyse; burada da `\r` odur.

## Neden Bu Deney Değerli?

Çünkü süreçler arası haberleşmeyi sihir olmaktan çıkarır. Bir API çağrısı da özünde kuralları belirlenmiş bayt alışverişidir. Burada hız, çerçeveleme ve zaman aşımı açıkça görünür. Baud rate düşükse kuyruk dolar; timeout kısa ise cevap kaçırılır; satır sonu yanlışsa modem sonsuza kadar bekler.

Küçük bir nostalji projesi gibi görünse de bu yöntem gömülü sistem testlerinde, donanım olmadan firmware simülasyonunda ve eski cihaz protokollerini tersine mühendislikle anlamada çok işe yarar. Üstelik iki process’i konuştururken duyulmayan o modem cızırtısını zihniniz otomatik tamamlar: cııııııık, hrrr, bıp... CONNECT 9600!
