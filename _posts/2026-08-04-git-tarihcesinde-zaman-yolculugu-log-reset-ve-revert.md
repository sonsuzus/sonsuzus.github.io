---
layout: post
title: "Git Tarihçesinde Zaman Yolculuğu: Log, Reset ve Revert"
math: true
categories: 
  - Bilgi
tags: 
  - Git
  - Versiyon Kontrolü
  - Hata Yönetimi
---

Bir Git deposunun geçmişi, projenin nasıl geliştiğini anlatan dijital bir seyir defteridir. Her commit; yapılan değişiklikleri, değişikliği yapan kişiyi ve önceki duruma giden bağlantıyı saklar. Yanlış bir commit oluşturduğumuzda paniğe kapılmak yerine bu kayıtları okuyabilir, ardından `reset` veya `revert` ile güvenli bir zaman yolculuğuna çıkabiliriz.

``

## Git geçmişinin teorik yapısı

Git commit’leri yalnızca sıralı kayıtlar değildir. Her commit, kendisinden önce gelen commit’in kimliğini taşıyan bir düğümdür. Basitleştirilmiş bir geçmiş şöyle gösterilebilir:

```text
A <- B <- C <- D
               ^
              HEAD
```

Burada `HEAD`, üzerinde çalıştığımız dalın güncel commit’ini işaret eder. Bir commit kimliği; içerik, yazar, zaman ve üst commit bilgileri kullanılarak üretilen bir özettir. Kavramsal olarak bunu şöyle düşünebiliriz:

$$CommitID = Hash(içerik + yazar + zaman + parent)$$

Bu yapı sayesinde geçmişteki bir commit değiştirilirse onu izleyen kimlikler de değişir. Bu nedenle yayımlanmış geçmişi yeniden yazmak ekip çalışmalarında risklidir.

## Geçmişi `git log` ile okumak

İlk inceleme aracımız `git log` komutudur:

```bash
git log
```

Bu komut commit kimliklerini, yazarları, tarihleri ve mesajları gösterir. Daha okunabilir bir görünüm için şu sürüm oldukça kullanışlıdır:

```bash
git log --oneline --graph --decorate --all
```

Buradaki `--oneline` kayıtları kısaltır, `--graph` dallanmaları görselleştirir, `--decorate` dal ve etiket adlarını ekler. Belirli bir dosyanın geçmişini incelemek için ise şunu kullanabiliriz:

```bash
git log --oneline -- src/app.js
```

Commit’in hangi değişiklikleri yaptığını görmek için `git show <commit-id>` kullanılabilir. Böylece geri alma kararı vermeden önce “Suçlu gerçekten bu commit mi?” sorusunu yanıtlarız.

## Reset mi, revert mü?

İki komut da geri dönüş sağlar fakat yöntemleri farklıdır:

| Komut | Geçmişi yeniden yazar mı? | Yeni commit üretir mi? | Uygun kullanım |
|---|---:|---:|---|
| `reset --soft` | Evet | Hayır | Commit’i silip değişiklikleri staged tutmak |
| `reset --mixed` | Evet | Hayır | Değişiklikleri çalışma alanında bırakmak |
| `reset --hard` | Evet | Hayır | Yerel değişiklikleri tamamen atmak |
| `revert` | Hayır | Evet | Paylaşılmış commit’i güvenle geri almak |

### Reset ile işaretçiyi taşımak

Son commit mesajı veya içeriği yanlışsa ve henüz uzak depoya gönderilmediyse şu komut kullanılabilir:

```bash
git reset --soft HEAD~1
```

`HEAD~1`, güncel commit’in bir önceki atasını ifade eder. Commit kaldırılır ancak değişiklikler staging alanında kalır; böylece düzenleyip yeniden commit oluşturabiliriz.

```bash
git reset --hard HEAD~1
```

Bu sürüm hem commit’i hem de dosya değişikliklerini siler. Kaydedilmemiş çalışmalar açısından oldukça tehlikelidir. Kısacası `--hard`, Git dünyasının “Emin misin?” diye iki kez sormamız gereken kırmızı düğmesidir.

## Revert ile güvenli geri alma

Hatalı commit uzak depoya gönderildiyse geçmişi değiştirmek yerine ters değişiklik oluşturan yeni bir commit eklemek daha güvenlidir:

```bash
git revert a1b2c3d
```

Geçmiş başlangıçta $A \rightarrow B \rightarrow C$ ise ve `C` geri alınırsa sonuç $A \rightarrow B \rightarrow C \rightarrow C^{-1}$ olur. Yani `C` kaybolmaz; etkisini tersine çeviren kayıt eklenir. Bu yaklaşım denetlenebilirliği korur ve ekip arkadaşlarının geçmişiyle çatışmaz.

## Yanlış reset yaptıysak ne olacak?

Git çoğu zaman kaçış kapısını açık bırakır. `reflog`, `HEAD` işaretçisinin önceki konumlarını gösterir:

```bash
git reflog
git reset --hard HEAD@{1}
```

İkinci komut, uygun kayıt seçildiğinde bizi reset öncesindeki konuma döndürebilir. Yine de reflog kalıcı bir yedek değildir.

Pratik kural basittir: Önce `log` ve `show` ile incele, paylaşılmamış geçmişte dikkatli biçimde `reset`, paylaşılmış geçmişte ise çoğunlukla `revert` kullan. Komutu çalıştırmadan önce `git status` kontrolü yapmak da zaman makinesine emniyet kemeri takmak gibidir.
