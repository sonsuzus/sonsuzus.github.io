---
layout: post
title: "TypeScript Felsefesi: JavaScript Dünyasında Statik Tip Güvenliği"
math: true
categories: 
  - Bilgi
tags: 
  - TypeScript
  - JavaScript
  - Statik Tipler
---

JavaScript, geliştiriciye büyük bir hareket özgürlüğü sunar; ancak bu özgürlük bazen üretim ortamında patlayan küçük sürpriz paketlerine dönüşebilir. TypeScript’in temel felsefesi, JavaScript’in esnekliğini ortadan kaldırmak değil, program çalışmadan önce olası hataları görünür hâle getiren bir düşünme katmanı eklemektir. C ve C++ dünyasındaki statik tip denetimini anımsatan bu yaklaşım, dinamik web ekosistemine daha güvenli ve ölçeklenebilir bir geliştirme modeli kazandırır.
``

## Statik ve dinamik tip sistemleri

Bir değişkenin hangi değerleri taşıyabileceği, programlama dilinin tip sistemi tarafından belirlenir. C++ gibi statik tipli bir dilde değişkenin tipi derleme sırasında bilinir ve uygunsuz işlemler reddedilir. JavaScript’te ise tip, değişkenden çok çalışma anındaki değere aittir.

```javascript
let value = 10;
value = "on";
console.log(value * 2); // NaN
```

Bu kod JavaScript açısından geçerlidir. Sorun ancak işlem çalıştırıldığında ortaya çıkar. TypeScript aynı belirsizliği derleme aşamasına taşır:

```typescript
let value: number = 10;
value = "on"; // Hata: string, number tipine atanamaz
```

Buradaki amaç programı yavaşlatan çalışma zamanı kontrolleri eklemek değildir. TypeScript tipleri JavaScript çıktısı üretilirken siler. Başka bir ifadeyle tip sistemi, çalışan programın değil, program hakkındaki bilgimizin parçasıdır.

| Özellik | JavaScript | TypeScript | C/C++ |
|---|---|---|---|
| Tip denetimi | Çalışma zamanında ağırlıklı | Derleme zamanında | Derleme zamanında |
| Tip açıklaması | Zorunlu değil | İsteğe bağlı ve çıkarımlı | Genellikle açık |
| Çıktı | Doğrudan çalışır | JavaScript’e çevrilir | Makine koduna derlenir |
| Bellek güvenliği | Motor tarafından yönetilir | JavaScript ile aynı | Geliştiricinin sorumluluğu olabilir |
| Mevcut kodla uyum | Doğal | Kademeli geçiş destekler | Sınırlı |

## Tip güvenliğinin teorik anlamı

Bir tip, olası değerler kümesi olarak düşünülebilir. Örneğin `number` tipi $N$ değer kümesini, `string` tipi ise $S$ kümesini temsil etsin. Bir fonksiyonun imzası şöyle modellenebilir:

$$f: N \rightarrow N$$

Bu ifade, fonksiyonun sayı kabul edip sayı ürettiğini söyler. Fonksiyona $x \in S$ verilmesi, tanımlanan sözleşmenin ihlalidir. TypeScript derleyicisi bu ihlali program çalışmadan yakalamaya çalışır.

```typescript
function double(input: number): number {
  return input * 2;
}

double(21);     // 42
double("21");   // Derleme hatası
```

Bu garanti mutlak değildir. Ağdan gelen JSON, kullanıcı girdisi veya yanlış kullanılan `any`, derleyicinin bilgisini aşabilir. Dolayısıyla TypeScript’in güvenliği, yalnızca ispatlayabildiği sınırlar içinde geçerlidir.

## Yapısal tipleme: İsim değil, biçim önemlidir

C++ çoğunlukla bildirilen tip kimliğine önem verirken TypeScript yapısal tipleme kullanır. Bir nesne gerekli alanlara sahipse ilgili tipe uyumlu kabul edilir. Bu yaklaşım JavaScript’in ördek tipleme geleneğiyle uyumludur: Ördek gibi görünüyorsa ve yüzüyorsa, büyük olasılıkla ördektir.

```typescript
interface User {
  id: number;
  name: string;
}

const customer = {
  id: 7,
  name: "Ada",
  premium: true
};

function greet(user: User): string {
  return `Merhaba ${user.name}`;
}

greet(customer);
```

`customer`, açıkça `User` olarak tanımlanmamasına rağmen gerekli yapıyı taşır. Böylece katı güvenlik ile JavaScript’in nesne esnekliği arasında kullanışlı bir denge kurulur.

## Tip çıkarımı ve daraltma

TypeScript her değişkene açıklama yazılmasını istemez. `const score = 100` ifadesinden tipin `number` olduğunu çıkarabilir. Birleşim tiplerinde ise kontrol akışını analiz ederek olasılıkları daraltır:

```typescript
function format(value: string | number): string {
  if (typeof value === "number") {
    return value.toFixed(2);
  }

  return value.trim();
}
```

Bu davranış, tip sistemini yalnızca yasak koyan bir bekçi olmaktan çıkarıp kodu anlayan bir asistana dönüştürür. Editör otomatik tamamlama sunar, yeniden adlandırma işlemleri güvenilirleşir ve API sözleşmeleri belgelenebilir hâle gelir.

Sonuç olarak TypeScript, JavaScript’e C++ kostümü giydirmez. Bellek modeli, çalışma ortamı ve dinamik nesne yapısı hâlâ JavaScript’e aittir. TypeScript’in yaptığı şey, esnek bir dilin üzerine derleme zamanlı bir mantık ağı sermektir. Bu ağ tüm hataları yakalayamaz; fakat büyük projelerde yanlış varsayımları erkenden göstererek hata maliyetini ciddi ölçüde azaltır.
