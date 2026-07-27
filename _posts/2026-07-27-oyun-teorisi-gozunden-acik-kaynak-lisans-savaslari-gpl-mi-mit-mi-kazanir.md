---
layout: post
title: "Oyun Teorisi Gözünden Açık Kaynak Lisans Savaşları: GPL mi MIT mi Kazanır?"
math: true
categories: 
  - Bilgi
tags: 
  - oyun teorisi
  - açık kaynak
  - yazılım lisansları
---

Bir açık kaynak lisansı seçmek, yalnızca hukuk metinleri arasında tercih yapmak değildir; geliştiriciler, şirketler ve kullanıcılar arasında oynanan uzun vadeli bir strateji oyununa katılmaktır. MIT özgürlüğü en az koşulla dağıtırken GPL, bu özgürlüğün sonraki sürümlerde de korunmasını ister. Peki rasyonel aktörlerin bulunduğu bir ekosistemde hangi yaklaşım kazanır?
``
## Oyuncular, stratejiler ve kazançlar

Basitleştirilmiş modelimizde üç aktör bulunsun:

- **Bağımsız geliştirici:** Kodun yayılmasını, itibar ve katkı kazanmayı hedefler.
- **Şirket:** Geliştirme maliyetini düşürmek ve rekabet avantajı elde etmek ister.
- **Topluluk:** İyileştirmelerin ortak havuza dönmesini ve projenin yaşamasını önemser.

Her aktörün faydasını kabaca şöyle gösterebiliriz:

$$U_i = \alpha A + \beta C + \gamma R - \delta K$$

Burada $A$ benimsenme oranını, $C$ topluluğa dönen katkıyı, $R$ rekabet avantajını ve $K$ uyumluluk maliyetini temsil eder. Katsayılar aktöre göre değişir. Bir girişim için $R$ yüksek ağırlık taşırken topluluk odaklı geliştiricide $C$ daha önemlidir.

| Ölçüt | MIT | GPL |
|---|---|---|
| Ticari benimsenme | Genellikle çok kolay | Dağıtım modeline bağlı |
| Değişiklikleri kapatma | Mümkün | Türetilmiş çalışmalarda sınırlı |
| Katkının geri dönmesi | Gönüllülüğe bağlı | Lisansla teşvik edilir |
| Uyumluluk maliyeti | Düşük | Daha yüksek |
| Ekosistem etkisi | Hızlı yayılma | Ortak havuzu koruma |

## Tekrarlanan oyun neden önemli?

Oyun yalnızca bir kez oynansaydı şirket, MIT kodunu alıp kapalı bir ürüne dönüştürerek yüksek kısa vadeli kazanç sağlayabilirdi. Geliştirici de daha geniş benimsenme elde ederdi. Bu senaryoda MIT güçlü görünür.

Açık kaynak ekosistemleri ise **tekrarlanan oyunlardır**. Aynı şirketler ve geliştiriciler yıllarca karşılaşır. Bugün katkıyı saklayan aktör yarın kötü itibar, zayıf topluluk ve daha yüksek bakım maliyetiyle karşılaşabilir. Gelecekteki kazançların bugünkü değeri şu seriyle modellenebilir:

$$V = u_0 + \delta u_1 + \delta^2 u_2 + \cdots$$

$\delta$ geleceğe verilen önemi gösterir. $\delta$ yüksekse iş birliği rasyonelleşir. GPL, iş birliğini yalnızca iyi niyete bırakmayıp oyunun kurallarına yerleştirir. MIT ise güven, itibar ve ağ etkisine daha fazla yaslanır.

## Basit bir kazanç matrisi

Şirketin “katkıyı paylaş” veya “kodu kapat” stratejilerinden birini seçtiğini düşünelim. Değerler kesin sonuçlar değil, teşvikleri görünür kılan örnek puanlardır.

| Lisans ve strateji | Şirket kazancı | Topluluk kazancı |
|---|---:|---:|
| MIT + paylaş | 7 | 8 |
| MIT + kapat | 9 | 3 |
| GPL + paylaş | 6 | 9 |
| GPL + kapatmaya çalışma | 2 | 4 |

MIT altında şirket için kapatma stratejisi kısa vadede baskın olabilir. GPL ise bu seçeneğin maliyetini artırarak dengeyi paylaşmaya yaklaştırır. Buna karşılık ağır uyumluluk gereksinimleri bazı şirketlerin oyuna hiç girmemesine yol açabilir.

## Modeli kodla deneyelim

Aşağıdaki Python örneği, geleceğe verilen önem değiştikçe paylaşmanın toplam değerini karşılaştırır:

```python
def uzun_vadeli_kazanc(anlik_kazanc, delta, tur=20):
    # Tekrarlanan oyundaki indirgenmiş toplam faydayı hesaplar.
    return sum((delta ** t) * anlik_kazanc for t in range(tur))

for delta in (0.3, 0.7, 0.95):
    paylas = uzun_vadeli_kazanc(7, delta)
    kapat = 9 + uzun_vadeli_kazanc(3, delta, tur=19)
    print(delta, round(paylas, 2), round(kapat, 2))
```

Burada kapatma ilk turda yüksek, sonraki turlarda düşük kazanç üretir; çünkü topluluk güveninin azaldığını varsayıyoruz. `delta` yükseldikçe sürdürülebilir iş birliğinin değeri belirginleşir.

## Öyleyse kim kazanır?

Tek bir evrensel galip yoktur. Amaç **maksimum yayılma, düşük sürtünme ve geniş entegrasyon** ise MIT çoğu zaman avantajlıdır. Amaç **iyileştirmelerin ortak havuzda kalması ve özel mülke dönüşmenin sınırlandırılması** ise GPL daha güçlü bir mekanizma tasarlar.

Oyun teorisinin cevabı şudur: Lisans, oyuncunun kişiliğini değiştirmez; kazanç tablosunu değiştirir. MIT “daha çok oyuncu gelsin” derken GPL “gelen oyuncu ortak masayı büyütsün” der. Kazanan, projenizin hangi oyunu oynamak istediğine bağlıdır.
