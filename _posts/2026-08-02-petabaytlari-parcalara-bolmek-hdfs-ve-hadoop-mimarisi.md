---
layout: post
title: "Petabaytları Parçalara Bölmek: HDFS ve Hadoop Mimarisi"
math: true
categories: 
  - Bilgi
tags: 
  - HDFS
  - Hadoop
  - Dağıtık Sistemler
---

Bir petabayt veriyi dizüstü bilgisayarınıza kopyalamaya çalıştığınızı düşünün. Diskin itiraz etmesi bir yana, işlem tamamlanmadan bilgisayarınız emekli olabilir! Hadoop Dağıtık Dosya Sistemi, yani HDFS, bu problemi devasa ve pahalı bir sunucu almak yerine veriyi yüzlerce sıradan makineye dağıtarak çözer. Üstelik disk arızalarını istisna değil, sistemin doğal bir parçası kabul eder.
``
## HDFS neden ortaya çıktı?

Geleneksel dosya sistemleri, çoğunlukla tek makinenin disklerini yönetir. Veri büyüklüğü terabaytlardan petabaytlara çıktığında kapasite, aktarım hızı ve hata toleransı ciddi sorunlara dönüşür. HDFS'nin temel düşüncesi basittir: **Veriyi hesaplamaya taşımak yerine hesaplamayı veriye taşı.**

Bir dosya küçük bloklara ayrılır ve farklı bilgisayarlarda saklanır. Toplam kullanılabilir kapasite kabaca şöyle düşünülebilir:

$$C_{toplam} = \frac{N \times D}{R}$$

Burada $N$ düğüm sayısını, $D$ her düğümün disk kapasitesini, $R$ ise çoğaltma faktörünü gösterir. Örneğin 100 makinenin her birinde 10 TB alan ve çoğaltma faktörü 3 ise kullanılabilir kapasite yaklaşık $333$ TB olur.

| Özellik | Geleneksel dosya sistemi | HDFS |
|---|---|---|
| Depolama | Tek sunucu ağırlıklı | Çok sayıda düğüme dağıtılmış |
| Hata yaklaşımı | Arıza olağan dışıdır | Arıza beklenen bir durumdur |
| Dosya tipi | Küçük ve büyük dosyalar | Büyük dosyalar için ideal |
| Erişim modeli | Düşük gecikme | Yüksek aktarım kapasitesi |
| Ölçekleme | Daha güçlü sunucu | Daha fazla sıradan sunucu |

## NameNode ve DataNode rolleri

HDFS mimarisinin koordinatörü **NameNode**'dur. Dosya adlarını, klasörleri, izinleri ve hangi bloğun hangi makinede bulunduğunu takip eder. Ancak gerçek dosya içeriğini saklamaz. Onu, işçiler gibi çalışan **DataNode** düğümleri depolar.

Bir istemci dosya okumak istediğinde önce NameNode'a başvurur. NameNode uygun DataNode adreslerini bildirir; veri daha sonra doğrudan DataNode'lardan alınır. Böylece NameNode, bütün verinin içinden geçtiği bir darboğaza dönüşmez.

DataNode'lar düzenli olarak **heartbeat** mesajları göndererek hayatta olduklarını bildirir. Bir düğüm uzun süre sessiz kalırsa NameNode onu arızalı sayar ve eksilen kopyaların başka düğümlerde oluşturulmasını ister.

## Bloklar ve çoğaltma

HDFS dosyaları genellikle 128 MB gibi büyük bloklara böler. Diyelim ki 300 MB büyüklüğünde bir dosyamız var. Bu dosya 128 MB, 128 MB ve 44 MB olmak üzere üç bloğa ayrılır. Çoğaltma faktörü 3 olduğunda her blok üç farklı DataNode üzerinde tutulur.

Bir bloğun kullanılabilir olma olasılığı, bağımsız düğüm arızası varsayımıyla şu şekilde ifade edilebilir:

$$P_{erişim} = 1 - p^R$$

$p$ tek düğümün arıza olasılığıdır. $p=0.1$ ve $R=3$ için bloğun bütün kopyalarını kaybetme olasılığı yalnızca $0.001$ olur. Elbette gerçek sistemlerde aynı rack veya ağ anahtarının çökmesi gibi ilişkili arızalar da vardır. Bu nedenle HDFS, kopyaları farklı rack'lere dağıtan **rack awareness** yaklaşımını kullanır.

## Dosya yükleme akışı

Aşağıdaki komut yerel bir dosyayı HDFS'ye gönderir:

```bash
hdfs dfs -mkdir -p /veri/loglar
hdfs dfs -put uygulama.log /veri/loglar/
hdfs dfs -ls /veri/loglar
```

İlk komut hedef klasörü oluşturur, ikincisi dosyayı HDFS'ye yükler, üçüncüsü sonucu listeler. Arka plandaki süreç ise şöyledir:

```text
1. İstemci, NameNode'dan dosya oluşturma izni ister.
2. NameNode uygun DataNode zincirini belirler.
3. İstemci bloğu ilk DataNode'a yollar.
4. Blok zincirdeki diğer DataNode'lara aktarılır.
5. Onaylar ters yönde istemciye döner.
```

Bu aktarım zinciri, istemcinin her kopyayı ayrı ayrı göndermesini önleyerek ağ kullanımını dengeler.

## Güçlü olduğu ve olmadığı yerler

HDFS; günlük kayıtları, video arşivleri, sensör verileri ve toplu analitik işlemler için mükemmeldir. Buna karşılık milyonlarca küçük dosya NameNode belleğini tüketebilir. Sürekli rastgele güncelleme isteyen işlemler ve milisaniyelik yanıt bekleyen uygulamalar da HDFS'nin uzmanlık alanı değildir.

Kısacası HDFS, tek bir süper bilgisayar yerine birlikte çalışan sıradan makinelerden güvenilir bir depolama ordusu kurar. Hadoop ekosistemindeki MapReduce veya Spark gibi araçlar da hesaplamayı ilgili blokların bulunduğu düğümlere yaklaştırarak petabaytların ağda gereksiz yere dolaşmasını engeller.
