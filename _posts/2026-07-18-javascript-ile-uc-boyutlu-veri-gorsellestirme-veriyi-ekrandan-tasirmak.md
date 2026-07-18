---
layout: post
title: "JavaScript ile Üç Boyutlu Veri Görselleştirme: Veriyi Ekrandan Taşırmak"
math: true
categories: 
  - Bilgi
tags: 
  - JavaScript
  - Three.js
  - Veri Görselleştirme
  - 3D Grafik
---

Bir tablo düşünün: binlerce satır, onlarca metrik, ilişkiler, kümeler ve zaman değişimleri... Excel bile iç çekiyor. İşte JavaScript ile üç boyutlu veri görselleştirme, bu karmaşayı döndürülebilir, yakınlaştırılabilir ve keşfedilebilir bir sahneye çevirir. Kullanıcı yalnızca grafiğe bakmaz; grafiğin içinde gezinir, düğümlere tıklar, kümeleri ayırır ve istatistiğin sakladığı hikâyeyi daha sezgisel biçimde yakalar.
``

## Neden 3D Görselleştirme?

Klasik 2D grafikler çoğu durumda harikadır; çizgi grafikler trendleri, sütun grafikler karşılaştırmaları, pasta grafikler oranları gösterir. Fakat veri çok boyutlu hale geldiğinde işler zorlaşır. Örneğin bir müşteri veri setinde yaş, gelir, satın alma sıklığı, lokasyon ve sosyal ağ bağlantıları aynı anda incelenmek istenebilir. 3D sahnede üç değişken eksenlere yerleştirilirken renk, boyut, parlaklık veya animasyonla ek değişkenler temsil edilebilir.

Basit bir eşleme şöyle düşünülebilir: veri noktası $d = (a, b, c)$ ise sahnedeki konumu $p = (x, y, z)$ olur. Ölçekleme genellikle şu mantıkla yapılır: $x = (a - minA) / (maxA - minA)$. Böylece farklı aralıklardaki değerler aynı görsel evrene taşınır.

| Yaklaşım | Güçlü Yön | Zayıf Yön | Uygun Kullanım |
|---|---|---|---|
| 2D Grafik | Hızlı anlaşılır | Boyut sayısı sınırlı | Raporlar, dashboardlar |
| 3D Grafik | Çok değişkenli keşif | Yanlış tasarlanırsa kafa karıştırır | Ağlar, kümeler, uzamsal veriler |
| Etkileşimli 3D | Kullanıcı keşfi sağlar | Performans optimizasyonu ister | Büyük veri analizi, simülasyon |

## Temel Teori: Sahne, Kamera, Nesne

Web tarafında 3D denince akla genellikle WebGL gelir. WebGL güçlüdür ama ham haliyle biraz dikenlidir. Bu yüzden Three.js gibi kütüphaneler kullanılır. Three.js dünyasında üç temel karakter vardır: sahne, kamera ve renderer. Sahne evrenin kendisidir, kamera kullanıcının gözüdür, renderer ise bu evreni ekrana çizen motordur.

Veri noktalarını kürelerle göstermek yaygın bir yaklaşımdır. Ağ görselleştirmelerinde düğümler küre, bağlantılar çizgi olarak modellenir. Bir düğümün büyüklüğü derece merkeziliğini gösterebilir. Örneğin bir ağda düğümün bağlantı sayısı $k$ ise yarıçap $r = sqrt(k)$ seçilebilir. Bu sayede çok bağlantılı düğümler görünür olur ama sahneyi ezmez.

## Mini Three.js Örneği

Aşağıdaki kod, veri noktalarını üç boyutlu uzayda küçük küreler olarak yerleştirir. Mantık şudur: her veri satırı bir konuma çevrilir, ardından sahneye mesh olarak eklenir.

```js
import * as THREE from 'three';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

camera.position.z = 80;

const data = [
  { x: 10, y: 25, z: 5, value: 12 },
  { x: -20, y: 5, z: 15, value: 30 },
  { x: 5, y: -15, z: -10, value: 18 }
];

const material = new THREE.MeshStandardMaterial({ color: 0x44aaff });
const light = new THREE.PointLight(0xffffff, 1);
light.position.set(40, 40, 40);
scene.add(light);

data.forEach(item => {
  const radius = Math.sqrt(item.value);
  const geometry = new THREE.SphereGeometry(radius, 24, 24);
  const point = new THREE.Mesh(geometry, material);
  point.position.set(item.x, item.y, item.z);
  scene.add(point);
});

function animate() {
  requestAnimationFrame(animate);
  scene.rotation.y += 0.003;
  renderer.render(scene, camera);
}

animate();
```

Bu örnekte `value` alanı kürenin boyutunu belirler. Büyük değerler büyük kürelere dönüşür. Gerçek projelerde renk skalası, tooltip, tıklama olayları ve filtreleme eklenerek grafik çok daha bilgilendirici hale gelir.

## Etkileşim Neden Kritik?

3D görselleştirmede kullanıcı kontrolü yoksa sahne kısa sürede süslü bir akvaryuma dönüşebilir. OrbitControls ile döndürme, raycasting ile tıklanan nesneyi bulma ve filtre panelleri ile veri katmanlarını açıp kapatma önemlidir.

| Etkileşim | Kullanıcıya Katkısı |
|---|---|
| Döndürme | Kümelerin arkasındaki yapıyı görür |
| Yakınlaştırma | Yoğun bölgeleri inceler |
| Tooltip | Noktanın ham değerlerini okur |
| Filtreleme | Gürültüyü azaltır |

## Performans ve Tasarım İpuçları

Her veri noktası ayrı mesh olursa binlerce nesnede performans düşebilir. Bu durumda InstancedMesh, BufferGeometry veya veri ön işleme teknikleri kullanılmalıdır. Ayrıca 3D her zaman daha iyi değildir. Eğer iki değişken anlatılacaksa 2D daha temizdir. 3D, gerçekten üçüncü boyut anlam katıyorsa kullanılmalıdır.

Sonuç olarak JavaScript, tarayıcıyı küçük bir veri laboratuvarına dönüştürür. Three.js, D3.js ve WebGL ekosistemiyle karmaşık istatistikleri yalnızca göstermek değil, yaşatmak mümkündür. Doğru ölçekleme, bilinçli görsel kodlama ve güçlü etkileşim birleştiğinde kullanıcılar veriye bakmaz; veriyle sohbet eder.
