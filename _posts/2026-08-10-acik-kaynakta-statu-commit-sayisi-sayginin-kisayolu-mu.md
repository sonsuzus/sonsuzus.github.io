---
layout: post
title: "Açık Kaynakta Statü: Commit Sayısı Saygının Kısayolu mu?"
math: true
categories: 
  - Bilgi
tags: 
  - açık kaynak
  - meritokrasi
  - yazılım toplulukları
  - sosyoloji
---

Açık kaynak dünyası ilk bakışta çekici bir vaatte bulunur: Kodun iyiyse, katkın görünürse ve problemi çözüyorsan saygıyı hak edersin. Bu anlatı, unvanlardan çok emeğin konuştuğu bir meritokrasi hayali kurar. Fakat bir depodaki commit sayısı, bir kişinin topluluk içindeki etkisini veya saygınlığını gerçekten ölçer mi? Sosyolojik açıdan yanıt, rahatsız edici derecede karmaşıktır.

``

Meritokrasi, ödül ve statünün bireysel yetenek ile çabaya göre dağıtılması fikridir. Açık kaynakta bu fikir genellikle GitHub sinyalleriyle somutlaşır: commit, pull request, yıldız, takipçi, issue yanıtı ve review. Basitleştirilmiş bir algı modeli şöyle yazılabilir:

$$S = \alpha C + \beta Q + \gamma V + \delta R$$

Burada $S$ algılanan statü; $C$ katkı miktarı, $Q$ katkının kalitesi, $V$ görünürlük ve $R$ ilişkisel sermayedir. Meritokrasi anlatısı $\alpha$ ve $\beta$ katsayılarını öne çıkarır. Pratikte ise özellikle büyük projelerde $V$ ve $R$ çoğu zaman beklenenden daha belirleyicidir.

| Sinyal | Ne ölçüyor gibi görünür? | Gerçekte kaçırabileceği şey |
|---|---|---|
| Commit sayısı | Süreklilik ve emek | Küçük değişiklikler, squash stratejileri, bakım emeği |
| Pull request | Teknik üretkenlik | PR inceleme, mentorluk, topluluk arabuluculuğu |
| Takipçi/yıldız | Tanınırlık | Popülerlik döngüsü ve platform görünürlüğü |
| Maintainer yetkisi | Güven ve uzmanlık | Tarihsel yakınlık, erişim ve karar gücü |

Örneğin tek satırlık bir belge düzeltmesi teknik olarak commit sayısını artırır; ancak erişilebilirlik denetimi yapan, yeni katılımcıya sabırla rehberlik eden veya zehirli bir tartışmayı yatıştıran kişi çoğu zaman daha az görünür iz bırakır. Buna **görünmez emek** denir. Topluluğun sürdürülebilirliği için kritik olan bu faaliyetler, Git geçmişinde kolayca sayılmaz.

Statü ayrıca yalnızca üretilmez, tanınır. Pierre Bourdieu'nün sermaye yaklaşımı burada kullanışlıdır: Teknik beceri bir tür kültürel sermayeyken, tanınmış geliştiricilerle ilişki kurmak sosyal sermayedir. Konferanslarda konuşmak, doğru kanallarda görünmek ve proje tarihinin erken döneminde yer almak ise sembolik sermayeye dönüşebilir. Dolayısıyla iki geliştirici aynı kalitede yama yazsa bile, yamalarının gördüğü ilgi eşit olmayabilir.

Aşağıdaki küçük örnek, niceliksel metriğin neden tek başına zayıf olduğunu anlatır:

```python
contributors = [
    {"ad": "Deniz", "commit": 80, "review": 3, "mentorluk": 0},
    {"ad": "Ece", "commit": 12, "review": 45, "mentorluk": 18},
]

for kisi in contributors:
    skor = kisi["commit"] + 2 * kisi["review"] + 3 * kisi["mentorluk"]
    print(kisi["ad"], skor)
```

Bu kod teknik bir “gerçek statü” hesabı değildir; yalnızca ağırlıkların politik olduğunu gösterir. Review için neden $2$, mentorluk için neden $3$ verildi? Bu kararı kim alıyor? Bir topluluğun değerleri, tam da bu katsayılarda saklıdır.

| Yaklaşım | Avantajı | Riski |
|---|---|---|
| Salt katkı sayısı | Ölçmesi kolaydır | Oyunlaştırılabilir ve dar görüşlüdür |
| Teknik kalite odaklı değerlendirme | Mühendislik standardını korur | Bakım ve iletişim emeğini dışlayabilir |
| Çok boyutlu katkı modeli | Daha adil bir tablo sunar | Değerlendirmesi zaman ve özen ister |

Sağlıklı bir açık kaynak topluluğu, commit sayılarını tamamen çöpe atmak zorunda değildir. Ancak onları statünün nihai kanıtı değil, bağlam isteyen bir sinyal olarak görmelidir. İyi bir proje; kod yazmayı, hata raporlamayı, inceleme yapmayı, dokümantasyonu, çeviriyi ve nazik iletişimi birlikte ödüllendirir. Gerçek meritokrasi, en çok görünenin değil, topluluğu gerçekten ileri taşıyan emeğin tanınmasıyla başlar.
