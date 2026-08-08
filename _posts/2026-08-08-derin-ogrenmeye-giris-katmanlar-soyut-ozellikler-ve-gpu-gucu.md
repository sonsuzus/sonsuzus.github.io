---
layout: post
title: "Derin Öğrenmeye Giriş: Katmanlar, Soyut Özellikler ve GPU Gücü"
math: true
categories: 
  - Bilgi
tags: 
  - derin öğrenme
  - yapay sinir ağları
  - GPU
---

Bir bilgisayara kediyi tanımayı öğretmek istediğimizi düşünelim. Geleneksel yaklaşımda sivri kulak, bıyık ve kuyruk gibi özellikleri tek tek tarif etmemiz gerekebilir. Derin öğrenmede ise modele yeterli sayıda örnek gösteririz; hangi ayrıntıların önemli olduğunu katmanlar boyunca kendisi keşfeder. İşin büyülü görünen, fakat matematik ve bol miktarda hesaplama gücüne dayanan kısmı tam olarak budur.

``

## Derin öğrenme neden “derin”?

Yapay sinir ağları, girdileri belirli ağırlıklarla işleyen yapay nöronlardan oluşur. Tek bir nöronun temel işlemi şöyle gösterilebilir:

$$z = \sum_{i=1}^{n} w_i x_i + b$$

Burada $x_i$ girdileri, $w_i$ öğrenilen ağırlıkları, $b$ ise bias değerini temsil eder. Sonuç genellikle ReLU gibi doğrusal olmayan bir aktivasyon fonksiyonundan geçirilir:

$$\operatorname{ReLU}(z)=\max(0,z)$$

Bir ağın “derin” olması, giriş ile çıkış arasında birden fazla gizli katman bulunması anlamına gelir. Katman sayısı arttıkça model, özellikleri hiyerarşik biçimde birleştirebilir. Bir görüntü ağının ilk katmanları kenarları, sonraki katmanları dokuları, daha ilerideki katmanları ise göz, tekerlek veya yüz gibi soyut yapıları öğrenebilir.

| Mimari düzeyi | Öğrenilebilen özellik | Görüntü örneği |
|---|---|---|
| İlk katmanlar | Kenar, yön ve renk geçişi | Dikey çizgi |
| Orta katmanlar | Doku ve basit şekil | Kürk veya daire |
| Derin katmanlar | Nesne parçaları | Kulak veya göz |
| Çıkış katmanı | Sınıf veya tahmin | Kedi olasılığı |

Bu özellikler geliştirici tarafından elle yazılmaz. Eğitim sırasında tahmin hatası geriye yayılım ile katmanlara dağıtılır. Ağırlıklar, kayıp fonksiyonunu azaltacak yönde güncellenir:

$$w \leftarrow w-\eta\frac{\partial L}{\partial w}$$

Buradaki $L$ kayıp fonksiyonu, $\eta$ ise öğrenme oranıdır. Kısacası ağ, hatalarından ders çıkarır; ancak bunu kahve molası vermeden milyonlarca kez yapar.

## GPU neden bu kadar önemli?

Derin ağların eğitimi çok sayıda matris çarpımı gerektirir. CPU az sayıda güçlü çekirdekle genel amaçlı işlemlerde başarılıdır. GPU ise binlerce daha küçük çekirdeği sayesinde aynı türden matematiksel işlemleri paralel çalıştırabilir.

| Donanım | Güçlü olduğu alan | Derin öğrenmedeki rolü |
|---|---|---|
| CPU | Sıralı işlemler ve uygulama mantığı | Veri hazırlama, küçük modeller |
| GPU | Yoğun paralel hesaplama | Eğitim ve hızlı çıkarım |
| TPU/NPU | Yapay zekâya özel işlemler | Büyük ölçekli veya mobil modeller |

GPU seçiminde yalnızca işlem hızı değil, VRAM kapasitesi de önemlidir. Model parametreleri, ara aktivasyonlar ve gradyanlar bellekte tutulur. Bellek yetmediğinde batch boyutu küçültülebilir, karma hassasiyet kullanılabilir veya model birkaç GPU’ya dağıtılabilir. Daha büyük GPU her zaman daha akıllı model demek değildir; bazen yalnızca elektrik faturasının daha atletik olması demektir.

## PyTorch ile cihaz seçimi

Aşağıdaki örnek, varsa CUDA destekli GPU’yu seçer ve basit bir ağı ilgili cihaza taşır:

```python
import torch
from torch import nn

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = nn.Sequential(
    nn.Linear(784, 256),
    nn.ReLU(),
    nn.Linear(256, 10)
).to(device)

sample = torch.randn(64, 784).to(device)
predictions = model(sample)
print(device, predictions.shape)
```

`to(device)` çağrısı hem modelin hem de verinin aynı donanıma taşınmasını sağlar. Aksi hâlde PyTorch, CPU ve GPU tensörlerini birlikte işleyemediği için hata üretir.

## Avantajlar ve sınırlar

Derin öğrenme; görüntü tanıma, doğal dil işleme, ses analizi ve üretken yapay zekâda elle özellik çıkarma ihtiyacını azaltır. Büyük ve karmaşık verilerde klasik yöntemlerden daha yüksek başarı sağlayabilir. Ayrıca önceden eğitilmiş modeller, transfer öğrenme ile daha küçük veri kümelerine uyarlanabilir.

Buna karşılık derin mimariler çok veri, enerji, zaman ve dikkatli hiperparametre ayarı ister. Katman eklemek başarıyı otomatik olarak artırmaz; aşırı öğrenme, kaybolan gradyan ve yüksek gecikme gibi sorunlar doğabilir. En iyi yaklaşım, probleme yetecek kadar derin bir model seçmek ve donanım gücünü ölçüm sonuçlarına göre kullanmaktır.
