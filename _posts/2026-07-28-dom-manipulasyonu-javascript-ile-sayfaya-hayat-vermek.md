---
layout: post
title: "DOM Manipülasyonu: JavaScript ile Sayfaya Hayat Vermek"
math: true
categories: 
  - Bilgi
tags: 
  - JavaScript
  - DOM
  - Web Geliştirme
---

Bir web sayfasındaki başlığın aniden değişmesi, yeni bir kartın listeye eklenmesi veya bir düğmeye basınca menünün açılması sihir değildir. Perdenin arkasında çoğunlukla JavaScript ve DOM birlikte çalışır. DOM, statik görünen HTML belgesini programlama yoluyla okunabilen ve değiştirilebilen canlı bir yapıya dönüştürür.
``
## DOM tam olarak nedir?

DOM, yani **Document Object Model**, tarayıcının HTML belgesini bellekte temsil etmek için oluşturduğu nesne modelidir. Tarayıcı HTML kodunu okur, etiketler arasındaki ebeveyn-çocuk ilişkilerini analiz eder ve hiyerarşik bir ağaç meydana getirir.

Örneğin aşağıdaki belgeyi düşünelim:

```html
<body>
  <main>
    <h1>Ürünler</h1>
    <ul id="liste">
      <li>Klavye</li>
    </ul>
  </main>
</body>
```

Bu yapıda `body`, `main` elemanının; `main` ise `h1` ve `ul` elemanlarının ebeveynidir. `li` düğümü de `ul` altında bulunur. DOM yalnızca etiketlerden oluşmaz: metinler, yorumlar ve belgenin kendisi de birer düğümdür.

Bir ağacın toplam düğüm sayısını basitçe $N = E + T + C$ biçiminde düşünebiliriz. Burada $E$ elemanları, $T$ metin düğümlerini, $C$ ise yorum düğümlerini temsil eder. Gerçek DOM modeli daha ayrıntılı olsa da bu yaklaşım yapının neden beklenenden kalabalık olabileceğini anlatır.

| Kavram | HTML tarafındaki anlamı | DOM tarafındaki karşılığı |
|---|---|---|
| Etiket | `<button>` | Element nesnesi |
| Metin | `Kaydet` | Text düğümü |
| İç içelik | Etiketlerin sıralanışı | Ebeveyn-çocuk ilişkisi |
| `id` | Benzersiz tanımlayıcı | Seçim için kullanılabilen özellik |
| Olay | HTML’de doğrudan görünmeyebilir | Tıklama, giriş veya gönderim sinyali |

## Elemanları seçmek ve değiştirmek

DOM manipülasyonunun ilk adımı hedefi bulmaktır. `querySelector`, CSS seçicilerini desteklediği için oldukça kullanışlıdır. `querySelectorAll` ise eşleşen bütün elemanları bir `NodeList` içinde döndürür.

```javascript
const baslik = document.querySelector("h1");
const liste = document.querySelector("#liste");

baslik.textContent = "Teknoloji Ürünleri";
baslik.classList.add("vurgulu");

const yeniUrun = document.createElement("li");
yeniUrun.textContent = "Mekanik Fare";
liste.appendChild(yeniUrun);
```

Bu kod önce başlığı ve listeyi bulur. Ardından başlığın güvenli biçimde metnini değiştirir, bir CSS sınıfı ekler ve bellekte yeni bir `li` üretip listeye bağlar. `textContent`, verilen değeri HTML olarak yorumlamadığı için kullanıcı kaynaklı içeriklerde genellikle `innerHTML` kullanımından daha güvenlidir.

| Yöntem | Kullanım amacı | Önemli nokta |
|---|---|---|
| `textContent` | Metin okuma veya yazma | HTML çalıştırmaz |
| `innerHTML` | HTML parçacığı ekleme | Güvenilmeyen veride risklidir |
| `classList` | CSS sınıflarını yönetme | `add`, `remove`, `toggle` sunar |
| `createElement` | Yeni eleman oluşturma | Önce bellekte hazırlanır |
| `appendChild` | Elemanı ağaca bağlama | Mevcut düğümü taşıyabilir |

## Olaylarla etkileşim kurmak

Dinamiklik yalnızca içerik değiştirmek değildir; kullanıcı davranışına tepki vermek de gerekir. Olay dinleyicileri tam bu noktada sahneye çıkar:

```javascript
const buton = document.querySelector("#urun-ekle");
let sayac = 1;

buton.addEventListener("click", () => {
  const eleman = document.createElement("li");
  eleman.textContent = `Yeni ürün ${sayac}`;
  liste.appendChild(eleman);
  sayac += 1;
});
```

Her tıklamada yeni bir liste elemanı oluşturulur. Böylece HTML dosyasını yeniden yüklemeden arayüz güncellenir. Olaylar genellikle hedef elemandan üst düğümlere doğru yayılır; bu davranışa **event bubbling** denir. Çok sayıda benzer eleman varsa her birine dinleyici eklemek yerine ortak ebeveyne tek dinleyici bağlamak, yani olay delegasyonu kullanmak daha verimli olabilir.

## Performans ve güvenlik

DOM işlemleri ücretsiz değildir. Çok sayıda değişiklik tarayıcının yerleşimi yeniden hesaplamasına neden olabilir. $n$ eleman üzerinde tek tek ve ağır işlemler yapmak yaklaşık $O(n)$ maliyet oluştururken, her adımda tüm ağacı yeniden taramak maliyeti büyütebilir. Eleman referanslarını saklamak, değişiklikleri gruplamak ve gerektiğinde `DocumentFragment` kullanmak daha akıcı arayüzler sağlar.

Sonuç olarak DOM, HTML ile JavaScript arasındaki köprüdür. Ağacı doğru okuyup güvenli yöntemlerle değiştirdiğinizde statik belgeler; filtrelenen listelere, açılır menülere ve etkileşimli uygulamalara dönüşür. Kısacası HTML sahneyse, DOM dekor düzeni; JavaScript ise dekoru hareket ettiren çalışkan sahne görevlisidir.
