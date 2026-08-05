---
layout: post
title: "tsconfig.json Rehberi: TypeScript Derleyicisini Baştan Sona Yapılandırmak"
math: true
categories: 
  - Bilgi
tags: 
  - TypeScript
  - tsconfig
  - JavaScript
---

TypeScript kodu yazmak işin yalnızca yarısıdır; diğer yarısı, bu kodun hangi JavaScript sürümüne, hangi modül sistemine ve ne kadar katı kurallarla dönüştürüleceğini belirlemektir. Projenin kontrol paneli sayılan `tsconfig.json`, derleyiciye adeta “Bu kodu nereye götürüyoruz ve yolda hangi kurallara uyuyoruz?” sorularının cevabını verir.

``

## Derleme ve transpilation mantığı

TypeScript derleyicisi `tsc`, `.ts` ve `.tsx` dosyalarını inceler, tip hatalarını raporlar ve gerektiğinde çalıştırılabilir JavaScript üretir. Bu işlem çoğunlukla **transpilation** olarak adlandırılır. Çünkü kaynak ve hedef diller benzer soyutlama seviyelerindedir.

Basitleştirilmiş süreç şöyle gösterilebilir:

$$TypeScript + Derleyici\ Ayarları \longrightarrow JavaScript + Tip\ Kontrolü$$

Burada önemli bir ayrım vardır: TypeScript tipleri çalışma zamanında JavaScript içinde yaşamaz. Örneğin `number` veya `User` gibi tip tanımları çıktı oluşturulurken silinir. Dolayısıyla TypeScript, çalışma zamanı doğrulayıcısı değil, geliştirme zamanında çalışan bir güvenlik ağıdır.

## Temel tsconfig.json yapısı

Orta ölçekli bir Node.js projesi için başlangıç yapılandırması şöyle olabilir:

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "rootDir": "src",
    "outDir": "dist",
    "strict": true,
    "esModuleInterop": true,
    "sourceMap": true,
    "declaration": true,
    "skipLibCheck": true
  },
  "include": ["src/**/*.ts"],
  "exclude": ["node_modules", "dist"]
}
```

`rootDir`, kaynak kodun bulunduğu dizini; `outDir` ise üretilen JavaScript dosyalarının gideceği dizini belirtir. `include` derlemeye katılacak, `exclude` göz ardı edilecek dosyaları tanımlar. Böylece derleyici yanlışlıkla `dist` klasörünü tekrar derleyip dijital bir matruşka bebeğe dönüşmez.

## target, module ve moduleResolution

Bu üç ayar sıkça karıştırılır fakat farklı sorumluluklara sahiptir:

| Ayar | Görevi | Örnek değerler |
|---|---|---|
| `target` | Üretilecek JavaScript sürümünü belirler | `ES2018`, `ES2022`, `ESNext` |
| `module` | Çıktının modül biçimini seçer | `CommonJS`, `ESNext`, `NodeNext` |
| `moduleResolution` | Import yollarının nasıl çözüleceğini belirler | `Node`, `NodeNext`, `Bundler` |

Eski tarayıcıları desteklemek daha düşük bir `target` gerektirebilir. Ancak düşük hedef, daha fazla dönüşüm ve daha büyük çıktı anlamına gelebilir. Kabaca:

$$Uyumluluk \uparrow \Rightarrow Dönüşüm\ Maliyeti \uparrow$$

Modern Node.js projelerinde `ES2022` ve `NodeNext`; Vite gibi paketleyici kullanan uygulamalarda ise `ESNext` ile `Bundler` genellikle mantıklı tercihlerdir.

## strict modu neden önemlidir?

`strict: true`, birden fazla güvenlik seçeneğini topluca etkinleştirir. Bunların arasında `strictNullChecks`, `noImplicitAny` ve `strictFunctionTypes` bulunur.

```ts
function kullaniciAdi(ad: string | null): string {
  if (ad === null) {
    return "Misafir";
  }

  return ad.toUpperCase();
}
```

`strictNullChecks` açıkken `null`, sıradan bir `string` gibi kullanılamaz. Kod önce olası boş değeri kontrol eder. Bu yaklaşım biraz daha fazla kod yazdırsa da üretimdeki “undefined nereden geldi?” dedektifliğini ciddi biçimde azaltır.

| Yaklaşım | Avantaj | Risk |
|---|---|---|
| `strict: false` | Hızlı başlangıç | Hatalar çalışma zamanına sızabilir |
| `strict: true` | Güçlü tip güvenliği | Eski projelerde çok hata gösterebilir |
| Kademeli geçiş | Kontrollü iyileştirme | Geçici ayar karmaşası yaratabilir |

## Mimariye göre ek ayarlar

Kütüphane geliştiriyorsanız `declaration: true`, tüketiciler için `.d.ts` dosyaları üretir. Yalnızca tip kontrolü yapıp çıktıyı Babel, SWC veya Vite’a bırakacaksanız `noEmit: true` kullanılabilir. `sourceMap: true` ise çalışan JavaScript hatalarını özgün TypeScript satırlarıyla eşleştirerek hata ayıklamayı kolaylaştırır.

Paylaşılan yapılarda temel ayarları ayrı bir dosyada tutmak da mümkündür:

```json
{
  "extends": "./tsconfig.base.json",
  "compilerOptions": {
    "outDir": "dist/server"
  },
  "include": ["src/server/**/*.ts"]
}
```

Sonuç olarak iyi bir `tsconfig.json`, rastgele seçenekler koleksiyonu değil, projenin çalışma ortamını ve kalite beklentisini belgeleyen mimari bir sözleşmedir. Ayarları kopyalayıp geçmek yerine hedef platformu, modül sistemini ve dağıtım yöntemini düşünmek; daha anlaşılır, güvenli ve taşınabilir projeler üretir.
