---
layout: post
title: "Terminalde ANSI Kaçış Kodlarıyla Gerçek Zamanlı Yılan Oyunu"
math: true
categories: 
  - Proje
tags: 
  - ANSI
  - terminal
  - python
  - oyun-programlama
  - kaçış-kodları
---

Terminali sadece komut yazılan siyah bir kutu sanıyorsan, bugün biraz sihir yapıyoruz: ANSI kaçış kodlarıyla imleci piksel gibi oynatıp, renkleri değiştirip, gerçek zamanlı bir yılan oyunu tasarlayacağız. Buradaki amaç yalnızca “Snake yaptık” demek değil; terminalin nasıl çizim alanına dönüştüğünü, klavye girişinin nasıl anlık okunduğunu ve oyun döngüsünün nasıl çalıştığını anlamak.
``
ANSI kaçış kodları, terminale “şuraya git”, “rengi kırmızı yap”, “ekranı temizle” gibi komutlar gönderen özel metin dizileridir. Genelde `\x1b[` ile başlarlar. Buradaki `\x1b`, ESC karakteridir. Örneğin `\x1b[2J` ekranı temizler, `\x1b[10;20H` imleci 10. satır 20. sütuna taşır. Yani terminalde grafik çizmenin en temel fikri şudur: karakterleri doğru koordinatlara basmak.

Yılan oyununu modellemek için birkaç kavram yeterlidir. Yılanın gövdesi koordinat çiftlerinden oluşan bir listedir: `[(x1,y1), (x2,y2), ...]`. Her karede baş, mevcut yöne göre ilerler. Matematiksel olarak bunu şöyle düşünebiliriz: $p_{t+1}=p_t+v_t$. Burada $p$ konum, $v$ ise yöndür. Sağ için $(1,0)$, sol için $(-1,0)$, aşağı için $(0,1)$ kullanırız. Kenarlardan geçişli bir harita istersek yeni konumu mod ile hesaplarız: $x=(x+dx) \bmod W$.

| ANSI kodu | Görevi | Oyundaki kullanımı |
|---|---|---|
| `\x1b[2J` | Ekranı temizler | Başlangıçta alanı sıfırlar |
| `\x1b[?25l` | İmleci gizler | Daha temiz görüntü sağlar |
| `\x1b[y;xH` | İmleci taşır | Yılan ve yem çizimi |
| `\x1b[32m` | Yeşil renk | Yılan gövdesi |
| `\x1b[0m` | Stili sıfırlar | Renk sızıntısını engeller |

Gerçek zamanlılık için klasik `input()` kullanamayız; çünkü Enter bekler. Python’da terminali “raw mode”a alarak tuşları anında okuyabiliriz. Aşağıdaki örnek, Linux/macOS terminallerinde çalışacak sade bir çekirdektir. Windows tarafında ANSI desteği yeni terminallerde vardır, fakat anlık tuş okuma için ek uyarlama gerekebilir.

```python
import sys, time, random, select, tty, termios

W, H = 40, 20
ESC = '\x1b['

def move(x, y):
    return f'{ESC}{y};{x}H'

def color(c):
    return f'{ESC}{c}m'

def draw(snake, food, score):
    out = []
    out.append(move(1, 1) + color(36) + f'Skor: {score}' + color(0))
    out.append(move(food[0], food[1]) + color(31) + '●' + color(0))
    for i, (x, y) in enumerate(snake):
        ch = '◎' if i == 0 else '■'
        out.append(move(x, y) + color(32) + ch + color(0))
    sys.stdout.write(''.join(out))
    sys.stdout.flush()

def read_key():
    if select.select([sys.stdin], [], [], 0)[0]:
        return sys.stdin.read(1)
    return None

old = termios.tcgetattr(sys.stdin)
try:
    tty.setcbreak(sys.stdin)
    sys.stdout.write(ESC + '2J' + ESC + '?25l')

    snake = [(10, 10), (9, 10), (8, 10)]
    direction = (1, 0)
    food = (random.randint(2, W), random.randint(3, H))
    score = 0

    while True:
        key = read_key()
        if key == 'q': break
        if key == 'w' and direction != (0, 1): direction = (0, -1)
        if key == 's' and direction != (0, -1): direction = (0, 1)
        if key == 'a' and direction != (1, 0): direction = (-1, 0)
        if key == 'd' and direction != (-1, 0): direction = (1, 0)

        hx, hy = snake[0]
        dx, dy = direction
        head = ((hx + dx - 1) % W + 1, (hy + dy - 2) % (H - 1) + 2)

        if head in snake:
            break

        snake.insert(0, head)
        if head == food:
            score += 1
            food = (random.randint(2, W), random.randint(3, H))
        else:
            tail = snake.pop()
            sys.stdout.write(move(tail[0], tail[1]) + ' ')

        draw(snake, food, score)
        time.sleep(max(0.04, 0.12 - score * 0.003))
finally:
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old)
    sys.stdout.write(ESC + '?25h' + ESC + '0m' + '\n')
```

Kodda önemli bir performans hilesi var: Her karede tüm ekranı temizlemek yerine sadece değişen hücreleri çiziyoruz. Kuyruğun eski konumuna boşluk basılıyor, yeni baş koordinatına sembol yazılıyor. Bu yaklaşım titremeyi azaltır. Eğer her karede `\x1b[2J` kullanırsan oyun çalışır ama göz kırpan bir disko topuna dönüşebilir.

| Yaklaşım | Avantaj | Dezavantaj |
|---|---|---|
| Tüm ekranı temizle | Kod basit | Titreme fazladır |
| Sadece değişeni çiz | Akıcı görüntü | Durum takibi gerekir |
| `curses` kullan | Hazır araçlar | ANSI mantığı daha gizli kalır |
| Saf ANSI | Öğretici ve hafif | Platform farklarına dikkat ister |

Renk geçişleri için skora göre ANSI renkleri değiştirebilirsin. Örneğin düşük skorda yeşil, orta skorda sarı, yüksek skorda mor yılan kullanmak mümkündür. Hatta RGB destekleyen terminallerde `\x1b[38;2;R;G;Bm` biçimiyle gerçek renkler kullanılabilir. Böylece $renk=f(skor)$ gibi küçük bir fonksiyonla oyuna görsel ilerleme hissi katarsın.

Sonuç olarak terminalde yılan oyunu yapmak, oyun programlamanın minyatür laboratuvarı gibidir: koordinat sistemi, olay okuma, zamanlama, çarpışma kontrolü ve render mantığı tek dosyada buluşur. Üstelik tüm bunları grafik kütüphanesi olmadan, yalnızca metin ve birkaç kaçış koduyla yapmak oldukça tatmin edici. Bir sonraki adım olarak duvarlar, seviye sistemi veya renkli parçacık efektleri ekleyebilirsin; terminal sandığından daha canlı bir sahne!
