---
layout: post
title: "Makine Çevirisinin Kültürel Bedeli: Sözcükler Geçerken Dünya Görüşü Geride mi Kalıyor?"
math: true
categories: 
  - Bilgi
tags: 
  - makine çevirisi
  - dilsel görecelik
  - yapay zekâ
---

Bir çeviri uygulamasına birkaç sözcük yazıp saniyeler içinde başka bir dilde karşılığını almak neredeyse sihir gibi görünüyor. Ancak dil yalnızca bilgi taşıyan nötr bir boru değildir; hitap biçimleri, toplumsal ilişkiler, tarihsel çağrışımlar ve dünyayı sınıflandırma alışkanlıkları da sözcüklerin içinde yolculuk eder. Makine çevirisi anlamı aktarırken bu görünmez yükün bir bölümünü peronda bırakabilir.

``

## Dil, düşüncenin yalnızca ambalajı mı?

Sapir-Whorf hipoteziyle ilişkilendirilen **dilsel görecelik**, konuştuğumuz dilin dünyayı algılama ve kategorilere ayırma biçimimizi etkilediğini savunur. Kuramın güçlü yorumu dilin düşünceyi belirlediğini, daha ılımlı ve günümüzde daha fazla kabul gören yorumu ise bazı düşünme alışkanlıklarını yönlendirdiğini söyler.

Örneğin Türkçedeki “o” zamiri konuşulan kişinin cinsiyetini belirtmez. İngilizceye çeviri yapan bir model ise bağlama göre “he”, “she” veya “they” seçmek zorundadır. Kaynak dilin açık bırakabildiği bir özellik, hedef dilde karara dönüşür. Model yalnızca çeviri yapmaz; belirsizliği yorumlar.

| Dilsel özellik | Kaynak dildeki işlev | Çeviride oluşabilecek kayıp |
|---|---|---|
| Saygı hitapları | Yaş ve statüyü gösterir | İlişki sıradanlaşabilir |
| Cinsiyetsiz zamir | Kimliği belirsiz bırakır | Modele ait varsayım eklenebilir |
| Deyim ve atasözü | Ortak kültürel hafıza taşır | Düz, açıklayıcı cümleye dönüşebilir |
| Kanıtsallık ekleri | Bilginin kaynağını belirtir | Kesinlik derecesi değişebilir |

## Modeller “en doğruyu” nasıl seçiyor?

Modern çeviri sistemleri, bir hedef cümlenin kaynak cümle verildiğinde ne kadar olası olduğunu hesaplar. Basitleştirilmiş amaç şöyle yazılabilir:

$$\hat{y}=\arg\max_y P(y\mid x)$$

Burada $x$ kaynak metin, $y$ hedef metindir. Sorun şudur: En olası çeviri, kültürel açıdan en sadık çeviri olmak zorunda değildir. Eğitim verilerinde sık görülen kalıplar yüksek olasılık kazanır; az temsil edilen lehçeler, yerel benzetmeler veya toplumsal nezaket biçimleri ise istatistiksel gürültü gibi değerlendirilebilir.

Kayıp yalnızca sözcük düzeyinde ölçülemez. Kavramsal olarak kültürel maliyeti şöyle düşünebiliriz:

$$C=\alpha L_s+\beta L_p+\gamma L_c$$

$L_s$ anlamsal kaybı, $L_p$ pragmatik yani bağlamsal kaybı, $L_c$ kültürel çağrışım kaybını temsil eder. Geleneksel otomatik ölçütler çoğunlukla ilk bileşene odaklanırken diğer ikisini yakalamakta zorlanır.

## Küçük bir belirsizlik deneyi

Aşağıdaki Python kodu, tek bir çeviri yerine adayların puanlarını incelemenin neden önemli olduğunu gösteren basitleştirilmiş bir örnektir:

```python
adaylar = {
    "He said he would come.": 0.46,
    "She said she would come.": 0.41,
    "They said they would come.": 0.13
}

sirali = sorted(adaylar.items(), key=lambda x: x[1], reverse=True)

for ceviri, olasilik in sirali:
    print(f"{olasilik:.0%} — {ceviri}")
```

Kaynak cümle “O geleceğini söyledi” ise ilk iki aday arasındaki küçük fark, modelin gerçek bilgiye sahip olduğunu göstermez. Bu fark; eğitim verilerindeki meslek, isim veya toplumsal cinsiyet dağılımlarından kaynaklanabilir. Sistem kendinden emin bir cümle üretirken aslında kültürel bir tahminde bulunmaktadır.

## Daha duyarlı çeviri mümkün mü?

Çözüm, makineleri terk etmek değil; başarı tanımını genişletmektir. Modeller bağlam sormalı, belirsizlikleri işaretlemeli ve birden fazla çeviri önermelidir. Değerlendirme ekiplerinde yerel konuşurlar, çevirmenler ve kültür araştırmacıları bulunmalıdır. Ayrıca “akıcı” görünen her çıktının sadık olmadığı unutulmamalıdır.

Makine çevirisi diller arasındaki mesafeyi olağanüstü biçimde azaltıyor. Yine de hızın bedeli, farklı düşünme biçimlerinin tek ve pürüzsüz bir ifadeye sıkıştırılması olabilir. İyi bir çeviri yalnızca “Bu cümle ne diyor?” sorusunu değil, “Bu dil dünyayı neden böyle söylüyor?” sorusunu da koruyabilmelidir.
