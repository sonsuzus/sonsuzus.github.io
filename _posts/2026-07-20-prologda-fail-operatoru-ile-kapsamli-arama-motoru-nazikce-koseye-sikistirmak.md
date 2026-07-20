---
layout: post
title: "Prolog’da Fail Operatörü ile Kapsamlı Arama: Motoru Nazikçe Köşeye Sıkıştırmak"
math: true
categories: 
  - Bilgi
tags: 
  - Prolog
  - mantıksal programlama
  - fail operatörü
  - backtracking
---

Prolog’da bazen cevabı bulmak yetmez; tüm cevapları, tüm kombinasyonları, hatta köşede saklanan o utangaç olasılığı da görmek isteriz. İşte `fail` operatörü burada sahneye çıkar: Sisteme bilinçli olarak başarısızlık dayatır ve Prolog motorunu geri izleme, yani backtracking yapmaya zorlar.
``

İlk bakışta kulağa tuhaf gelir: Neden çalışan bir kuralı bilerek başarısız yapalım? Çünkü Prolog’un arama mantığı, başarısızlık anında alternatif yolları denemeye dayanır. Prolog, bir hedefi kanıtlamaya çalışırken bilgi tabanındaki olası eşleşmeleri sırayla inceler. Bir eşleşme bulunduğunda durabilir; fakat `fail` kullanırsak motor şöyle der: “Tamam, bu sonuç güzel ama başarılı sayılmadık, başka ihtimal var mı?”

Teorik olarak Prolog, hedefleri birer mantıksal önerme gibi ele alır. Örneğin şu sorgu:

$başarılı(X) \leftarrow öğrenci(X) \land notu(X,N) \land N \ge 50$

şunu anlatır: Bir `X`, öğrenci ise ve notu `N` olup `N >= 50` koşulunu sağlıyorsa başarılıdır. Prolog bu tür ilişkileri kanıtlamak için unification ve depth-first search kullanır. Yani önce bir yolu derinlemesine dener, olmazsa geri döner.

| Kavram | Ne Yapar? | Günlük Hayat Benzetmesi |
|---|---|---|
| Unification | Değişkenleri uygun değerlerle eşleştirir | Boş forma uygun bilgileri doldurmak |
| Backtracking | Alternatif çözümlere geri döner | Yanlış sokaktan dönüp diğer sokağa girmek |
| `fail` | Mevcut çözümü bilerek reddeder | “Bunu gördüm, sıradakini getir” demek |
| Choice point | Geri dönülebilecek karar noktasıdır | Yol ayrımına konan işaret |

Şimdi küçük ama lezzetli bir örnek görelim:

```prolog
ogrenci(ayse).
ogrenci(veli).
ogrenci(zeynep).

ders(ayse, prolog, 85).
ders(veli, prolog, 42).
ders(zeynep, prolog, 91).
ders(ayse, yapay_zeka, 78).

basarili(Ogrenci, Ders) :-
    ders(Ogrenci, Ders, Not),
    Not >= 50.

tum_basarililari_yaz :-
    basarili(Ogrenci, Ders),
    write(Ogrenci), write(' - '), write(Ders), nl,
    fail.

tum_basarililari_yaz.
```

Buradaki kritik bölüm `tum_basarililari_yaz` kuralıdır. Önce `basarili(Ogrenci, Ders)` hedefi bir eşleşme bulur. Sonra sonucu ekrana yazar. Ardından `fail` gelir ve kuralı başarısız yapar. Bu başarısızlık Prolog’u önceki choice point’e döndürür. Böylece başka başarılı öğrenci-ders kombinasyonları aranır.

En sonda ikinci bir `tum_basarililari_yaz.` kuralı vardır. Bu küçük satır, arama tamamen bittikten sonra sorgunun genel olarak başarılı görünmesini sağlar. Aksi hâlde tüm sonuçlar yazılsa bile sorgu nihai olarak `false` dönebilir. Yani `fail` sahnede kaos çıkarır, ikinci kural da perdeyi düzgün kapatır.

| Yöntem | Kullanım Amacı | Avantaj | Dikkat Edilecek Nokta |
|---|---|---|---|
| `fail` ile yazdırma | Tüm çözümleri yan etkiyle gezmek | Basit ve öğreticidir | Sonuç toplamaz, sadece işler |
| `findall/3` | Tüm çözümleri listeye almak | Veri olarak kullanılabilir | Bellek tüketebilir |
| `bagof/3` | Gruplanmış çözümler üretmek | Mantıksal ayrım güçlüdür | Serbest değişkenlere dikkat ister |
| `setof/3` | Tekrarsız ve sıralı sonuçlar | Temiz çıktı verir | Sıralama otomatik gelir |

Aynı örneği liste toplayarak yazmak istersek:

```prolog
tum_basarililar(Liste) :-
    findall(Ogrenci-Ders, basarili(Ogrenci, Ders), Liste).
```

Bu kez Prolog sonuçları ekrana basmak yerine `Liste` içinde toplar. Yani `fail` daha çok “tüm olasılıkları dolaş ve bu sırada bir şey yap” senaryolarında parlar. Raporlama, debug çıktısı üretme, kombinasyonları test etme veya bilgi tabanını tarama gibi işlerde oldukça kullanışlıdır.

Mantıksal açıdan `fail`, her zaman yanlış olan özel bir hedeftir. Bunu şöyle düşünebiliriz:

$fail \equiv false$

Ama etkisi sadece yanlış olmak değildir; Prolog’un arama mekanizmasını tetiklemesidir. Bu yüzden `fail` operatörü, mantıksal programlamada başarısızlığın bazen üretken bir araç olabileceğini gösterir. Normal programlamada hata can sıkıcıdır; Prolog’da ise doğru yerde kullanılan başarısızlık, bilgi tabanının tamamını konuşturan küçük bir dedektif olabilir.

Sonuç olarak `fail`, Prolog öğrenirken mutlaka anlaşılması gereken güçlü bir tekniktir. Motoru pes ettirmez; aksine pes etmeye zorlayarak her alternatifi denetir. Yeter ki onu bilinçli kullanın: Yoksa Prolog, sizin adınıza sonsuz bir olasılıklar labirentine neşeyle dalabilir.
