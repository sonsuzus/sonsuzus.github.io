---
layout: post
title: "IDE'lerde Çoklu Dil Mimarisi: Tek Çalışma Alanında Backend, Betik ve Önyüz Senfonisi"
math: true
categories: 
  - Bilgi
tags: 
  - IDE
  - LSP
  - çoklu dil mimarisi
  - otomasyon
  - frontend
---

Modern bir IDE artık sadece renkli parantez gösteren bir metin editörü değil; adeta küçük bir yazılım işletim sistemi. Aynı çalışma alanında TypeScript ile önyüz geliştirirken, Python betikleriyle otomasyon çalıştırabilir, Go ya da Java servislerini debug edebilir ve tüm bu parçaları tek bir proje akışı gibi yönetebilirsiniz. Çoklu dil mimarisi tam da burada devreye girer: IDE, farklı dillerin araçlarını ortak bir orkestrada buluşturur.
``
Bu mimarinin kalbinde şu fikir vardır: IDE her dili doğrudan kendi içinde yeniden icat etmez; bunun yerine dil sunucuları, hata ayıklama adaptörleri, görev çalıştırıcıları ve eklentilerle konuşur. Yani editör kısmı kullanıcı arayüzüdür, zeka ise çoğunlukla arka plandaki servislerden gelir. Bu ayrım sayesinde aynı ekranda React bileşeni yazarken, arka planda veritabanı migrasyonu hazırlayan bir betik de çalışabilir.

Teorik olarak sistemi şu denklemle düşünebiliriz: $IDE = Editör + LSP + DAP + TaskRunner + Eklenti$. Burada LSP, Language Server Protocol yani dil sunucusu protokolüdür. Kod tamamlama, sembole gitme, hata işaretleme gibi özellikleri sağlar. DAP, Debug Adapter Protocol ile hata ayıklama dünyasını standartlaştırır. TaskRunner ise derleme, test, lint ve deploy gibi komutları yönetir.

| Bileşen | Görevi | Örnek kullanım |
|---|---|---|
| LSP | Dil zekası sağlar | TypeScript hatalarını anlık gösterme |
| DAP | Debug sürecini soyutlar | Python betiğinde breakpoint kullanma |
| Task Runner | Komutları otomatik çalıştırır | npm test ve pytest zinciri |
| Eklenti Sistemi | IDE davranışını genişletir | Docker, Git, Kubernetes paneli |

Çoklu dil çalışma alanında önemli kavramlardan biri bağımlılık grafiğidir. Diyelim ki önyüz projesi API tiplerini otomatik üretilen bir dosyadan alıyor. Bu durumda $frontend \rightarrow generatedTypes \rightarrow backendSchema$ şeklinde bir ilişki oluşur. IDE bu ilişkiyi görevlerle temsil ederse, geliştirici tek tuşla önce şemayı güncelleyip sonra önyüzü başlatabilir.

```ts
type Task = { name: string; run: () => Promise<void> };

const tasks: Task[] = [
  { name: 'api:generate', run: async () => console.log('OpenAPI tipleri üretildi') },
  { name: 'frontend:lint', run: async () => console.log('Önyüz kontrol edildi') },
  { name: 'frontend:dev', run: async () => console.log('Vite geliştirme sunucusu açıldı') }
];

async function runPipeline() {
  for (const task of tasks) {
    console.log('Çalışıyor:', task.name);
    await task.run();
  }
}

runPipeline();
```

Bu kod basit bir görev hattını temsil eder. Gerçek IDE içinde bu yapı çoğu zaman launch, tasks veya workspace ayarlarıyla tanımlanır. Ama mantık aynıdır: görevler sıraya alınır, çıktılar terminalde toplanır, hata olursa zincir durdurulur ya da kullanıcı uyarılır.

| Yaklaşım | Avantaj | Risk |
|---|---|---|
| Tek dil, tek proje | Basit kurulum | Büyük sistemlerde yetersiz kalır |
| Çoklu dil, ayrı klasörler | Sorumluluklar netleşir | Araçlar kopuk çalışabilir |
| Çoklu dil, tek workspace | Entegre deneyim | Doğru yapılandırma ister |

Gelişmiş IDE'lerde bu entegrasyonun eğlenceli kısmı otomasyondur. Örneğin dosya kaydedildiğinde formatter çalışır, testler tetiklenir, tip dosyaları yenilenir ve önyüz sıcak yenileme ile güncellenir. Kullanıcı sadece kod yazar; IDE sahne arkasında küçük bir robot ordusu gibi çalışır. Ancak bu robot ordusunun kontrolden çıkmaması için net kurallar gerekir: görev adları anlamlı olmalı, ortam değişkenleri belgelenmeli, her dilin bağımlılık yönetimi izole edilmelidir.

Pratikte iyi bir çoklu dil IDE mimarisi için üç öneri öne çıkar. Birincisi, her teknolojinin kendi doğal aracını kullanın; Python için venv, Node için pnpm veya npm, Java için Maven gibi. İkincisi, ortak akışları IDE görevlerine bağlayın. Üçüncüsü, debug yapılandırmalarını ekip içinde paylaşın. Böylece yeni gelen geliştirici projeyi klonladığında sadece kodu değil, çalışma ritüelini de devralır.

Sonuç olarak çoklu dil mimarisi, IDE'yi pasif bir editörden aktif bir geliştirme merkezine dönüştürür. Arka plandaki otomasyon betikleri, önyüz projeleri ve servisler aynı sahnede buluştuğunda üretkenlik artar. Doğru kurgulanmış bir workspace, geliştiriciye şu hissi verir: Farklı diller konuşan bir ekip var, ama hepsi aynı orkestrada çalıyor.
