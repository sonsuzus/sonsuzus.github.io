---
layout: post
title: "TypeScript Kurulumu ve VS Code ile Çalışma Ortamı Hazırlama"
math: true
categories: 
  - Program
tags: 
  - TypeScript
  - Node.js
  - VS Code
---

JavaScript projelerine tür güvenliği, daha güçlü editör desteği ve erken hata yakalama yeteneği kazandırmak istiyorsanız TypeScript harika bir başlangıç noktasıdır. Bu rehberde TypeScript derleyicisini Node.js üzerinden kuracak, temel yapılandırmayı gerçekleştirecek ve hazırladığımız çalışma ortamını VS Code içinde küçük bir örnekle sınayacağız.

``

## TypeScript Aslında Ne Yapar?

TypeScript, JavaScript’in üzerine statik tür sistemi ekleyen bir programlama dilidir. Tarayıcılar ve Node.js, TypeScript kodunu doğrudan çalıştırmaz. Bu nedenle `.ts` uzantılı dosyalar, TypeScript derleyicisi anlamına gelen `tsc` tarafından JavaScript’e dönüştürülür.

Bu dönüşümü basitçe şöyle gösterebiliriz:

$$TypeScript\ Kaynak\ Kodu \xrightarrow{tsc} JavaScript\ Çıktısı$$

Derleme sırasında türler kontrol edilir ve daha sonra silinir. Başka bir ifadeyle TypeScript’in tür sistemi geliştirme zamanında çalışır; ortaya çıkan JavaScript dosyasında tür açıklamaları bulunmaz.

| Özellik | JavaScript | TypeScript |
|---|---|---|
| Tür kontrolü | Çalışma zamanında ağırlıklı | Derleme zamanında |
| Dosya uzantısı | `.js` | `.ts` |
| Tarayıcıda doğrudan çalışma | Evet | Hayır |
| Editör desteği | İyi | Çok güçlü |
| Derleme gereksinimi | Genellikle yok | Var |

Teorik olarak bir fonksiyonun beklediği tür $T$, gönderilen değerin türü $G$ olsun. Güvenli bir çağrı için temel beklenti $G \subseteq T$ biçiminde düşünülebilir. Uyumsuzluk varsa derleyici henüz programı çalıştırmadan bizi uyarır.

## Node.js ve Proje Kurulumu

Öncelikle Node.js’in güncel LTS sürümünü resmi sitesinden kurun. Kurulumla birlikte paket yöneticisi `npm` de bilgisayarınıza gelir. Terminalde doğrulama yapabilirsiniz:

```bash
node --version
npm --version
```

Ardından proje klasörünü oluşturup bir Node.js projesi başlatalım:

```bash
mkdir typescript-baslangic
cd typescript-baslangic
npm init -y
npm install --save-dev typescript
```

Burada TypeScript’i global olarak değil, projeye özel bir geliştirme bağımlılığı şeklinde kurduk. Böylece farklı projeler farklı derleyici sürümlerini kullanabilir. Kurulumu doğrulamak için şu komutu çalıştırın:

```bash
npx tsc --version
```

`npx`, projenin `node_modules` klasöründeki yerel TypeScript derleyicisini bulup çalıştırır.

## tsconfig.json Yapılandırması

TypeScript yapılandırma dosyasını otomatik oluşturabiliriz:

```bash
npx tsc --init
```

Başlangıç için dosyayı daha sade bir içerikle düzenleyelim:

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "CommonJS",
    "rootDir": "src",
    "outDir": "dist",
    "strict": true,
    "esModuleInterop": true
  },
  "include": ["src/**/*.ts"]
}
```

`rootDir`, kaynak kodların yerini; `outDir` ise üretilen JavaScript dosyalarının hedefini belirtir. `strict`, daha kapsamlı tür denetimlerini etkinleştirir. `target` seçeneği de üretilecek JavaScript’in dil seviyesini belirler.

## VS Code Ortamını Hazırlama

Proje klasörünü VS Code ile açın:

```bash
code .
```

VS Code, TypeScript desteğini yerleşik olarak sunar. İsterseniz ESLint ve Prettier eklentilerini de kurarak kod kalitesi ile biçimlendirmeyi otomatikleştirebilirsiniz. Şimdi `src/index.ts` dosyasını oluşturalım:

```typescript
type Kullanici = {
  ad: string;
  puan: number;
};

function seviyeHesapla(kullanici: Kullanici): string {
  return kullanici.puan >= 100 ? "Usta" : "Çırak";
}

const yazilimci: Kullanici = {
  ad: "Ada",
  puan: 120
};

console.log(`${yazilimci.ad}: ${seviyeHesapla(yazilimci)}`);
```

Bu örnekte `Kullanici` türü nesnenin sözleşmesini tanımlar. `puan` alanına yanlışlıkla metin verirseniz VS Code, daha derleme yapmadan kırmızı bir uyarı gösterecektir.

Projeyi derleyip çalıştırmak için:

```bash
npx tsc
node dist/index.js
```

Terminalde `Ada: Usta` çıktısını görüyorsanız zincirin tamamı çalışıyor demektir: VS Code kodu analiz etti, `tsc` türleri denetleyip JavaScript üretti ve Node.js sonucu çalıştırdı. Artık daha büyük TypeScript maceralarına hazırsınız!
