---
layout: post
title: "GAN ve Difüzyon Modelleri: Rekabetten Gürültüye Üretken Yapay Zekâ"
math: true
categories: 
  - Bilgi
tags: 
  - GAN
  - Difüzyon Modelleri
  - Üretken Yapay Zekâ
---

Bir yapay zekânın sıfırdan insan yüzü çizdiğini, kısa bir melodi bestelediğini veya birkaç kelimelik komuttan video ürettiğini düşünün. Bu sihrin arkasında çoğunlukla iki güçlü yaklaşım bulunur: birbirini alt etmeye çalışan ağlardan oluşan **Üretken Çekişmeli Ağlar (GAN)** ve gürültüyü adım adım temizleyen **difüzyon modelleri**. İkisi de öğrendiği veri dağılımından yeni örnekler üretir; ancak hedefe giderken tamamen farklı yollar izler.

``

## GAN: Sahtekâr ile dedektifin oyunu

GAN, 2014 yılında Ian Goodfellow ve çalışma arkadaşları tarafından tanıtıldı. Yapı, iki sinir ağından oluşur:

- **Üretici (Generator):** Rastgele gürültüyü gerçekçi bir örneğe dönüştürmeye çalışır.
- **Ayırt edici (Discriminator):** Karşısındaki örneğin gerçek veriden mi yoksa üreticiden mi geldiğini tahmin eder.

Üreticiyi sahte tablo yapan bir ressama, ayırt ediciyi ise sanat uzmanına benzetebiliriz. Ressam geliştikçe uzman daha dikkatli olur; uzman geliştikçe ressam daha başarılı sahte eserler üretmek zorunda kalır.

Bu rekabetin klasik amaç fonksiyonu şöyledir:

$$\min_G \max_D V(D,G)=\mathbb{E}_{x\sim p_{data}}[\log D(x)] + \mathbb{E}_{z\sim p_z}[\log(1-D(G(z)))]$$

Burada $G(z)$ üreticinin gürültüden oluşturduğu örneği, $D(x)$ ise bir örneğin gerçek olma olasılığını gösterir. İdeal dengede ayırt edici artık gerçeği sahteden ayıramaz ve her örnek için yaklaşık $0.5$ sonucu verir.

GAN eğitiminin sadeleştirilmiş PyTorch benzeri akışı şöyledir:

```python
# Önce ayırt edici, gerçek ve sahte örnekleri tanımayı öğrenir.
noise = torch.randn(batch_size, latent_size)
fake_images = generator(noise)

d_loss = discriminator_loss(
    discriminator(real_images),
    discriminator(fake_images.detach())
)
d_loss.backward()
d_optimizer.step()

# Ardından üretici, ayırt ediciyi kandıracak şekilde güncellenir.
g_loss = generator_loss(discriminator(fake_images))
g_loss.backward()
g_optimizer.step()
```

`detach()` kullanımı önemlidir: Ayırt edici eğitilirken gradyanların üreticiye akmasını engeller. Sonraki aşamada ise üretici, ayırt edicinin geri bildiriminden doğrudan yararlanır.

## Difüzyon: Gürültüden düzene yolculuk

Difüzyon modelleri farklı bir oyun oynar. Eğitim sırasında temiz veriye aşamalı olarak Gauss gürültüsü eklenir. İleri süreç yaklaşık olarak şu şekilde ifade edilir:

$$x_t=\sqrt{\bar{\alpha}_t}x_0+\sqrt{1-\bar{\alpha}_t}\epsilon$$

Burada $x_0$ temiz örnek, $x_t$ gürültülü örnek ve $\epsilon$ rastgele gürültüdür. Sinir ağı, belirli bir adımdaki gürültüyü tahmin etmeyi öğrenir. Üretim aşamasında tamamen rastgele bir görüntüden başlanır ve tahmin edilen gürültü defalarca çıkarılır. Bulanık lekeler önce şekillere, ardından ayrıntılı bir görsele dönüşür.

Basitleştirilmiş örnekleme döngüsü şöyledir:

```python
# Üretim tamamen rastgele gürültüyle başlar.
x = torch.randn(image_shape)

for timestep in reversed(range(total_steps)):
    predicted_noise = model(x, timestep)
    x = scheduler.remove_noise(x, predicted_noise, timestep)

# x artık modelin ürettiği temiz örnektir.
```

Gerçek sistemlerde zaman adımı kodlamaları, U-Net mimarileri, dikkat mekanizmaları ve özel gürültü zamanlayıcıları kullanılır. Metin komutları da gömleme vektörlerine çevrilerek üretim sürecini yönlendirebilir.

## GAN mı, difüzyon mu?

| Özellik | GAN | Difüzyon modeli |
|---|---|---|
| Temel mantık | İki ağın rekabeti | Gürültüyü aşamalı temizleme |
| Eğitim kararlılığı | Hassas ve dengesiz olabilir | Genellikle daha kararlı |
| Üretim hızı | Tek geçişle hızlı | Çok sayıda adım nedeniyle yavaş |
| Çeşitlilik | Mod çökmesi yaşayabilir | Veri çeşitliliğini iyi kapsar |
| Görsel kalite | Keskin sonuçlar | Ayrıntılı ve yüksek kaliteli sonuçlar |
| Kontrol edilebilirlik | Ek mimariler gerektirebilir | Metin ve koşullarla güçlü kontrol |

GAN’ler gerçek zamanlı yüz dönüştürme, görüntü iyileştirme ve hızlı sentez için hâlâ değerlidir. Difüzyon modelleri ise metinden görsel, ses ve video üretiminde öne çıkar. Kısacası GAN bir düello, difüzyon ise sabırlı bir restorasyon sürecidir. Hangisinin seçileceği; hız, kalite, donanım maliyeti ve üretim üzerindeki kontrol ihtiyacına bağlıdır.
