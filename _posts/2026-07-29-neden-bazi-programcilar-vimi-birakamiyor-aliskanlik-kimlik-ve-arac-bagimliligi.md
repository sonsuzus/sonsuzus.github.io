---
layout: post
title: "Neden Bazı Programcılar Vim’i Bırakamıyor? Alışkanlık, Kimlik ve Araç Bağımlılığı"
math: true
categories: 
  - Bilgi
tags: 
  - Vim
  - programcı psikolojisi
  - geliştirici araçları
---

Bir programcının Vim hakkında konuşmaya başlaması bazen teknik bir sohbetten çok aile yadigârını anlatmasına benzer. “Hızlı”, “hafif” ve “her sunucuda var” gibi makul gerekçeler sıralanır; ardından tuş kombinasyonları, nokta komutu ve fare kullanmamanın erdemleri gelir. Fakat Vim bağlılığını yalnızca verimlilikle açıklamak eksik kalır. Burada alışkanlık döngüleri, emekle kurulan duygusal bağ, topluluk üyeliği ve profesyonel kimlik aynı terminal penceresinde buluşur.
``

## Editör değil, öğrenilmiş bir hareket sistemi

Vim’in temel farkı **modal** olmasıdır. Normal modda tuşlar karakter yazmak yerine komut verir; ekleme modunda ise metin oluşturur. Böylece düzenleme, tek tek düğmelere basmaktan ziyade küçük bir dil konuşmaya dönüşür. Örneğin `dw` “sonraki kelimeyi sil”, `ci"` ise “tırnakların içini değiştir” anlamına gelir.

Bu yapı, başlangıçta yüksek bilişsel yük üretir. Zamanla komutlar prosedürel belleğe taşınır ve kullanıcı artık adımları bilinçli biçimde düşünmez. Basitleştirilmiş bir öğrenme modeli şöyle gösterilebilir:

$$T(n) = T_{min} + (T_0 - T_{min})e^{-kn}$$

Burada $T(n)$, $n$ tekrar sonrasındaki işlem süresi; $T_0$ başlangıç süresi, $T_{min}$ ulaşılabilecek alt sınır ve $k$ öğrenme hızıdır. Yeterli tekrar sonrasında komut, zihinsel bir problem olmaktan çıkarak parmakların bildiği bir harekete dönüşür.

| Özellik | Vim’e yeni başlayan | Deneyimli Vim kullanıcısı |
|---|---|---|
| Komut kullanımı | Bilinçli olarak hatırlar | Kas belleğiyle uygular |
| Modal yapı | Kafa karıştırıcıdır | Düzenleme dilidir |
| Yapılandırma | Ek iş gibi görünür | Kişisel yatırım sayılır |
| Araç değişimi | Kolay görünebilir | Akışı bozan maliyettir |

## Alışkanlık döngüsü ve anlık ödül

Psikolojide alışkanlıklar çoğunlukla **tetikleyici, davranış ve ödül** döngüsüyle açıklanır. Vim’de tetikleyici, düzenlenmesi gereken metindir. Davranış kısa bir komut dizisidir; ödül ise değişikliğin anında ve zarif biçimde gerçekleşmesidir. Özellikle karmaşık bir düzenlemeyi birkaç tuşla tamamlamak küçük ama güçlü bir yeterlilik hissi verir.

Aşağıdaki komut, geçerli satırdaki ilk `foo` ifadesini `bar` ile değiştirir:

```vim
:s/foo/bar/
```

Bu yalnızca kısa bir komut değildir. Kullanıcıya “Metni ben kontrol ediyorum” hissi veren hızlı bir geri bildirim mekanizmasıdır. Benzer ödüller tekrarlandıkça araç kullanımı otomatikleşir.

## Emek, sahiplik ve batık maliyet

Vim kullanıcıları genellikle kendi yapılandırmalarını yıllar içinde geliştirir. Örneğin şu ayarlar satır numaralarını açar ve aramayı yazarken sonuçları gösterir:

```vim
set number
set incsearch
set ignorecase
set smartcase
```

Bu dosya büyüdükçe editör, fabrikadan çıkmış standart bir araç olmaktan uzaklaşır; kullanıcının tercihlerini taşıyan kişisel bir çalışma ortamına dönüşür. **IKEA etkisi**, insanların emek verdikleri şeylere daha fazla değer biçtiğini söyler. Batık maliyet yanılgısı da geçmişte harcanan zamanın gelecekteki tercihler üzerinde gereğinden fazla etkili olabileceğini açıklar.

Ancak her bağlılık irrasyonel değildir. Araç değiştirme maliyeti kabaca şöyle düşünülebilir:

$$M = E + Y + A$$

Burada $E$ eğitim süresi, $Y$ yeni yapılandırma emeği, $A$ ise geçiş sırasında yaşanan akış kaybıdır. Vim becerisi yüksek biri için bu toplam gerçekten büyük olabilir.

## Araçtan kimliğe

“Vim kullanıyorum” ifadesi zamanla “Ben klavye odaklı, sistemleri anlayan ve araçlarını özelleştiren bir programcıyım” mesajına dönüşebilir. Topluluk şakaları, `.vimrc` paylaşımları ve editör tartışmaları bu kimliği pekiştirir. Sosyal kimlik kuramına göre insanlar ait oldukları gruplardan benlik değerinin bir kısmını elde eder. Vim topluluğu da ortak bir jargon ve ustalık ölçütleri sunar.

Sorun, araç tercihi ahlaki üstünlük yarışına dönüştüğünde başlar. Vim kullanmak disiplinin garantisi olmadığı gibi başka bir editör kullanmak da teknik yetersizlik değildir. Sağlıklı bağlılık, aracın işe hizmet etmesidir; bağımlılık ise işin aracı savunmaya hizmet etmeye başlamasıdır.

Sonuçta bazı programcılar Vim’i bırakamaz çünkü yalnızca bir editörü değil, yıllarca geliştirdikleri hareket hafızasını, kişisel çalışma alanını ve mesleki benliklerinin küçük bir parçasını bırakmaları gerekir. Çıkmak için `:q` yeterli olabilir; fakat psikolojik olarak çıkış komutu biraz daha uzundur.
