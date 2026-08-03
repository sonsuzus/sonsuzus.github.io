---
layout: post
title: "Git Push ve Pull ile Senkronizasyon Akışı"
math: true
categories: 
  - Bilgi
tags: 
  - Git
  - GitHub
  - Sürüm Kontrolü
---

Bir ekip projesinde kod yazmak kadar, yazılan kodu doğru yere ve doğru zamanda ulaştırmak da önemlidir. Git’in **push** ve **pull** komutları, yerel bilgisayarımız ile GitHub, GitLab veya Bitbucket gibi uzak sunucular arasında köprü kurar. Biri tamamladığımız çalışmaları dışarı gönderirken diğeri ekip arkadaşlarımızın değişikliklerini içeri alır; yani biri kargoyu yollar, diğeri kapıda teslim alır.

``

## Yerel ve Uzak Depo Mantığı

Git ile çalışırken aslında birbirinden bağımsız iki depo bulunur:

- **Yerel depo (local repository):** Bilgisayarımızdaki proje geçmişidir.
- **Uzak depo (remote repository):** Ekibin ortak kullandığı sunucu kopyasıdır.

Dosyayı kaydetmek, değişikliği otomatik olarak uzak sunucuya göndermez. Önce değişiklik çalışma alanında oluşur, ardından `git add` ile hazırlama alanına alınır ve `git commit` ile yerel geçmişe kaydedilir. Ancak bundan sonra `git push` kullanılarak uzak depoya aktarılabilir.

Bu akışı basitçe şöyle gösterebiliriz:

$$Çalışma\ Alanı \rightarrow Staging \rightarrow Yerel\ Depo \rightarrow Uzak\ Depo$$

Senkronizasyon durumunu kabaca bir fark denklemiyle de düşünebiliriz:

$$Fark = Yerel\ Commit\ Sayısı - Uzak\ Commit\ Sayısı$$

$Fark > 0$ ise gönderilecek yerel commit’lerimiz vardır. $Fark < 0$ ise uzak depoda henüz almadığımız güncellemeler bulunabilir. Gerçekte Git yalnızca sayıları değil, commit’ler arasındaki yönlü geçmiş ilişkisini inceler.

## Push ve Pull Karşılaştırması

| Özellik | `git push` | `git pull` |
|---|---|---|
| Veri yönü | Yerelden uzağa | Uzaktan yerele |
| Temel amaç | Commit’leri paylaşmak | Güncellemeleri almak |
| Geçmişe etkisi | Uzak dalı ilerletir | Yerel dalı birleştirir |
| Olası sorun | Push reddedilebilir | Birleştirme çakışması oluşabilir |
| Güvenli alışkanlık | Önce pull yapmak | Değişiklikleri kontrol etmek |

## Değişiklikleri Uzak Sunucuya Göndermek

Aşağıdaki komutlar tamamlanan bir özelliği kaydeder ve `main` dalına gönderir:

```bash
git status
git add .
git commit -m "Kullanıcı profil ekranını ekle"
git push origin main
```

`git status`, hangi dosyaların değiştiğini gösterir. `git add .`, değişiklikleri hazırlama alanına taşır. `git commit`, bu aşamanın yerel anlık görüntüsünü oluşturur. Son komuttaki `origin`, uzak deponun yaygın takma adı; `main` ise gönderilecek daldır.

İlk gönderimde dalın takip ilişkisini kurmak gerekebilir:

```bash
git push -u origin feature/profil
```

`-u` seçeneği yerel dalı uzak dalla ilişkilendirir. Sonraki işlemlerde yalnızca `git push` yazmak çoğunlukla yeterli olur.

## Güncellemeleri Çalışma Alanına Çekmek

Ekip arkadaşımız uzak depoya yeni commit gönderdiyse bunları şu şekilde alabiliriz:

```bash
git switch main
git pull origin main
```

`git pull`, perde arkasında iki işi birlikte gerçekleştirir:

$$git\ pull = git\ fetch + git\ merge$$

Önce `fetch` uzak geçmişi indirir, ardından `merge` bu geçmişi mevcut dalımızla birleştirir. Süreci daha kontrollü yürütmek isteyenler iki adımı ayrı çalıştırabilir:

```bash
git fetch origin
git log --oneline main..origin/main
git merge origin/main
```

Buradaki `git log`, uzakta bulunan fakat yerel `main` dalında olmayan commit’leri gösterir. Böylece neyi birleştirdiğimizi önceden görebiliriz.

## Çakışmalar ve Sağlıklı Akış

Aynı dosyanın aynı satırları iki kişi tarafından değiştirilmişse Git hangi sürümün doğru olduğuna karar veremez ve **conflict** oluşturur. Çakışmalı bölümler elle düzenlenir, test edilir ve yeniden commit edilir:

```bash
git add duzeltilen-dosya.js
git commit -m "Birleştirme çakışmasını çöz"
git push
```

Sağlıklı bir ekip akışında güne `git pull` ile başlamak, küçük ve anlamlı commit’ler oluşturmak, push öncesinde testleri çalıştırmak ve doğrudan `main` yerine özellik dalları kullanmak faydalıdır. Kısacası **pull dinlemeyi, push konuşmayı temsil eder**. İyi bir Git kullanıcısı ise yalnızca konuşmaz; önce ekibin en güncel hâlini dinler.
