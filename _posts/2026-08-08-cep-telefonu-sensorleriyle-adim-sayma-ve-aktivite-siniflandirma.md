---
layout: post
title: "Cep Telefonu Sensörleriyle Adım Sayma ve Aktivite Sınıflandırma"
math: true
categories: 
  - Proje
tags: 
  - ivmeölçer
  - makine öğrenmesi
  - sinyal işleme
---

Telefonunuz cebinizde sessizce duruyor gibi görünse de ivmeölçer sensörü her saniye onlarca ölçüm üretir. Bu ham veriyi doğru biçimde işlediğimizde kaç adım atıldığını hesaplayabilir; kullanıcının yürüdüğünü, koştuğunu veya hareketsiz kaldığını tahmin edebiliriz. Bu projede gürültülü sensör değerlerini anlamlı aktivite bilgisine dönüştüren uçtan uca bir sistem kuracağız.
``

## Ham ivmeölçer verisini anlamak

İvmeölçer, telefonun üç eksendeki ivmesini ölçer: $a_x$, $a_y$ ve $a_z$. Değerler genellikle $m/s^2$ cinsindendir. Telefon masada hareketsiz olsa bile sensör sıfır göstermez; çünkü yerçekimi ivmesi olan yaklaşık $9.81\,m/s^2$ ölçüme dahildir.

Telefonun cebimizdeki yönü sürekli değişebileceği için eksenleri ayrı ayrı kullanmak kırılgan bir çözümdür. Bunun yerine toplam ivme büyüklüğünü hesaplayabiliriz:

$$a = \sqrt{a_x^2 + a_y^2 + a_z^2}$$

Bu değer telefonun yönünden büyük ölçüde bağımsızdır. Dinamik hareketi görmek için yerçekimi bileşeni çıkarılabilir:

$$a_d = a - g$$

Burada $g \approx 9.81\,m/s^2$ kabul edilir. Daha güvenilir uygulamalarda sabit çıkarma yerine alçak geçiren filtreyle tahmin edilen yerçekimi kullanılır.

| İşlem | Amaç | Uygun yöntem |
|---|---|---|
| Gürültü azaltma | Sensördeki küçük titreşimleri temizlemek | Alçak geçiren filtre |
| Yerçekimi ayırma | Gerçek vücut hareketini bulmak | Yüksek geçiren filtre |
| Yön bağımsızlığı | Telefon konumunun etkisini azaltmak | Vektör büyüklüğü |
| Pencereleme | Sinyali analiz edilebilir parçalara bölmek | 2–5 saniyelik pencereler |

## Adımları tepe noktalarıyla saymak

Yürürken her adım, filtrelenmiş ivme sinyalinde belirgin bir tepe oluşturur. Ancak her tepeyi adım kabul edersek telefonu sallamak bile maraton koşmuşuz gibi görünebilir. Bu nedenle üç koşul kullanılır: minimum tepe yüksekliği, iki tepe arasındaki minimum süre ve tepenin belirginliği.

Normal yürüyüş frekansı çoğunlukla $1$–$2.5$ Hz aralığındadır. Dolayısıyla iki adım arasında örneğin en az $0.3$ saniye bulunmasını isteyebiliriz. Eşiklerin kişiye ve telefon konumuna göre ayarlanması sonuçları iyileştirir.

```python
import numpy as np
from scipy.signal import butter, filtfilt, find_peaks

def analyze_steps(ax, ay, az, sample_rate=50):
    # Telefon yönünden bağımsız toplam ivme büyüklüğü
    magnitude = np.sqrt(ax**2 + ay**2 + az**2)

    # Yürüme ritmini koruyan 0.5–3 Hz bant geçiren filtre
    nyquist = sample_rate / 2
    b, a = butter(3, [0.5 / nyquist, 3 / nyquist], btype='band')
    filtered = filtfilt(b, a, magnitude)

    # En az 0.3 saniye aralıklı ve belirgin tepeleri bul
    peaks, _ = find_peaks(
        filtered,
        distance=int(0.3 * sample_rate),
        prominence=0.4
    )
    return len(peaks), filtered, peaks
```

Bu fonksiyon önce büyüklüğü hesaplar, ardından yürüyüş dışındaki çok yavaş ve çok hızlı değişimleri süzer. `find_peaks`, belirgin ritmik tepelerin indekslerini döndürür; tepe sayısı da yaklaşık adım sayısıdır.

## Aktivite türünü sınıflandırmak

Aktivite sınıflandırması için sinyal, örtüşmeli zaman pencerelerine bölünür. Her pencereden ortalama, standart sapma, maksimum değer, enerji ve baskın frekans gibi özellikler çıkarılır. Örneğin sinyal enerjisi şöyle hesaplanabilir:

$$E = \frac{1}{N}\sum_{i=1}^{N}a_i^2$$

| Aktivite | Standart sapma | Baskın frekans | Enerji |
|---|---:|---:|---:|
| Hareketsiz | Düşük | Belirsiz | Düşük |
| Yürüme | Orta | 1–2.5 Hz | Orta |
| Koşma | Yüksek | 2–4 Hz | Yüksek |

Bu özellikler Random Forest, SVM veya küçük bir sinir ağına verilebilir. Başlangıç için Random Forest; ölçeklemeye daha az duyarlı, hızlı ve yorumlanabilir olduğu için iyi bir seçimdir. Eğitim verisini farklı kişilerden, telefon konumlarından ve hızlardan toplamak kritik önemdedir. Aksi hâlde model kullanıcıyı değil, yalnızca belirli bir cebi ezberleyebilir!

Başarıyı değerlendirirken adım sayımı için ortalama mutlak hata; sınıflandırma için doğruluk, F1 skoru ve karmaşıklık matrisi kullanılmalıdır. Son aşamada işlemleri kısa pencerelerle gerçek zamanlı çalıştırarak pil tüketimi ile doğruluk arasında dengeli bir mobil aktivite takipçisi elde edebiliriz.
