---
layout: post
title: "Dotfiles Kültürü: .bashrc Dosyanız Dijital Kişiliğinizi Ele Verir mi?"
math: true
categories: 
  - Bilgi
tags: 
  - dotfiles
  - bashrc
  - linux
  - geliştirici kültürü
  - kişiselleştirme
---

Bir geliştiricinin bilgisayarına kısa süreliğine oturduğunuzda, terminal açılır açılmaz karakteri hakkında ipuçları toplamaya başlarsınız: rengârenk bir prompt, dikkatle seçilmiş takma adlar, sessizce çalışan araçlar ve belki de yıllardır taşınan bir ASCII sanat eseri. Dotfiles — `.bashrc`, `.zshrc`, `.gitconfig`, `vimrc` ve benzerleri — yalnızca ayar deposu değildir; çalışma alışkanlıklarının, estetik tercihlerin ve teknik dünya görüşünün küçük bir arşividir.
``

Elbette bir `.bashrc` dosyasından insanın tüm kişiliğini çıkarmak bilimsel bir karakter analizi değildir. Ancak bu dosya, kullanıcının bilgisayarla nasıl ilişki kurduğunu gösterir. Terminali yalnızca komut yazılan bir araç olarak gören biriyle, onu kişisel bir çalışma stüdyosuna dönüştüren biri aynı yapılandırmayı yazmaz. Dotfiles kültürünün çekiciliği de burada başlar: Tekrarlanan işleri azaltırken kişinin dijital ortamına bir imza atmasına izin verir.

## Dotfiles neden kimlik ifadesidir?

Yapılandırma dosyaları çoğu zaman görünmez emek içerir. Bir geliştirici, her yeni makinede aynı ortamı kurmak istemez; bu nedenle tercihlerini sürüm kontrolüne alır. Böylece dotfiles, taşınabilir bir alışkanlık setine dönüşür. Basitçe şöyle düşünebiliriz:

$$\text{Verimlilik} = \frac{\text{Sık yapılan iş sayısı} \times \text{Kısalan süre}}{\text{Yapılandırma bakım maliyeti}}$$

Bu formül kesin bir ölçüm değildir, fakat önemli bir gerilimi anlatır: Her alias zaman kazandırmaz; bazen unutulmuş kısayollar ve karmaşık koşullar bakım maliyetini büyütür. İyi bir `.bashrc`, kişiselleştirme ile anlaşılabilirlik arasındaki dengedir.

| `.bashrc` tercihi | Olası çalışma tarzı | Dikkat edilmesi gereken nokta |
|---|---|---|
| Az sayıda alias | Açıklık ve standart araçlara bağlılık | Tekrarlayan uzun komutlar yorabilir |
| Git odaklı kısayollar | Sık commit alan, akış odaklı çalışma | Kısayollar ekip komutlarını gizleyebilir |
| Renkli, bilgi dolu prompt | Durumsal farkındalık ve görsel düzen | Çok fazla bilgi terminali yorar |
| Fonksiyon koleksiyonu | Otomasyon merakı | Fonksiyonlar belgelenmezse unutulur |
| Minimal dosya | Taşınabilirlik ve düşük bakım | Kişisel hız avantajları sınırlı kalabilir |

Örneğin `ll` alias'ı neredeyse evrensel bir alışkanlıktır; fakat `gs`, `gp`, `kctx` gibi kısaltmalar kullanıcının araç ekosistemini ele verir. Git, Docker, Kubernetes veya Node.js etrafında dönen komutlar, hangi problemlerin günlük hayatın merkezinde olduğunu gösterir. Prompt içindeki aktif Git dalı ise yalnızca şık bir detay değil, bağlam değiştirme maliyetini azaltan bir arayüz tercihidir.

## Kişisellik ile sürdürülebilirlik arasında

Aşağıdaki örnek, gösterişli olmaktan çok okunabilir kalmayı hedefleyen orta düzey bir `.bashrc` parçasıdır:

```bash
# Geçmişteki tekrarları azaltır ve oturumlar arasında paylaşır.
HISTCONTROL=ignoreboth:erasedups
HISTSIZE=10000
shopt -s histappend

# Sık kullanılan komutları daha güvenli ve kısa hale getirir.
alias ll='ls -lah --color=auto'
alias gs='git status -sb'
alias ..='cd ..'

# Proje klasörüne geçip editörü açan küçük bir iş akışı fonksiyonu.
workon() {
  local project="$HOME/projects/$1"
  [ -d "$project" ] || { echo "Proje bulunamadı: $1"; return 1; }
  cd "$project" && code .
}

# Prompt, klasörü ve Git dalını gösterir.
parse_git_branch() {
  git branch --show-current 2>/dev/null
}
PS1='\u@\h:\W [$(parse_git_branch)]\$ '
```

Burada alias'lar tekrar eden komutları kısaltır, `workon` ise küçük bir ritüeli otomatikleştirir. Buna karşılık her satırın bir bedeli vardır: `code` komutu her makinede bulunmayabilir, Git sorgusu çok büyük depolarda prompt'u yavaşlatabilir. Bu yüzden dotfiles yazmak biraz da ürün geliştirmektir: Kullanıcısı sizsiniz, ama gelecekteki siz de bakım ekibidir.

Sağlıklı dotfiles kültürünün temel ilkesi paylaşılabilir kişiselliktir. Gizli anahtarları dosyaya koymamak, makineye özgü ayarları ayrı tutmak, açıklama satırları eklemek ve Git ile sürümlemek bu kültürü olgunlaştırır. `.bashrc` dosyanız kişiliğinizi tamamen ele vermez; ama hangi sürtünmeleri ortadan kaldırmak istediğinizi, hangi araçlara güvendiğinizi ve dijital masanızı nasıl düzenlediğinizi gayet samimi biçimde anlatır.
