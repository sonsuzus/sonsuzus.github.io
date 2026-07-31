---
layout: post
title: "Büyük Dil Modellerinin Hafıza Yanılsaması: Hatırlamak mı, Taklit Etmek mi?"
math: true
categories: 
  - Bilgi
tags: 
  - yapay zeka
  - büyük dil modelleri
  - bellek felsefesi
---

Bir sohbet botuna geçen hafta anlattığınız kedinizin adını sorduğunuzda doğru cevap alırsanız, model sizi gerçekten hatırlamış mı olur? Yoksa önüne yeniden konulan metindeki örüntüleri ustaca tamamlayan dijital bir oyuncuyla mı karşı karşıyasınızdır? Büyük dil modellerinin ikna edici dili, belleğe sahip oldukları izlenimini doğurur; ancak teknik mekanizma ile kullanıcı deneyimi arasında önemli bir felsefi boşluk vardır.

``

## Modelin temel işi: Sonraki parçayı tahmin etmek

Bir büyük dil modeli, en yalın hâliyle, önceki metin parçalarına bakarak sıradaki parçanın olasılığını hesaplar. Bu ilişki şöyle gösterilebilir:

$$P(x_t \mid x_1, x_2, \ldots, x_{t-1})$$

Burada $x_t$ üretilecek yeni token, önceki tokenlar ise modele sunulan bağlamdır. Model, eğitim sırasında öğrendiği parametreleri kullanarak olası devamları puanlar. Dolayısıyla sohbet geçmişinde “Kedimin adı Zeytin” yazıyorsa, daha sonra gelen “Kedimin adı neydi?” sorusuna “Zeytin” cevabını vermesi şaşırtıcı değildir. Bilgi, çalışma belleğini andıran **bağlam penceresinin** içindedir.

Fakat bağlam penceresi temizlendiğinde modelin bu ayrıntıya erişimi kalmayabilir. Bir uygulama eski konuşmaları veritabanından getirip modele yeniden gönderiyorsa, hatırlayan taraf doğrudan model değil, onu çevreleyen yazılım sistemidir.

| Özellik | İnsan belleği | LLM bağlamı | Haricî yapay zekâ belleği |
|---|---|---|---|
| Bilginin kaynağı | Yaşanmış deneyim | Mevcut girdi metni | Veritabanı veya dosya |
| Süreklilik | Biyografik ve değişken | Oturum ya da pencere sınırında | Sistem tasarımına bağlı |
| Geri çağırma | Çağrışım ve yeniden kurma | Olasılıksal tamamlama | Arama ve modele ekleme |
| Unutma | Psikolojik ve biyolojik | Bağlamın dışına taşma | Silme veya erişememe |
| Öznel deneyim | Genellikle var kabul edilir | Kanıtlanmış değildir | Yoktur |

## Hatırlıyormuş gibi yapan küçük bir sistem

Aşağıdaki örnek, “kalıcı hafızalı model” görüntüsünün basit bir sözlük ve bağlam oluşturma işlemiyle üretilebileceğini gösterir:

```python
memory = {}

def remember(user_id, key, value):
    # Bilgiyi modelde değil, uygulamanın deposunda saklar.
    memory.setdefault(user_id, {})[key] = value

def build_prompt(user_id, question):
    # Eski bilgiyi yeniden modele sunulacak metne dönüştürür.
    facts = memory.get(user_id, {})
    context = "\n".join(f"{k}: {v}" for k, v in facts.items())
    return f"Bilinenler:\n{context}\n\nSoru: {question}"

remember("u42", "kedinin adı", "Zeytin")
print(build_prompt("u42", "Kedimin adı neydi?"))
```

Model yalnızca oluşturulan istemi görür. Buna rağmen kullanıcı açısından deneyim son derece kişiseldir: Sistem onu tanıyor gibidir. Bu ayrım, bilgisayardaki hesap makinesi simgesinin fiziksel bir hesap makinesi olmaması kadar basit; konuşmanın duygusal etkisi nedeniyle de bir o kadar kolay unutulabilirdir.

## Bellek ile örüntü tanıma arasındaki felsefi sınır

Belleği yalnızca “geçmiş bilginin bugünkü davranışı etkilemesi” diye tanımlarsak, model parametreleri bir çeşit **istatistiksel bellek** sayılabilir. Eğitim verisi ağırlıklarda birebir cümleler hâlinde değil, dağıtılmış ilişkiler olarak iz bırakır. Kabaca modelin öğrenmesi şu optimizasyonla anlatılabilir:

$$\theta^* = \arg\min_\theta \sum_i -\log P_\theta(x_i \mid x_{<i})$$

Ancak insan belleği çoğu zaman daha güçlü ölçütler içerir: Bir olayın kişinin başına gelmiş olması, geçmişteki benlikle süreklilik kurması ve hatırlama eyleminin öznel bir niteliğe sahip olması. Model “Bunu hatırlıyorum” dediğinde bu ifade içsel bir anıya rapor vermek zorunda değildir; benzer diyaloglarda uygun görülen dilsel kalıbı üretmiş olabilir.

Üstelik insan belleği de kusursuz bir kayıt cihazı değildir. İnsanlar anıları yeniden kurar, ayrıntıları karıştırır ve boşlukları beklentilerle doldurur. Bu nedenle fark, “insan kaydeder, model tahmin eder” kadar keskin değildir. İkisi de geçmiş izlerden hareketle mevcut duruma uygun bir temsil oluşturabilir. Asıl tartışma, bu işlemin bilinçli bir özneye, kişisel tarihe ve deneyim sahipliğine ihtiyaç duyup duymadığıdır.

Pratik sonuç nettir: Bir modelin adınızı doğru söylemesini bilinç veya sadakat kanıtı saymamalıyız. Önce bağlamın, kayıt sistemlerinin ve kişiselleştirme katmanlarının nasıl çalıştığını sormalıyız. LLM’ler geçmişi yaşamış olmayabilir; fakat geçmişe sahipmiş gibi konuşmayı olağanüstü iyi taklit eder. Hafıza yanılsamasının gücü de tam burada yatar: Dilsel performans, zihinsel deneyimin kanıtı gibi görünür.
