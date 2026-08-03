---
layout: post
title: "Git Temelleri: Değişiklikleri Anlamlı Commit’lerle Kaydetmek"
math: true
categories: 
  - Bilgi
tags: 
  - Git
  - Versiyon Kontrolü
  - Commit
---

Bir projede kod yazarken yalnızca sonucun çalışması yeterli değildir; hangi değişikliğin ne zaman ve neden yapıldığını da bilmek gerekir. Git, projenin belirli anlarını yerel bir tarihçeye kaydederek geçmişe bakmayı, hataları izlemeyi ve güvenle deney yapmayı sağlar. Commit ise bu tarihçedeki sıradan bir kayıt değil, projenin belirli bir andaki anlamlı fotoğrafıdır.
``
## Git’in temel yaklaşımı: Anlık fotoğraflar

Git çoğu zaman yalnızca satır satır farkları saklayan bir araç gibi düşünülür. Oysa temel modeli **snapshot**, yani anlık fotoğraf yaklaşımıdır. Commit oluşturulduğunda Git, izlenen dosyaların o andaki durumunu temsil eden bir kayıt üretir. Değişmeyen dosyalar için mevcut nesneler yeniden kullanılabildiğinden bu yöntem düşündüğünüzden daha verimlidir.

Her commit; proje ağacına, yazara, tarihe, açıklama mesajına ve genellikle bir önceki commit’e referans verir. Böylece commit’ler birbirine bağlanarak bir tarihçe oluşturur:

$$C_n = S_n + P(C_{n-1}) + M_n + A_n$$

Burada $S_n$ proje fotoğrafını, $P(C_{n-1})$ önceki commit referansını, $M_n$ mesajı ve $A_n$ yazar bilgilerini temsil eder. İçeriğin özeti alınarak commit kimliği üretilir. Bu nedenle geçmişteki bir kaydın içeriği değiştirilirse kimliği de değişir.

## Üç çalışma alanını anlamak

Git kullanımındaki karışıklıkların büyük bölümü çalışma dizini, staging area ve repository ayrımının bilinmemesinden kaynaklanır.

| Alan | Görevi | İlgili komut |
|---|---|---|
| Working Directory | Dosyaları düzenlediğiniz aktif alan | `git status` |
| Staging Area | Sonraki commit’e girecek değişikliklerin seçildiği alan | `git add` |
| Repository | Commit’lerin kalıcı yerel tarihçesi | `git commit` |

`git add`, değişikliği doğrudan tarihçeye kaydetmez. Yalnızca bir sonraki fotoğrafa hangi düzenlemelerin gireceğini belirler. Bu ara katman, aynı anda yaptığınız ilgisiz değişiklikleri ayrı commit’lere bölmenizi sağlar.

## İlk anlamlı commit akışı

Aşağıdaki komutlar yeni bir depo oluşturur, durumu inceler ve seçilen değişiklikleri kaydeder:

```bash
git init
git status
git add README.md src/app.js
git diff --staged
git commit -m "Kullanıcı giriş doğrulamasını ekle"
```

`git diff --staged`, commit oluşturulmadan önce sahnelenen içeriği gösterir. Bu küçük kontrol, yanlışlıkla şifre, geçici dosya veya ilgisiz kod kaydetme riskini azaltır. Commit sonrasında `git log --oneline` ile kısa tarihçe görüntülenebilir.

```bash
git log --oneline --decorate
git show HEAD
```

`git show HEAD`, son commit’in bilgilerini ve değişikliklerini incelemek için kullanılır. Buradaki `HEAD`, üzerinde çalıştığınız güncel commit’i işaret eder.

## İyi commit mesajı ne anlatır?

“Değişiklik yaptım” veya “son düzeltme” gibi mesajlar gelecekte kimseye yardımcı olmaz. İyi bir mesaj, kodda görülebilen ayrıntıyı tekrarlamak yerine değişikliğin amacını açıklar.

| Zayıf mesaj | Daha iyi mesaj |
|---|---|
| `güncelleme` | `Sepet toplamında indirim oranını uygula` |
| `bug fix` | `Boş e-postada oluşan doğrulama hatasını düzelt` |
| `kodlar eklendi` | `Siparişler için sayfalama desteği ekle` |

Mesajın emir kipinde, kısa ve odaklı olması okunabilirliği artırır. Büyük bir commit içinde özellik, biçimlendirme ve hata düzeltmesi karıştırmak yerine her mantıksal işi ayrı kaydetmek daha sağlıklıdır.

## Commit atmadan önce mini kontrol

Önce `git status` ile kapsamı, ardından `git diff` ile değişiklikleri inceleyin. İlgili testleri çalıştırın, yalnızca aynı amacı taşıyan dosyaları staging area’ya ekleyin ve “Bu commit neden var?” sorusunu cevaplayan bir mesaj yazın.

Commit’i bir yedekleme düğmesi değil, gelecekteki geliştiriciye bırakılan açıklamalı bir zaman kapsülü olarak düşünün. Küçük, çalışır ve anlamlı commit’ler; hata ayıklamayı, kod incelemeyi ve gerektiğinde güvenli biçimde geçmişe dönmeyi ciddi ölçüde kolaylaştırır.
