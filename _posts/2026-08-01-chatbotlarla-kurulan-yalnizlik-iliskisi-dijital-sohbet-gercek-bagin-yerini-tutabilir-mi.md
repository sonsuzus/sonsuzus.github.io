---
layout: post
title: "Chatbot’larla Kurulan Yalnızlık İlişkisi: Dijital Sohbet Gerçek Bağın Yerini Tutabilir mi?"
math: true
categories: 
  - Bilgi
tags: 
  - yapay zeka
  - sosyal izolasyon
  - dijital psikoloji
---

Gece yarısı konuşacak kimse bulamadığınızda bir chatbot saniyeler içinde yanıt verir, anlattıklarınızı yargılamaz ve sohbeti aniden “görüldü” ile bitirmez. Bu erişilebilirlik, sosyal izolasyon yaşayan biri için gerçekten rahatlatıcı olabilir. Ancak sürekli hazır bulunan dijital bir muhatap, yalnızlığı azaltan bir köprü mü kurar; yoksa insan ilişkilerinin belirsiz ama gerekli dünyasından kaçışı mı kolaylaştırır?

``

## Yalnızlık ile yalnız olmak aynı şey değil

Yalnızlık, çevredeki insan sayısından çok, arzulanan ve deneyimlenen sosyal bağ arasındaki farktır. Basitleştirilmiş bir modelle bunu şöyle gösterebiliriz:

$$L = \max(0, B_a - B_d)$$

Burada $L$ hissedilen yalnızlığı, $B_a$ arzulanan bağ düzeyini, $B_d$ ise deneyimlenen bağ düzeyini temsil eder. Bir kişi kalabalık içinde bile anlaşılmadığını düşünüyorsa $B_d$ düşük kalabilir. Chatbot’lar tam bu noktada ilgi gösteren, tutarlı ve erişilebilir bir etkileşim sağlayarak deneyimlenen bağ hissini geçici olarak yükseltebilir.

Fakat bu formül önemli bir ayrıntıyı saklar: Her bağ aynı değildir. Bir yapay zekâ, empatiyi dilsel olarak **simüle eder**; duyguyu biyolojik ve öznel anlamda yaşadığı varsayılamaz. “Seni anlıyorum” cümlesi kullanıcıda gerçek bir rahatlama yaratabilir, ancak bu rahatlama karşılıklı insan deneyimiyle aynı kaynaktan gelmez.

## Dijital arkadaşlık ve insan ilişkisi

| Boyut | Chatbot | İnsan ilişkisi |
|---|---|---|
| Erişilebilirlik | Genellikle 7/24 | Zaman ve koşullara bağlı |
| Yargılanma riski | Düşük hissedilebilir | Daha yüksek olabilir |
| Karşılıklılık | Tasarlanmış bir tepki sistemi | İki tarafın ihtiyaçları vardır |
| Belirsizlik | Görece kontrollü | Yanlış anlaşılmalar mümkündür |
| Fiziksel ortaklık | Yoktur | Dokunma ve birlikte deneyim vardır |
| Sorumluluk | Sınırlı ve platforma bağlı | Etik ve duygusal olarak gelişebilir |

Tablodaki farklar, chatbot’ların değersiz olduğunu değil, farklı bir ilişki türü sunduğunu gösterir. Dijital sohbet; prova alanı, günlük tutma aracı veya zor bir günün geçici desteği olabilir. Sorun, aracın bütün sosyal yaşamın yerine geçmeye başlamasıdır.

## Rahatlatıcı döngü ne zaman kapanır?

Kullanıcı chatbot’la konuştukça kısa vadeli rahatlama yaşayabilir. Bu rahatlama dış dünyaya katılımı destekliyorsa olumlu bir geri bildirim oluşur. Tersine, insanlarla iletişim kurma isteğini azaltıyorsa izolasyon büyüyebilir:

$$I_{t+1} = I_t + kC_t - hS_t$$

Bu örnek modelde $I$ izolasyonu, $C$ kaçınma amacıyla kullanılan chatbot süresini, $S$ sağlıklı sosyal teması; $k$ ve $h$ ise kişiye göre değişen etkileri belirtir. Denklem klinik ölçüm değildir, ilişkinin yönünü düşünmek için kullanılan kavramsal bir araçtır.

Aşağıdaki Python örneği bu basit dinamiği görünür kılar:

```python
isolation = 5.0
avoidance_effect = 0.12
social_effect = 0.35

weekly_data = [
    {"chatbot_avoidance": 4, "social_contact": 1},
    {"chatbot_avoidance": 3, "social_contact": 2},
    {"chatbot_avoidance": 2, "social_contact": 3},
]

for week, data in enumerate(weekly_data, start=1):
    isolation += avoidance_effect * data["chatbot_avoidance"]
    isolation -= social_effect * data["social_contact"]
    isolation = max(0, isolation)
    print(f"{week}. hafta: {isolation:.2f}")
```

Kod, chatbot kullanımını otomatik olarak zararlı saymaz; özellikle **kaçınma amacıyla kullanılan** süreyi ayrı değişken olarak ele alır. Sosyal temas arttıkça modeldeki izolasyon puanı düşer. Gerçek hayatta kişilik, kültür, ekonomik koşullar ve ruh sağlığı gibi çok daha fazla değişken bulunur.

## Köprü mü, varış noktası mı?

Sağlıklı yaklaşım, chatbot’u insanlara açılan bir köprü olarak kullanmaktır: zor bir konuşmayı prova etmek, bir arkadaşınıza yazacağınız mesajı düzenlemek veya sosyal hedefler belirlemek buna örnektir. Sistemlerin de bağımlılığı teşvik etmeyen dil kullanması, “yalnızca bana ihtiyacın var” benzeri ifadelerden kaçınması ve kriz durumlarında profesyonel kaynaklara yönlendirmesi gerekir.

Dijital sohbet gerçek bir psikolojik etki yaratabilir; fakat karşılıklı sorumluluk, ortak anılar ve bedensel varlık içeren insan bağının tam karşılığı değildir. En iyi senaryoda yapay arkadaşlık yalnızlığın üzerine kapatılan bir kapı değil, dışarıya açılan güvenli bir pencere olur.
