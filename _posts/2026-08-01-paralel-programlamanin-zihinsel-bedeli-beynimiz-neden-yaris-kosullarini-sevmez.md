---
layout: post
title: "Paralel Programlamanın Zihinsel Bedeli: Beynimiz Neden Yarış Koşullarını Sevmez?"
math: true
categories: 
  - Bilgi
tags: 
  - paralel programlama
  - eşzamanlılık
  - yazılım mimarisi
---

Bir programın aynı anda birkaç iş yapması kulağa verimlilik gibi gelir: dosya indirirken arayüz yanıt verir, sunucu binlerce isteği işler, işlemci çekirdekleri veriyi paylaşır. Ne var ki kod hızlanırken onu anlamaya çalışan insan zihni yavaşlayabilir. Çünkü beynimiz olayları öyküler gibi, çoğunlukla belirli bir sırayla kavrar; eşzamanlı programlarsa tek bir öykü yerine birbirine karışabilen çok sayıda olası senaryo üretir.
``

## Eşzamanlılık ile paralellik aynı şey değildir

**Eşzamanlılık**, birden fazla işin ilerleyişinin aynı zaman aralığında yönetilmesidir. **Paralellik** ise bu işlerden birkaçının fiziksel olarak aynı anda yürütülmesidir. Tek çekirdekli bir işlemci görevler arasında hızla geçiş yaparak eşzamanlı olabilir; çok çekirdekli bir işlemciyse görevleri gerçekten paralel çalıştırabilir.

| Kavram | Temel soru | İnsan zihnindeki benzeri |
|---|---|---|
| Sıralı çalışma | Sonraki adım hangisi? | Tarifi adım adım uygulamak |
| Eşzamanlılık | Hangi iş ne zaman ilerleyecek? | Yemek yaparken telefonu yanıtlamak |
| Paralellik | Kaç iş gerçekten aynı anda çalışıyor? | Bir ekibin farklı işleri paylaşması |
| Senkronizasyon | Kim, kimi beklemeli? | Toplantıya herkesin gelmesini beklemek |

Bu ayrım önemlidir; fakat zihinsel bedelin ana kaynağı ikisinde de aynıdır: olası yürütme sıralarının çoğalması.

## Olasılık ağacı neden hızla büyür?

İki iş parçacığının üçer atomik adımı olduğunu düşünelim. Her iş parçacığının kendi iç sırası korunurken adımlar farklı biçimlerde iç içe geçebilir. Olası sıralama sayısı kabaca kombinasyonla hesaplanır:

$$N = \frac{(a+b)!}{a!b!}$$

$a=3$ ve $b=3$ için $N=20$ olur. İş parçacığı ve adım sayısı arttıkça sayı patlar. Üstelik gerçek programlarda önbellek, işletim sistemi zamanlayıcısı, G/Ç gecikmesi ve bellek modeli de oyuna katılır. Programcı yalnızca “Kod ne yapıyor?” sorusunu değil, “Başka hangi sırayla yapabilir?” sorusunu da yanıtlamak zorundadır.

İnsan çalışma belleği sınırlıdır. Birkaç değişkenin değerini, kilitlerin durumunu ve iş parçacıklarının konumunu aynı anda zihinde tutmaya çalışmak bilişsel yükü artırır. Bu nedenle eşzamanlılık hataları çoğu zaman kodu yazarken değil, nadir bir zamanlama gerçekleştiğinde ortaya çıkar.

## Klasik tuzak: yarış koşulu

Aşağıdaki Python örneğinde iki iş parçacığı aynı sayacı artırır:

```python
import threading

counter = 0

def increment():
    global counter
    for _ in range(100_000):
        counter += 1  # Okuma, artırma ve yazma tek bir düşünsel adım değildir.

threads = [threading.Thread(target=increment) for _ in range(2)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print(counter)
```

`counter += 1` basit görünür; ancak kavramsal olarak değeri okuma, yeni değeri hesaplama ve geri yazma aşamalarından oluşur. İki iş parçacığı aynı eski değeri okuyabilir ve artışlardan biri kaybolabilir. Buna **yarış koşulu** denir: sonuç, işlemlerin zamanlamasına bağlıdır.

Bir kilit kritik bölgeyi koruyabilir:

```python
lock = threading.Lock()

def safe_increment():
    global counter
    for _ in range(100_000):
        with lock:
            counter += 1  # Bu bölgeye aynı anda yalnızca bir iş parçacığı girer.
```

Kilidin bedeli yalnızca performans değildir. Programcı artık kilidin nerede alındığını, ne zaman bırakıldığını ve başka kilitlerle hangi sırada kullanıldığını da izlemelidir. Yanlış sıra, bu kez deadlock adlı “Herkes birbirini bekliyor” komedisine dönüşebilir.

## Beyne uygun eşzamanlılık tasarlamak

| Yaklaşım | Zihinsel avantaj | Olası bedel |
|---|---|---|
| Değişmez veri | Paylaşılan durum azalır | Daha fazla kopyalama |
| Mesajlaşma | Etkileşim açık hale gelir | Mesaj sırası yönetilmelidir |
| Actor modeli | Durum tek sahipte toplanır | Mimari öğrenme gerektirir |
| Yapılandırılmış eşzamanlılık | Görev ömürleri sınırlandırılır | Eski API’lerle uyum zorlaşabilir |

En güvenli strateji, beynimizi daha fazla iş parçacığı düşünmeye zorlamak değil, düşünülmesi gereken durum sayısını azaltmaktır. Paylaşılan değişkenleri sınırlamak, saf fonksiyonlar kullanmak, görev sahipliğini açıkça belirtmek ve zaman aşımı tasarlamak kodu anlatılabilir hale getirir.

Sonuçta paralel programlama yalnızca işlemci çekirdeklerini yönetme sanatı değildir; olasılık uzayını insan zihninin taşıyabileceği boyuta indirme sanatıdır. İyi eşzamanlı kod, sadece hızlı çalışan değil, sabah kahvesinden önce bile hangi olayın kimi beklediği anlaşılabilen koddur.
