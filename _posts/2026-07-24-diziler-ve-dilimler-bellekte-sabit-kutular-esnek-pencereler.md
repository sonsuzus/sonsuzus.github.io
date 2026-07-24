---
layout: post
title: "Diziler ve Dilimler: Bellekte Sabit Kutular, Esnek Pencereler"
math: true
categories: 
  - Bilgi
tags: 
  - Go
  - Arrays
  - Slices
  - Bellek Yönetimi
---

Bir veri koleksiyonunu saklamak istediğimizde aklımıza ilk gelen yapı genellikle dizidir; ama Go gibi dillerde sahneye bir de dilimler, yani slices çıkar. Dizi, bellekte yan yana duran sabit sayıda kutu gibidir; dilim ise bu kutuların tamamını ya da bir bölümünü gösteren akıllı bir pencere. Aralarındaki farkı anlamak, sadece sözdizimini değil, performans ve bellek davranışını da doğru okumayı sağlar.
``

## Teorik Temel: Boyut mu, Esneklik mi?

Dizi, uzunluğu türünün parçası olan sabit boyutlu bir veri yapısıdır. Go’da `[3]int` ile `[4]int` farklı türlerdir. Yani derleyici için “3 elemanlı int dizisi” ile “4 elemanlı int dizisi” aynı ailenin kuzenleri bile değildir; tamamen ayrı kimliklere sahiptir.

Dilim ise kendi başına veriyi doğrudan taşımaz. Arkasında genellikle bir dizi bulunur ve dilim bu dizinin belirli bir aralığına referans verir. Bir slice üç parçalı küçük bir başlık gibi düşünülebilir:

- işaretçi: alttaki dizide başlangıç konumu,
- uzunluk: şu an görünen eleman sayısı,
- kapasite: başlangıçtan itibaren kullanılabilecek maksimum alan.

Matematiksel olarak temel kural şudur: $0 \le len(slice) \le cap(slice)$. Yani uzunluk kapasiteyi aşamaz; ama `append` ile kapasite yetmezse Go yeni ve daha büyük bir alttaki dizi ayırabilir.

| Özellik | Array | Slice |
|---|---|---|
| Boyut | Sabit | Dinamik görünümlü |
| Tür bilgisi | Boyut türün parçasıdır | Boyut türün parçası değildir |
| Kopyalama | Tüm elemanlar kopyalanır | Başlık kopyalanır, veri paylaşılabilir |
| Bellek modeli | Doğrudan veri | Alttaki diziye referans |
| Esneklik | Düşük | Yüksek |

## Diziler: Sabit Boyutlu Disiplin

Diziler, özellikle boyutun kesin bilindiği durumlarda harikadır. Örneğin RGB renk değeri için `[3]uint8` gayet anlamlıdır. Çünkü kırmızı, yeşil ve mavi olmak üzere tam üç kanal vardır; dördüncü eleman beklenmez.

```go
func updateArray(a [3]int) {
    a[0] = 99
}

func main() {
    nums := [3]int{1, 2, 3}
    updateArray(nums)
    println(nums[0]) // 1
}
```

Bu örnekte `updateArray` fonksiyonuna dizi gönderildiğinde tüm dizi kopyalanır. Fonksiyon içindeki değişiklik dışarıdaki `nums` dizisini etkilemez. Bu davranış güvenlidir ama büyük dizilerde maliyetli olabilir. Eğer $n$ elemanlı bir dizi kopyalanıyorsa işlem maliyeti yaklaşık $O(n)$ olur.

## Dilimler: Esnek ve Paylaşımcı Pencereler

Dilimlerde durum daha hareketlidir. Slice değeri kopyalansa bile alttaki dizi çoğu zaman aynı kalır. Bu yüzden bir fonksiyona slice gönderdiğinizde eleman değişiklikleri dışarıdan görülebilir.

```go
func updateSlice(s []int) {
    s[0] = 99
}

func main() {
    nums := []int{1, 2, 3}
    updateSlice(nums)
    println(nums[0]) // 99
}
```

Burada `s` aslında slice başlığının kopyasıdır; fakat başlığın gösterdiği alttaki dizi aynıdır. Bu nedenle `s[0] = 99`, orijinal veriyi değiştirir. İşte slice’ların “referans gibi davranıyor” denmesinin sebebi budur. Tam anlamıyla referans türü demek yerine, “referans taşıyan küçük bir descriptor” demek daha doğrudur.

## Append ve Kapasite Sürprizi

Slice’ların en eğlenceli tarafı `append` ile büyüyebilmesidir; ama burada küçük bir numara vardır. Kapasite yetiyorsa aynı alttaki dizi kullanılır. Yetmiyorsa yeni bir dizi oluşturulur ve elemanlar oraya taşınır.

```go
func main() {
    a := []int{10, 20, 30}
    b := a[:2]

    b = append(b, 99)

    println(a[2]) // kapasite yeterse 99 olabilir
}
```

Bu örnekte `b`, `a` dizisinin ilk iki elemanını gösterir. Eğer `b` için kapasite yeterliyse `append`, üçüncü konuma `99` yazar ve `a[2]` de değişmiş gibi görünür. Bu, slice paylaşımının hem süper gücü hem de potansiyel tuzağıdır.

| Senaryo | Sonuç | Dikkat Edilecek Nokta |
|---|---|---|
| Slice elemanı değiştirme | Alttaki dizi değişir | Diğer slice’lar etkilenebilir |
| Append, kapasite yeterli | Aynı dizi kullanılır | Yan etki oluşabilir |
| Append, kapasite yetersiz | Yeni dizi ayrılır | Eski slice etkilenmeyebilir |
| Array fonksiyona geçme | Tam kopya | Büyük veri için pahalıdır |

## Ne Zaman Hangisi?

Boyut gerçekten sabitse ve bu bilgi programın anlamının parçasıysa array iyi seçimdir. Örneğin matris boyutu, kriptografik bloklar veya sabit protokol alanları buna uygundur. Ancak çoğu uygulama kodunda veri miktarı çalışma zamanında değişir: kullanıcı listeleri, dosyadan okunan satırlar, API sonuçları... Bu durumda slice çok daha pratiktir.

Kısa özetle: array, bellekte düzenli ve sabit bir apartman; slice ise bu apartmanın odalarına bakan esnek bir emlak danışmanıdır. Danışman hafiftir, kolay kopyalanır; ama hangi odayı gösterdiğini unutursanız yanlış duvarı boyayabilirsiniz. Go’da güçlü ve hatasız kod yazmanın yolu, bu küçük pencerenin arkasındaki büyük diziyi her zaman akılda tutmaktan geçer.
