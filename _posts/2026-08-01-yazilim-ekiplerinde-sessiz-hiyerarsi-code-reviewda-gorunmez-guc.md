---
layout: post
title: "Yazılım Ekiplerinde Sessiz Hiyerarşi: Code Review’da Görünmez Güç"
math: true
categories: 
  - Bilgi
tags: 
  - code-review
  - yazılım-kültürü
  - ekip-dinamikleri
---

Bir pull request açılır, değişiklikler yüzlerce satırdır ve kıdemli geliştiricinin kodu birkaç dakika içinde “LGTM” alır. Aynı ekipte yeni başlayan birinin üç satırlık düzeltmesi ise isimlendirmeden mimariye kadar didiklenir. Bu fark yalnızca teknik deneyimle açıklanabilir mi? Code review, hataları yakalayan bir mühendislik pratiği olduğu kadar statü, güven ve otoritenin yeniden üretildiği küçük bir sosyal sahnedir.

``

## Code review gerçekten yalnızca kodu mu inceler?

İdeal modelde incelemenin nesnesi kişiden bağımsız olarak değişikliktir. Reviewer; doğruluk, güvenlik, okunabilirlik ve bakım maliyetini değerlendirir. Fakat gerçek ekiplerde yorumun ağırlığı, kodun niteliği kadar onu yazanın konumundan da etkilenebilir.

Sosyolojide **statü genellemesi**, bir alandaki itibarın başka alanlardaki kararları da etkilemesini anlatır. Örneğin güçlü mimari bilgisiyle tanınan bir geliştiricinin frontend değişiklikleri de daha az sorgulanabilir. Böylece geçmiş başarı, bugünkü kod için görünmez bir güven kredisine dönüşür.

Bu ilişkiyi basitleştirilmiş biçimde şöyle düşünebiliriz:

$$S = \frac{Q_r}{L_c + 1}$$

Burada $Q_r$, review sırasında sorulan anlamlı soru sayısını; $L_c$ ise kod sahibinin ekip içindeki algılanan otorite seviyesini temsil etsin. $S$ değeri küçüldükçe sorgulama yoğunluğu azalır. Elbette insan ilişkileri tek formülle açıklanamaz; denklem yalnızca otorite yükseldikçe eleştirel incelemenin düşebileceği hipotezini görünür kılar.

| Görünen davranış | Olası teknik açıklama | Olası güç ilişkisi |
|---|---|---|
| Hızlı onay | Değişiklik küçük ve güvenlidir | Kıdemliye itiraz etmekten kaçınma |
| Çok sayıda yorum | Kod gerçekten sorunludur | Junior geliştiriciyi aşırı denetleme |
| Yorumsuz onay | Reviewer konuya hâkim değildir | Otorite sahibine karşı sessiz kalma |
| Uzayan tartışma | Mimari belirsizlik vardır | Statü mücadelesi yaşanıyordur |

Tablo bir suçlama listesi değildir. Aynı davranışın hem teknik hem sosyal nedenleri bulunabilir. Ama yalnızca teknik açıklamayı kabul etmek, ekibin kör noktalarını büyütür.

## “LGTM” bir onaydan fazlası olabilir

Review yorumları nötr görünse de kullanılan dil hiyerarşiyi açığa çıkarır. Bir kişiye “Bunu neden böyle yaptın?” denirken diğerine “Burada farklı bir yaklaşım düşünülebilir mi?” denmesi, psikolojik güvenliğin eşit dağılmadığını gösterebilir. Ayrıca yöneticinin veya teknik liderin PR’ına ilk itiraz eden kişi olmak, bazı ekiplerde gereksiz bir kariyer riski gibi algılanır.

Bu örüntüyü görmek için basit metrikler üretilebilir:

```python
reviews = [
    {"author": "junior", "comments": 12, "changed_lines": 40},
    {"author": "senior", "comments": 2, "changed_lines": 180},
]

for review in reviews:
    density = review["comments"] / max(review["changed_lines"], 1)
    print(review["author"], round(density, 3))
```

Kod, değiştirilen satır başına yorum yoğunluğunu hesaplar. Ancak yüksek yoğunluk otomatik olarak ayrımcılık kanıtı değildir. Değişikliğin riski, dosyanın karmaşıklığı ve yorumların niteliği de değerlendirilmelidir. Metrikler hüküm vermek için değil, doğru soruları başlatmak için kullanılmalıdır.

## Daha dengeli bir review kültürü

İlk adım, kod sahibinin kimliğinden önce değişikliğin riskini değerlendiren ortak bir kontrol listesi oluşturmaktır. Güvenlik, test kapsamı, geriye dönük uyumluluk ve gözlemlenebilirlik gibi ölçütler herkes için aynı olmalıdır.

İkinci olarak ekipler, kıdemli geliştiricilerin PR’larında da alan uzmanı onayı aramalıdır. Kıdem, her konuda uzmanlık anlamına gelmez. Teknik liderlerin gelen eleştirilere açıkça teşekkür etmesi de itiraz etmenin güvenli olduğuna dair güçlü bir kültürel sinyal üretir.

Son olarak review başarısı, “kaç hata bulduk?” yerine “hangi bilgiyi paylaştık?” sorusuyla ölçülmelidir. İyi bir code review ne sorgusuz itaattir ne de satır satır üstünlük gösterisi. Amaç, otoritenin kodun önüne geçmediği ve herkesin gerekçesini açıklayabildiği ortak bir düşünme alanı kurmaktır.
