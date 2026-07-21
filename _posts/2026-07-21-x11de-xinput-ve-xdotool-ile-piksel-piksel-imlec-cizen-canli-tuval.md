---
layout: post
title: "X11’de xinput ve xdotool ile Piksel Piksel İmleç Çizen Canlı Tuval"
math: true
categories: 
  - Proje
tags: 
  - x11
  - xdotool
  - xinput
  - linux
  - python
---

Fare imlecini ekranda minik bir robot kalem gibi gezdirip, geçtiği yolu canlı olarak çizen bir tuval uygulaması kulağa biraz büyücülük gibi gelebilir. Aslında X11 dünyasında bu işin arkasında çok net bir mantık var: imleç konumunu oku, konumu bir önceki noktayla birleştir, gerekiyorsa imleci programatik olarak bir piksel kaydır ve tekrar et.
``

X11, Linux masaüstlerinde uzun yıllardır kullanılan bir pencereleme sistemidir. Burada uygulamalar “client”, ekran, klavye ve fare gibi kaynakları yöneten yapı ise “server” gibi düşünülebilir. Fare imleci de bu sunucunun yönettiği ortak bir varlıktır. Biz `xinput` ile giriş aygıtlarını ve olaylarını gözlemleyebilir, `xdotool` ile imleci hareket ettirebilir veya konumunu okuyabiliriz.

Temel matematik oldukça sade. İmlecin ekrandaki konumunu şu vektörle temsil edelim: $p_t = (x_t, y_t)$. Bir sonraki örnekte elimizde $p_{t+1} = (x_{t+1}, y_{t+1})$ varsa, tuvale çizeceğimiz çizgi parçası bu iki noktanın birleşimidir. İmleci piksel piksel hareket ettirmek istediğimizde ise her adımda $\Delta x$ ve $\Delta y$ değerlerini genellikle $-1$, $0$ veya $1$ seçeriz. Böylece hareket, büyük sıçramalar yerine minik adımlar halinde gerçekleşir.

| Araç | Görevi | Bu projedeki rolü |
|---|---|---|
| `xinput` | Giriş aygıtlarını ve olaylarını izler | Fareyi tanımak, X11 olay mantığını görmek |
| `xdotool` | X11 üzerinde klavye/fare otomasyonu yapar | İmleci taşımak ve konum okumak |
| Python Tkinter | Basit GUI tuvali sağlar | İmleç yolunu canlı çizmek |

Önce sistemde gerekli araçları kurarak başlayalım:

```bash
sudo apt install xdotool xinput python3-tk
```

Fare aygıtlarını görmek için:

```bash
xinput list
```

Daha detaylı olay akışını izlemek isterseniz şu komut faydalıdır:

```bash
xinput test-xi2 --root
```

Bu çıktı, X11’in fare hareketini nasıl olaylara dönüştürdüğünü anlamak için harikadır. Ancak canlı çizim uygulamasında pratiklik adına konumu `xdotool getmouselocation` ile okuyacağız.

Aşağıdaki Python kodu bir Tkinter penceresi açar, imlecin ekran koordinatlarını düzenli olarak okur ve önceki konumla yeni konum arasına çizgi çeker. Ayrıca küçük bir otomasyon fonksiyonu, imleci piksel piksel hareket ettirerek ekranda iz bırakmasını sağlar.

```python
import tkinter as tk
import subprocess
import time
import threading

WIDTH, HEIGHT = 900, 600
last_point = None

def get_mouse_position():
    out = subprocess.check_output(['xdotool', 'getmouselocation']).decode()
    parts = dict(item.split(':') for item in out.split() if ':' in item)
    return int(parts['x']), int(parts['y'])

def move_relative(dx, dy):
    subprocess.call(['xdotool', 'mousemove_relative', '--sync', '--', str(dx), str(dy)])

def draw_loop():
    global last_point
    x, y = get_mouse_position()

    # Ekran koordinatlarını basitçe tuval sınırlarına sıkıştırıyoruz.
    cx = max(0, min(WIDTH, x))
    cy = max(0, min(HEIGHT, y))

    if last_point is not None:
        canvas.create_line(last_point[0], last_point[1], cx, cy, fill='lime', width=2)

    last_point = (cx, cy)
    root.after(16, draw_loop)  # Yaklaşık 60 FPS örnekleme

def pixel_walk():
    # Küçük kare benzeri bir rota: sağ, aşağı, sol, yukarı
    route = [(1, 0)] * 120 + [(0, 1)] * 80 + [(-1, 0)] * 120 + [(0, -1)] * 80
    for dx, dy in route:
        move_relative(dx, dy)
        time.sleep(0.01)

def start_walk():
    threading.Thread(target=pixel_walk, daemon=True).start()

root = tk.Tk()
root.title('X11 Canlı İmleç Tuvali')
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='black')
canvas.pack()

button = tk.Button(root, text='Piksel Piksel Yürüt', command=start_walk)
button.pack(fill='x')

draw_loop()
root.mainloop()
```

Burada `draw_loop` fonksiyonu kalp atışı gibidir. Her 16 milisaniyede bir imlecin nerede olduğunu sorar. Eğer önceki nokta biliniyorsa, iki nokta arasına çizgi çeker. Bu yüzden imleç hızlı hareket etse bile yol, kesik noktalar yerine çizgi segmentleri olarak görünür. `pixel_walk` ise imleci küçük adımlarla gezdirir; yani bizim minik robot ressamımızdır.

Koordinat dönüşümü önemlidir. Örnekte ekran koordinatlarını doğrudan tuval sınırlarına sıkıştırdık. Daha doğru bir yaklaşım için ekran boyutu $S_w \times S_h$, tuval boyutu $C_w \times C_h$ ise dönüşüm şöyle olabilir: $c_x = x \cdot C_w / S_w$, $c_y = y \cdot C_h / S_h$.

| Yaklaşım | Avantaj | Dezavantaj |
|---|---|---|
| Doğrudan koordinat kullanımı | Basit ve hızlı | Büyük ekranlarda taşma olabilir |
| Ölçekli dönüşüm | Her ekrana uyumlu | Biraz daha hesaplama ister |
| `xinput` olay ayrıştırma | Daha gerçek zamanlı | Çıktı parse etmek zahmetli |

Bu proje X11’in ne kadar esnek olduğunu gösteren eğlenceli bir örnektir. Wayland oturumlarında güvenlik nedeniyle bu komutların bazıları çalışmayabilir; bu yüzden denemeyi X11 oturumunda yapmalısınız. Sonuçta birkaç komut satırı aracı, biraz Python ve basit vektör mantığıyla imleci hem hareket ettiren hem de izini çizen canlı bir dijital eskiz defteri elde etmiş olduk.
