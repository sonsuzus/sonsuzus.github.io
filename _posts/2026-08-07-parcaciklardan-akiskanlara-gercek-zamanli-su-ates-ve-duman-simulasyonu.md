---
layout: post
title: "Parçacıklardan Akışkanlara: Gerçek Zamanlı Su, Ateş ve Duman Simülasyonu"
math: true
categories: 
  - Proje
tags: 
  - parçacık sistemi
  - fizik motoru
  - akışkan simülasyonu
---

Bir avuç noktanın su gibi akmasını, ateş gibi yükselmesini veya duman gibi havada süzülmesini sağlamak ilk bakışta büyücülük gibi görünebilir. Oysa gerçek zamanlı akışkan simülasyonlarının temelinde parçacıklar, kuvvetler ve her karede tekrarlanan birkaç fizik hesabı bulunur. Tam ölçekli bilimsel doğruluk yerine görsel inandırıcılığı hedefleyerek tarayıcıda bile çalışan eğlenceli bir mini fizik motoru geliştirebiliriz.
``
## Temel fikir: Her damla bir parçacık

Parçacık sistemi, akışkanı çok sayıda küçük nesneyle temsil eder. Her parçacığın konumu $\vec{x}$, hızı $\vec{v}$, kütlesi $m$, ömrü ve türüne özgü özellikleri bulunur. Simülasyon döngüsünde önce kuvvetler hesaplanır, ardından ivme, hız ve konum güncellenir.

Newton’un ikinci yasası başlangıç noktamızdır:

$$\vec{F}=m\vec{a} \quad \Rightarrow \quad \vec{a}=\frac{\vec{F}}{m}$$

Basit Euler integrasyonuyla güncelleme şöyledir:

$$\vec{v}_{t+\Delta t}=\vec{v}_t+\vec{a}\Delta t$$

$$\vec{x}_{t+\Delta t}=\vec{x}_t+\vec{v}_{t+\Delta t}\Delta t$$

Buradaki $\Delta t$, iki kare arasında geçen süredir. Sabit zaman adımı kullanmak simülasyonun farklı ekran yenileme hızlarında benzer davranmasını sağlar.

## Su, ateş ve duman neden farklı görünür?

Aynı motoru kullanıp kuvvetleri ve görsel özellikleri değiştirerek üç farklı akışkan izlenimi oluşturabiliriz.

| Özellik | Su | Ateş | Duman |
|---|---|---|---|
| Ana kuvvet | Aşağı yönlü yerçekimi | Yukarı yönlü kaldırma | Zayıf kaldırma ve rüzgâr |
| Parçacık ömrü | Uzun | Kısa | Orta veya uzun |
| Hareket | Yoğun ve yapışkan | Hızlı ve titreşimli | Yavaş ve dağınık |
| Görünüm | Mavi, yüksek opaklık | Sarıdan kırmızıya | Gri, giderek saydam |
| Çarpışma | Zemin ve kaplarla önemli | Genellikle gereksiz | Genellikle gereksiz |

Su için yerçekimi, yüzey çarpışmaları ve komşu parçacıklar arasında itme kuvveti gerekir. Basitleştirilmiş basınç kuvveti, iki parçacık arasındaki uzaklık $r$ etkileşim yarıçapı $h$ değerinden küçükse uygulanabilir:

$$F_p=k(h-r)$$

Burada $k$, akışkanın ne kadar sıkışmaz görüneceğini belirleyen katsayıdır. Bu yaklaşım gerçek SPH yönteminin sadeleştirilmiş hâlidir; bilimsel olarak kusursuz değildir ama oyun efektleri için hızlıdır.

Ateşte negatif yerçekimi benzeri bir kaldırma kuvveti kullanılır. Parçacık yaşlandıkça boyutu büyütülür, rengi sarıdan turuncuya geçirilir ve opaklığı azaltılır. Duman da yükselir fakat rastgele rüzgâr kuvvetleriyle yatayda daha fazla savrulur.

## JavaScript ile çekirdek parçacık sınıfı

Aşağıdaki sınıf kuvvet biriktirme, Euler integrasyonu ve yaşam süresi yönetimini gerçekleştirir:

```js
class Particle {
  constructor(x, y, type) {
    this.x = x;
    this.y = y;
    this.vx = (Math.random() - 0.5) * 40;
    this.vy = 0;
    this.ax = 0;
    this.ay = 0;
    this.age = 0;
    this.life = type === 'fire' ? 1.2 : 3;
    this.type = type;
  }

  applyForce(fx, fy, mass = 1) {
    this.ax += fx / mass;
    this.ay += fy / mass;
  }

  update(dt) {
    const gravity = this.type === 'water' ? 500 : -80;
    const turbulence = this.type === 'water'
      ? 0
      : (Math.random() - 0.5) * 100;

    this.applyForce(turbulence, gravity);
    this.vx += this.ax * dt;
    this.vy += this.ay * dt;
    this.x += this.vx * dt;
    this.y += this.vy * dt;
    this.ax = this.ay = 0;
    this.age += dt;
  }

  get alive() {
    return this.age < this.life;
  }
}
```

Her animasyon karesinde parçacıklara kuvvet uygulanır, `update(dt)` çağrılır ve ömrü dolanlar diziden çıkarılır. Su parçacıkları zemine çarptığında `vy *= -0.3` ile sönümlü sekme uygulanabilir. Daha yapışkan bir sonuç için yatay hız da `vx *= 0.9` ile azaltılabilir.

## Performans ve görsel sihir

Parçacık sayısı yükseldiğinde bütün parçacık çiftlerini karşılaştırmak $O(n^2)$ maliyet oluşturur. Alanı ızgara hücrelerine bölerek yalnızca yakın hücrelerdeki komşuları test etmek maliyeti büyük ölçüde azaltır. Canvas üzerinde daire çizmek başlangıç için yeterlidir; WebGL kullanıldığında binlerce parçacık GPU üzerinde işlenebilir.

Son dokunuş fizik değil, sunumdur: suya yarı saydam katmanlar, ateşe additive blending, dumana yumuşak dokular ekleyin. Böylece basit denklemler, doğru renk ve hareket tercihleriyle şaşırtıcı derecede canlı bir akışkan gösterisine dönüşür.
