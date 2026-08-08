---
layout: post
title: "Büyük Dil Modelleri ve İstem Mühendisliği: Yapay Zekâya Doğru Soruyu Sormak"
math: true
categories: 
  - Bilgi
tags: 
  - LLM
  - İstem Mühendisliği
  - Fine-Tuning
---

Bir büyük dil modeliyle sohbet etmek bazen her şeyi bilen bir kütüphaneciyle, bazen de özgüveni bilgisinden yüksek bir stajyerle konuşmaya benzer. Sonuçların arasındaki bu fark yalnızca modelin büyüklüğünden değil; eğitim verisinden, ince ayar yönteminden, bağlam penceresinden ve yazdığımız istemin kalitesinden doğar. Milyarlarca parametre etkileyici görünse de modeli gerçekten kullanışlı yapan şey, bu dev matematik makinesinin nasıl yönlendirildiğini anlamaktır.

``

## LLM aslında ne yapar?

Büyük Dil Modelleri, metni insanlar gibi “anlamaya” çalışmaktan önce sıradaki parçayı tahmin eder. Metin, **token** adı verilen kelime, hece veya karakter parçalarına ayrılır. Model, önceki token’ları kullanarak bir sonraki token’ın olasılık dağılımını hesaplar:

$$P(w_t \mid w_1, w_2, ..., w_{t-1})$$

Örneğin “Bugün hava çok” ifadesinden sonra “güzel” token’ına yüksek olasılık verilebilir. Bu işlem art arda tekrarlandığında paragraflar, kodlar ve hatta şiirler ortaya çıkar. Yani sihirli görünen sohbet, temelde olağanüstü gelişmiş bir otomatik tamamlama sürecidir.

Modelin parametreleri, sinir ağındaki öğrenilebilir sayısal ağırlıklardır. Eğitim sırasında tahmin ile gerçek token arasındaki hata ölçülür. Yaygın kayıp fonksiyonu kabaca şöyledir:

$$L = - \sum_t \log P(w_t \mid w_{<t})$$

Geri yayılım ve gradyan inişi, bu kaybı azaltacak biçimde milyarlarca ağırlığı günceller. Transformer mimarisindeki **attention** mekanizması ise cümlenin hangi parçalarının birbirleriyle ilişkili olduğunu belirler. Böylece model, uzak kelimeler arasındaki bağlantıları yakalayabilir.

## Ön eğitim, ince ayar ve RAG farkı

Her problemi modele yeniden ezberletmek gerekmez. İhtiyaca göre farklı uyarlama yöntemleri kullanılabilir:

| Yöntem | Ne değişir? | Güçlü yanı | Uygun senaryo |
|---|---|---|---|
| Ön eğitim | Tüm model ağırlıkları | Genel dil yeteneği kazandırır | Temel model geliştirme |
| Fine-tuning | Ağırlıkların tümü veya bir kısmı | Davranışı kalıcı biçimde özelleştirir | Sınıflandırma, kurum dili |
| RAG | Model yerine bağlam zenginleşir | Güncel ve kaynaklı bilgi sağlar | Doküman arama, destek botu |
| Prompting | Yalnızca giriş metni | Hızlı ve düşük maliyetlidir | Günlük görevler, prototipler |

Fine-tuning sürecinde kaliteli giriş-çıkış örnekleri hazırlanır. Ardından düşük öğrenme oranıyla eğitim yapılır ve model daha önce görmediği doğrulama verisiyle sınanır. Veri azsa LoRA gibi parametre-verimli yöntemler tercih edilebilir. LoRA, dev modelin tamamını değiştirmek yerine küçük ek matrisler öğrenerek maliyeti düşürür.

## İyi bir istem nasıl yazılır?

“Bana yazılımı anlat” istemi belirsizdir. Model hedef kitleyi, kapsamı ve çıktı biçimini tahmin etmek zorunda kalır. Sağlam bir istem genellikle dört bileşen içerir:

1. **Rol:** Modelin hangi uzman gibi davranacağı.
2. **Görev:** Tam olarak ne üretileceği.
3. **Bağlam:** Kullanılacak bilgi ve sınırlamalar.
4. **Çıktı biçimi:** Tablo, JSON, liste veya kod gibi format.

Örneğin API üzerinden yapılandırılmış bir istem şöyle hazırlanabilir:

```python
prompt = """
Rolün: Kıdemli Python geliştiricisi.
Görev: Aşağıdaki fonksiyondaki performans sorunlarını bul.
Kısıtlar: Davranışı değiştirme, en fazla üç öneri sun.
Çıktı: Sorun, neden ve düzeltilmiş kod başlıklarını kullan.
Kod:
{code}
"""

response = client.responses.create(
    model="uygun-model",
    input=prompt.format(code=source_code)
)
```

Bu kod, modele yalnızca soru sormaz; rol, sınır ve beklenen yapıyı da bildirir. Üretim ortamında kullanıcı verisi doğrudan isteme ekleniyorsa prompt injection saldırılarına karşı doğrulama ve yetkilendirme uygulanmalıdır.

## Daha güvenilir sonuçlar için küçük taktikler

Karmaşık işleri tek seferde istemek yerine görevi aşamalara bölmek başarıyı artırır. Birkaç kaliteli örnek vermek **few-shot prompting**, hiç örnek vermeden açık talimat kullanmak ise **zero-shot prompting** olarak adlandırılır. Modelden bilinmeyen noktaları belirtmesini, varsayımlarını listelemesini ve mümkünse kaynak göstermesini istemek de halüsinasyon riskini azaltır.

Sonuç olarak LLM, niyet okuyan bir kahin değil; bağlamdan olasılık üreten güçlü bir sistemdir. Fine-tuning davranışı uzmanlaştırır, RAG güncel bilgiyi taşır, iyi prompting ise tüm bu kapasitenin doğru kapıya yönelmesini sağlar. Yapay zekâ çağında yalnızca cevabı bilmek değil, doğru soruyu tasarlamak da temel bir mühendislik becerisidir.
