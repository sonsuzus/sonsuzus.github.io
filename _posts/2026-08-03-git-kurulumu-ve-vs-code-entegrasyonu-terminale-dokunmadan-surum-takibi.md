---
layout: post
title: "Git Kurulumu ve VS Code Entegrasyonu: Terminale Dokunmadan Sürüm Takibi"
math: true
categories: 
  - Bilgi
tags: 
  - Git
  - VS Code
  - Versiyon Kontrolü
---

Kod yazarken çalışan bir özelliği yanlışlıkla bozmak, çoğu geliştiricinin yaşadığı küçük çaplı bir korku filmidir. Git, projenin değişim geçmişini kaydederek bu filmi mutlu sonla bitirir. VS Code entegrasyonu sayesinde dosya değişikliklerini görmek, commit oluşturmak ve uzak depoya göndermek için terminal komutlarını ezberlemek de gerekmez.
``
## Git neyi çözer?

Git, **dağıtık versiyon kontrol sistemi**dir. Projenin yalnızca son durumunu değil, belirli zamanlarda kaydedilen sürümlerini de saklar. Her geliştiricide deponun geçmişini içeren yerel bir kopya bulunur. Böylece internet bağlantısı olmadan commit oluşturulabilir ve geçmiş incelenebilir.

Bir dosyanın Git içindeki yolculuğu üç temel alandan geçer:

| Alan | Anlamı | VS Code karşılığı |
|---|---|---|
| Working Directory | Üzerinde çalışılan güncel dosyalar | Editörde değiştirdiğiniz dosyalar |
| Staging Area | Sonraki commit için seçilen değişiklikler | **Changes** listesindeki `+` işlemi |
| Repository | Kalıcı olarak kaydedilmiş geçmiş | Oluşturulan commit kayıtları |

Bir commit, projenin tamamının gelişigüzel kopyası değildir. Git içerikleri nesneler ve referanslar üzerinden verimli biçimde izler. Basitleştirilmiş olarak bir commit’i şöyle düşünebiliriz:

$$C_n = H(D_n + C_{n-1} + M_n)$$

Burada $D_n$ dosya durumunu, $C_{n-1}$ önceki commit’i, $M_n$ açıklama ve yazar gibi meta verileri, $H$ ise özetleme fonksiyonunu temsil eder. Bu bağlantılı yapı geçmişin tutarlı biçimde takip edilmesini sağlar.

## Git kurulumu

Windows kullanıcıları Git’i [git-scm.com](https://git-scm.com/) üzerinden indirebilir. Kurulum sihirbazındaki varsayılan seçenekler çoğu kullanıcı için uygundur. macOS üzerinde resmi yükleyici veya Homebrew, Linux üzerinde ise dağıtımın paket yöneticisi kullanılabilir.

```bash
# macOS
brew install git

# Ubuntu ve Debian
sudo apt update
sudo apt install git
```

Kurulumdan sonra kullanıcı bilgileri bir kez yapılandırılır. Bu bilgiler commit’lerin kime ait olduğunu belirtir:

```bash
git config --global user.name 'Ada Geliştirici'
git config --global user.email 'ada@example.com'
```

Terminal kullanmak istemiyorsanız bu ayarları VS Code içindeki **Settings** ekranından `git config` aramasıyla veya Git istemcisinin kurulum aşamasında belirleyebilirsiniz. Kurulumu doğrulamak için VS Code’u yeniden başlatmak önemlidir.

## VS Code ile depo oluşturma

Proje klasörünü VS Code’da açın ve sol kenar çubuğundaki dallanma simgesine, yani **Source Control** görünümüne tıklayın. Klasör henüz Git tarafından izlenmiyorsa **Initialize Repository** düğmesi görünür. Bu düğme, klasörde gizli bir `.git` dizini oluşturarak yerel depoyu hazırlar.

Bir dosyayı değiştirdiğinizde **Changes** bölümünde listelenir. Dosyaya tıklamak, eski ve yeni hâli yan yana gösteren karşılaştırma ekranını açar. Satırların anlamı oldukça görseldir:

| Görünüm | Anlamı |
|---|---|
| Yeşil satırlar | Eklenen içerik |
| Kırmızı satırlar | Silinen içerik |
| Mavi işaretler | Değiştirilen bölge |
| `U` rozeti | Henüz izlenmeyen dosya |
| `M` rozeti | Değiştirilmiş dosya |

Commit’e eklenecek dosyanın yanındaki `+` simgesine basarak dosyayı **Staged Changes** alanına taşıyın. Üstteki kutuya `Kullanıcı giriş ekranını ekle` gibi açıklayıcı bir mesaj yazın ve **Commit** düğmesine basın. İyi bir commit tek bir mantıksal değişikliği kapsamalıdır; yüz farklı işi aynı pakete doldurmak, gelecekteki size bırakılmış bir bilmece olur.

## GitHub ile eşitleme

VS Code’daki **Publish Branch** veya **Publish to GitHub** seçeneği, yerel depoyu GitHub’a göndermeyi kolaylaştırır. İlk kullanımda tarayıcı üzerinden GitHub hesabına giriş izni istenir. Sonrasında **Sync Changes** düğmesi iki işlemi yönetir:

- **Push:** Yerel commit’leri uzak depoya gönderir.
- **Pull:** Uzak depodaki yeni commit’leri bilgisayara getirir.

Dallar arasında geçmek için pencerenin sol altındaki dal adına tıklayabilirsiniz. Yeni özellikleri ayrı bir dalda geliştirmek, ana sürümü korur. Çakışma oluşursa VS Code; mevcut değişikliği, gelen değişikliği veya ikisini birlikte kabul etme seçenekleri sunar.

Son olarak `.env`, parola, derleme çıktıları ve `node_modules` gibi gereksiz ya da gizli içerikleri `.gitignore` dosyasına ekleyin. Böylece görsel araçların rahatlığıyla güvenli ve düzenli bir sürüm geçmişi oluşturabilirsiniz.
