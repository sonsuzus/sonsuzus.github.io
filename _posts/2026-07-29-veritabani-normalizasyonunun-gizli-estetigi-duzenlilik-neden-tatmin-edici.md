---
layout: post
title: "Veritabanı Normalizasyonunun Gizli Estetiği: Düzenlilik Neden Tatmin Edici?"
math: true
categories: 
  - Bilgi
tags: 
  - veritabanı
  - normalizasyon
  - yazılım psikolojisi
---

Dağınık bir tabloyu küçük, anlamlı ve birbirine düzgün bağlanan tablolara dönüştürmek yalnızca teknik bir iyileştirme değildir. Tekrarlanan sütunların kaybolması, bağımlılıkların görünür hâle gelmesi ve her bilginin kendine ait bir yere kavuşması zihinsel bir rahatlama yaratır. Peki bu tatmin nereden gelir? Normalizasyonun estetiği; beynimizin örüntüleri tanıma, belirsizliği azaltma ve karmaşık sistemleri daha küçük parçalara ayırma eğilimiyle yakından ilişkilidir.

``

## Normalizasyon Gerçekte Neyi Düzenler?

Veritabanı normalizasyonu, verileri belirli kurallara göre ayrıştırarak tekrarları ve istenmeyen bağımlılıkları azaltma sürecidir. Amaç yalnızca daha fazla tablo üretmek değil; her gerçeği mümkün olduğunca tek bir yerde saklamaktır.

Örneğin sipariş, müşteri ve ürün bilgilerinin aynı tabloda tutulduğunu düşünelim. Bir müşteri on sipariş verdiyse adresi de on kez tekrarlanır. Adres değiştiğinde bütün satırları güncellemek gerekir. Bir satır unutulursa aynı müşterinin iki farklı adresi varmış gibi görünür. Buna **güncelleme anomalisi** denir.

| Yaklaşım | Zihinsel etkisi | Teknik sonucu |
|---|---|---|
| Tek büyük tablo | İlk bakışta kolay, zamanla yorucu | Tekrar ve tutarsızlık |
| Normalize edilmiş yapı | Sınırları belirgin, öngörülebilir | Daha güvenli güncelleme |
| Aşırı normalizasyon | Fazla parçalı, takip etmesi zor | Çok sayıda JOIN işlemi |

Bu karşılaştırma önemli bir gerçeği gösterir: Estetik, mutlak sadelikten değil, **doğru miktarda düzenlenmiş karmaşıklıktan** doğar.

## Fonksiyonel Bağımlılığın Zarafeti

Normalizasyonun teorik kalbinde fonksiyonel bağımlılık bulunur. Bir $X$ değeri, bir $Y$ değerini tek biçimde belirliyorsa bunu şöyle yazarız:

$$X \rightarrow Y$$

Örneğin müşteri numarası müşterinin adını belirliyorsa:

$$MusteriID \rightarrow MusteriAdi$$

Bu ifade küçük bir matematiksel cümle gibi çalışır: “Kimliği biliyorsan adı da bilirsin.” İkinci normal form kısmi bağımlılıkları, üçüncü normal form ise anahtar olmayan alanların birbirine bağımlılığını ortadan kaldırmaya çalışır. Böylece her tablo daha net bir sorumluluk kazanır.

```sql
CREATE TABLE Musteri (
    musteri_id INT PRIMARY KEY,
    ad VARCHAR(100),
    adres VARCHAR(200)
);

CREATE TABLE Siparis (
    siparis_id INT PRIMARY KEY,
    musteri_id INT NOT NULL,
    tarih DATE,
    FOREIGN KEY (musteri_id) REFERENCES Musteri(musteri_id)
);
```

Bu yapı, müşteri adresini her siparişte yeniden saklamak yerine `Musteri` tablosunda tekilleştirir. `Siparis` tablosu ise müşteriyi yabancı anahtarla işaret eder. Kodun verdiği tatmin, iki kavramın sınırlarının artık karışmamasından gelir.

## Beyin Neden Düzeni Seviyor?

İnsan zihni sürekli tahmin üretir. Bir sistemin davranışı öngörülebilir olduğunda bilişsel yük azalır; çelişki veya belirsizlik ortaya çıktığında ise dikkat ihtiyacı artar. Normalize edilmiş bir şema, “Bu bilgi nerede bulunur?” sorusuna kararlı cevaplar verir. Bu da çalışma belleğinin aynı anda taşıması gereken olasılıkları azaltır.

Burada “haz merkezi” ifadesini fazla basitleştirmemek gerekir. Beyinde düzen sevgisine ayrılmış tek bir düğme yoktur. Örüntü tanıma, beklentinin doğrulanması, kontrol hissi ve problem çözme başarısı birlikte ödüllendirici bir deneyim oluşturabilir. Bir geliştiricinin kusursuz bir şemaya bakarken hissettiği memnuniyet, tamamlanan yapbozun son parçasına benzer.

## Düzen Her Zaman Daha İyi midir?

Hayır. Analitik sistemlerde performans için denormalizasyon yapılabilir. Her sorguda on tabloyu birleştirmek teorik saflığı korurken pratik maliyeti artırabilir. Bu nedenle iyi tasarımın hedefi “en normalize yapı” değil, veri bütünlüğü ile kullanım ihtiyacı arasındaki dengedir.

Normalizasyonun gizli estetiği tam burada belirir: Güzel şema, bütün karmaşıklığı yok etmez; onu anlaşılır sınırlara yerleştirir. Zihnimizi rahatlatan şey kusursuz simetri değil, her parçanın neden orada olduğunu açıklayabilmektir.
