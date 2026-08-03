---
layout: post
title: "Git Merge ve Conflict Çözümü: Dalları Birleştirme Sanatı"
math: true
categories: 
  - Bilgi
tags: 
  - Git
  - Merge
  - Conflict
---

Yazılım ekiplerinde herkes aynı dosyaya sırayla dokunsaydı hayat kolay, geliştirme süreci ise epey yavaş olurdu. Git dalları sayesinde geliştiriciler paralel çalışabilir; ancak bu çalışmaların eninde sonunda yeniden buluşması gerekir. `merge`, farklı dallardaki değişiklikleri ortak bir geçmişte birleştirirken conflict çözümü Git'in karar veremediği noktalarda insan muhakemesini devreye sokar.
``
## Merge Mantığı: İki Geçmiş, Tek Sonuç

Bir dal, belirli bir commit'ten başlayan bağımsız geliştirme çizgisidir. Örneğin `main` üretime hazır kodu taşırken `feature/login` yeni giriş ekranını içerebilir. Özellik tamamlandığında hedefimiz, feature dalındaki commit'leri `main` dalına aktarmaktır.

Commit geçmişini yönlü bir grafik gibi düşünebiliriz. Her commit bir düğüm, ebeveyn bağlantıları ise kenardır. İki dalın ortak atasını $B$, dal uçlarını $M$ ve $F$ olarak gösterirsek üç yönlü birleştirme şu değişimleri karşılaştırır:

$$\Delta_M = M - B \qquad \Delta_F = F - B$$

Git, $\Delta_M$ ile $\Delta_F$ değişikliklerini uyumlu biçimde uygulayabiliyorsa merge otomatik tamamlanır. Aynı bölge farklı şekillerde değiştirilmişse karar kullanıcıya bırakılır.

| Birleştirme türü | Ne zaman oluşur? | Sonuç |
|---|---|---|
| Fast-forward | Hedef dalda yeni commit yoksa | Dal işaretçisi ileri taşınır |
| Three-way merge | Her iki dal da ilerlediyse | Yeni bir merge commit'i oluşur |
| Conflict | Aynı içerik uyumsuz değiştirildiyse | Manuel çözüm gerekir |

## Temel Bir Merge İşlemi

Önce hedef dala geçilir, güncel durum alınır ve kaynak dal birleştirilir:

```bash
git switch main
git pull origin main
git merge feature/login
```

Burada önemli ayrıntı şudur: `feature/login`, içinde bulunduğumuz `main` dalına eklenir. Git temiz bir birleştirme yaparsa işlem tamamdır. Takım politikasına göre dal daha sonra silinebilir:

```bash
git branch -d feature/login
```

## Conflict Neden Oluşur?

Diyelim ki iki geliştirici aynı fonksiyonun dönüş mesajını değiştirdi. Git hangi mesajın iş kuralını doğru temsil ettiğini bilemez. Dosyada şu işaretleri bırakır:

```text
<<<<<<< HEAD
return "Ana daldaki mesaj";
=======
return "Özellik dalındaki mesaj";
>>>>>>> feature/login
```

`<<<<<<< HEAD` mevcut dalın, `>>>>>>> feature/login` ise birleştirilen dalın içeriğini gösterir. Ortadaki `=======` iki sürümü ayırır. Çözüm, işaretleri silip doğru nihai kodu oluşturmaktır; seçeneklerden birini körü körüne seçmek zorunlu değildir.

Örneğin iki fikri birleştiren sonuç şöyle olabilir:

```javascript
function loginMessage(username) {
  return `Hoş geldin ${username}, giriş başarılı!`;
}
```

Ardından çözüm Git'e bildirilir:

```bash
git add src/login.js
git commit -m "Resolve login message conflict"
```

Tüm çakışmaları görmek için `git status`, yapılan düzenlemeyi incelemek için `git diff` kullanılabilir. Yanlış yola girildiyse `git merge --abort`, çalışma alanını merge öncesi duruma döndürür.

## Güvenli Çözüm Stratejisi

Conflict çözmek yalnızca sözdizimini düzeltmek değildir; iki değişikliğin niyetini anlamaktır. Önce çakışan commit'leri ve ilgili gereksinimleri inceleyin. Ardından küçük parçalar hâlinde düzenleme yapın, testleri çalıştırın ve davranışın korunduğunu doğrulayın.

| Riskli yaklaşım | Güvenli yaklaşım |
|---|---|
| Tüm incoming değişiklikleri seçmek | Her bloğun amacını değerlendirmek |
| Test etmeden commit atmak | Birim ve entegrasyon testlerini çalıştırmak |
| Devasa dalları geç birleştirmek | Küçük ve sık merge yapmak |
| Conflict işaretlerini unutmak | `git diff --check` ile doğrulamak |

Son olarak merge commit'ini uzak depoya göndermeden önce uygulamayı derlemek ve test paketini çalıştırmak gerekir. Unutmayın: Git satırları birleştirir, fakat ürün davranışının doğru olup olmadığına karar veremez. Başarılı conflict çözümü; araç bilgisi, iletişim ve biraz da kod dedektifliği gerektirir.
