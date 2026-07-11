---
layout: post
title: "Turing Testi ve Yapay Zekanın Psikolojisi: Kod Ne Zaman İnsan Gibi Konuşur?"
math: true
categories: 
  - Bilgi
tags: 
  - turing-testi
  - yapay-zeka
  - doğal-dil-işleme
---

Bir sohbet botu size doğru cevabı verdiğinde etkilenirsiniz; ama size duraksayarak, şaka yaparak, konuyu hafifçe yanlış anlayıp sonra toparlayarak cevap verdiğinde ona neredeyse kişilik atfedersiniz. Turing Testi tam da bu bulanık bölgede yaşar: Mesele yalnızca kodun mantıklı çıktı üretmesi değil, insan bilişini, dil alışkanlıklarını ve sohbetin sosyal ritmini ne kadar inandırıcı taklit edebildiğidir.
``

Alan Turing’in 1950’de önerdiği ünlü “taklit oyunu”, bir makinenin düşünüp düşünmediğini doğrudan sormak yerine daha pratik bir soru sorar: Bir insan değerlendirici, yazılı sohbet üzerinden makineyi insandan ayırt edemezse, makine zeki davranış sergiliyor sayılabilir mi? Bu yaklaşım zekâyı içsel bir özden çok gözlemlenebilir davranış üzerinden ele alır. Yani test, beynin içinde ne olduğunu değil, konuşmanın karşı tarafta nasıl bir izlenim bıraktığını ölçer.

Burada psikoloji devreye girer. İnsan iletişimi yalnızca bilgi aktarımı değildir; niyet, bağlam, bellek, duygu tonu ve beklenti yönetimi içerir. Bir kullanıcı “Bugün berbat geçti” dediğinde iyi bir sistem sadece “Üzgünüm” dememeli; cümlenin duygusal ağırlığını, devam sorusu ihtiyacını ve fazla mekanik görünmeme riskini de hesaba katmalıdır. Bu yüzden modern yapay zekâ sistemlerinde dil modeli kadar “sohbet dinamiği modeli” de önemlidir.

Basitçe ifade edersek, bir cevap üretme sistemi şu olasılığı büyütmeye çalışır: $P(cevap | bağlam)$. Ancak Turing benzeri inandırıcılık için hedef biraz daha karmaşıktır: $S = αT + βD + γB$. Burada $T$ tutarlılığı, $D$ duygusal uygunluğu, $B$ bağlama bağlılığı temsil eder. Katsayılar, sistemin hangi özelliğe daha çok önem vereceğini belirler.

| Boyut | Mantıksal Bot | İnsan Benzeri Bot |
|---|---|---|
| Cevap amacı | Doğru bilgi vermek | Doğru ve sosyal olarak uygun tepki vermek |
| Hata davranışı | Hatasını gizler veya tekrarlar | Belirsizliği kabul eder, düzeltme ister |
| Dil yapısı | Düz ve kalıplı | Vurgu, bağlaç, küçük sapmalar içerir |
| Bellek kullanımı | Son mesaja odaklanır | Önceki niyetleri ve ilişki tonunu taşır |

Böyle sistemler geliştirmek için önce konuşmayı parçalara ayırmak gerekir. Niyet tanıma, duygu analizi, bağlam takibi ve cevap üretimi ayrı katmanlar gibi düşünülebilir. Aşağıdaki küçük Python örneği, oyuncak seviyesinde bir sohbet değerlendiricisi kurar. Amaç, cevabın yalnızca anahtar kelimeye değil, duygu tonuna da tepki vermesidir.

```python
class MiniTuringBot:
    def __init__(self):
        self.memory = []

    def detect_emotion(self, text):
        sad_words = ['kötü', 'berbat', 'üzgün', 'yoruldum']
        happy_words = ['harika', 'güzel', 'sevindim', 'başardım']
        if any(word in text.lower() for word in sad_words):
            return 'sad'
        if any(word in text.lower() for word in happy_words):
            return 'happy'
        return 'neutral'

    def reply(self, user_text):
        emotion = self.detect_emotion(user_text)
        self.memory.append(user_text)

        if emotion == 'sad':
            return 'Bunu yaşaman zor olmalı. İstersen ne olduğunu birlikte açabiliriz.'
        if emotion == 'happy':
            return 'Bu güzel haber! Sence bunu mümkün kılan en önemli şey neydi?'
        return 'Anladım. Biraz daha detay verirsen daha iyi takip edebilirim.'

bot = MiniTuringBot()
print(bot.reply('Bugün gerçekten berbat geçti'))
```

Bu kod “zeki” değildir; fakat önemli bir fikri gösterir: İnsan benzeri sohbet, tek seferlik cevaplardan değil, durum değerlendirmesinden oluşur. Gerçek sistemlerde bu yapı büyük dil modelleri, vektör veritabanları, kullanıcı profilleri ve güvenlik filtreleriyle genişletilir. Yine de temel soru değişmez: Cevap, karşıdaki kişinin zihinsel durumuna uygun mu?

| Değerlendirme Kriteri | Örnek Soru | Risk |
|---|---|---|
| Tutarlılık | Bot önceki cevabıyla çelişiyor mu? | Güven kaybı |
| Doğallık | Cümleler fazla kusursuz mu? | Robotik izlenim |
| Empati | Duyguya uygun tepki var mı? | Soğuk iletişim |
| Şeffaflık | Bilmediğini söyleyebiliyor mu? | Halüsinasyon |

Turing Testi’nin en eğlenceli tarafı, bizi “zeka nedir?” sorusundan “zeki görünmek ne demektir?” sorusuna taşır. Bu ikisi aynı şey değildir. Bir sistem insanı kandırabilir ama gerçekten anlamıyor olabilir; yine de pratik yazılım geliştirmede kullanıcı deneyimi açısından bu inandırıcılık değerlidir. Özellikle eğitim, müşteri desteği, terapi destek araçları ve oyun karakterlerinde dilin psikolojik dokusu kritik hale gelir.

Sonuç olarak Turing Testi, yapay zekâ geliştiricilerine hâlâ güçlü bir pusula sunar. Daha iyi modeller kurmak istiyorsanız sadece algoritmaya değil, insanın konuşurken yaptığı küçük bilişsel numaralara da bakın: ima, tereddüt, bağlam, duygu ve hatırlama. Çünkü bazen bir botu inandırıcı yapan şey en doğru cevabı vermesi değil, doğru anda “hmm, bunu biraz açalım” diyebilmesidir.
