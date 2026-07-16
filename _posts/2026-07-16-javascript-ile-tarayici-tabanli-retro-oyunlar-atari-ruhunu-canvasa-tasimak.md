---
layout: post
title: "JavaScript ile Tarayıcı Tabanlı Retro Oyunlar: Atari Ruhunu Canvas’a Taşımak"
math: true
categories: 
  - Proje
tags: 
  - javascript
  - canvas
  - retro-oyun
---

Eski atari oyunlarının büyüsü, devasa grafik motorlarından değil; basit kuralların, hızlı geri bildirimin ve akıcı kontrollerin birleşiminden gelir. JavaScript, HTML ve biraz CSS ile tarayıcıda çalışan mini retro oyunlar yapmak, hem temel programlama mantığını pekiştirir hem de “oyun döngüsü” gibi yazılım dünyasının çok önemli kavramlarını eğlenceli biçimde öğretir.
``
Retro oyun dediğimizde akla Pong, Space Invaders, Snake veya Breakout gelir. Bu oyunların ortak noktası şudur: Ekranda birkaç şekil vardır, kullanıcı giriş yapar, nesneler hareket eder, çarpışmalar kontrol edilir ve skor güncellenir. Yani aslında elimizde küçük ama düzenli çalışan bir simülasyon vardır.

Tarayıcı tabanlı oyunlarda en popüler araçlardan biri **HTML5 Canvas**’tır. Canvas, piksel piksel çizim yapmamızı sağlayan bir sahne gibidir. JavaScript ise bu sahnedeki oyuncuları, topları, düşmanları ve puanları yöneten yönetmendir.

| Kavram | Web Karşılığı | Oyundaki Rolü |
|---|---|---|
| Sahne | `<canvas>` | Oyunun çizildiği alan |
| Yönetmen | JavaScript | Kuralları ve akışı kontrol eder |
| Kare | `requestAnimationFrame` | Her ekran yenilemesi |
| Oyuncu girdisi | Klavye / mouse eventleri | Karakteri hareket ettirir |
| Fizik | Basit matematik | Hız, yön, çarpışma |

Bir oyunun kalbi **game loop**, yani oyun döngüsüdür. Bu döngü genelde üç şey yapar: girdileri okur, oyun durumunu günceller, sonra ekrana çizer. Matematiksel olarak konum güncellemesini şöyle düşünebiliriz: $x_{yeni}=x+vx*dt$. Burada `x` konum, `vx` yatay hız, `dt` ise iki kare arasında geçen zamandır. Retro oyunlarda çoğu zaman bu formül yeterince güçlüdür.

Aşağıdaki örnek, Canvas üzerinde basit bir Pong topu hareketi oluşturur. Kodun amacı topu ekranda sektirmek ve temel oyun döngüsünü göstermektir:

```html
<canvas id='game' width='640' height='360'></canvas>
<script>
const canvas = document.getElementById('game');
const ctx = canvas.getContext('2d');

const ball = {
  x: 320,
  y: 180,
  r: 10,
  vx: 180,
  vy: 140
};

let lastTime = 0;

function update(dt) {
  ball.x += ball.vx * dt;
  ball.y += ball.vy * dt;

  if (ball.x < ball.r || ball.x > canvas.width - ball.r) {
    ball.vx *= -1;
  }

  if (ball.y < ball.r || ball.y > canvas.height - ball.r) {
    ball.vy *= -1;
  }
}

function draw() {
  ctx.fillStyle = '#111';
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  ctx.fillStyle = '#00ff99';
  ctx.beginPath();
  ctx.arc(ball.x, ball.y, ball.r, 0, Math.PI * 2);
  ctx.fill();
}

function loop(time) {
  const dt = (time - lastTime) / 1000;
  lastTime = time;

  update(dt);
  draw();
  requestAnimationFrame(loop);
}

requestAnimationFrame(loop);
</script>
```

Buradaki önemli detay `dt` kullanımıdır. Eğer sadece `ball.x += 3` yazsaydık, oyun farklı cihazlarda farklı hızlarda çalışabilirdi. `dt` sayesinde hareket zamana bağlanır. Yani saniyedeki kare sayısı değişse bile oyun daha tutarlı kalır. Basitçe hız formülü $v = mesafe / zaman$ mantığına dayanır.

Çarpışma kontrolü de retro oyunların vazgeçilmezidir. En basit yöntemlerden biri dikdörtgen çarpışmasıdır. İki kutu üst üste biniyorsa çarpışma vardır.

| Yöntem | Avantaj | Dezavantaj |
|---|---|---|
| Daire çarpışması | Top, mermi gibi nesnelerde kolaydır | Köşeli nesnelerde hassas değildir |
| Dikdörtgen çarpışması | Platform ve blok oyunları için idealdir | Dönen nesnelerde yetersiz kalır |
| Piksel kontrolü | Çok hassastır | Performans maliyeti yüksektir |

Klavye kontrolü için tuş durumlarını saklamak iyi bir pratiktir. Böylece tek tek “tuşa basıldı” olayına bağlı kalmak yerine, her karede mevcut durumu okuyabiliriz:

```js
const keys = {};
const player = { x: 40, y: 150, w: 12, h: 60, speed: 240 };

document.addEventListener('keydown', e => keys[e.key] = true);
document.addEventListener('keyup', e => keys[e.key] = false);

function updatePlayer(dt) {
  if (keys['ArrowUp']) player.y -= player.speed * dt;
  if (keys['ArrowDown']) player.y += player.speed * dt;

  player.y = Math.max(0, Math.min(360 - player.h, player.y));
}
```

Bu yapı, oyuncunun paddle’ını yukarı-aşağı hareket ettirir ve ekran dışına çıkmasını engeller. Aslında burada küçük bir durum makinesi kurmuş oluruz: tuş basılıysa hareket et, değilse bekle.

Retro hissi artırmak için piksel fontlar, sınırlı renk paleti, basit ses efektleri ve düşük çözünürlüklü görseller kullanabilirsiniz. Önemli olan, oyunu karmaşıklaştırmadan “oynanabilir döngüyü” hızlıca kurmaktır: başlat, oyna, kaybet, tekrar dene.

Sonuç olarak JavaScript ile retro oyun yapmak; değişkenler, fonksiyonlar, döngüler, olaylar, matematik ve durum yönetimi gibi temel konuları tek bir eğlenceli projede birleştirir. Bir topu sektirmekle başlayan yolculuk, kısa sürede kendi Pong’unuza, Snake’inize veya uzay nişancı oyununuza dönüşebilir. Üstelik tek ihtiyacınız olan şey bir tarayıcı, biraz merak ve bolca “bir tur daha” isteği!
