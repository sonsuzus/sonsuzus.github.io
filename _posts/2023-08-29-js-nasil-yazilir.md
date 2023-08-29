---
title: Javascript Nasıl Yazılır?
author: sonsuz
date: 2023-08-29 23:32:08 +0300
categories: [Program,Javascript]
tags: [javascript,programlama,ders,js]
---



Daha önce bahsettiğimiz gibi **Javascript** bir programlama dili ve çalıştırılabilmesi için bir **Javascript derleyicisi**ne ihtiyaç duyar.

Yazdığımız bir Javascript kodunu çalıştırabilmek için ya bir tarayıcıya ihtiyacımız var, "çünkü Javascript derleyicisi tarayıcı içinde zaten mevcut" ya da nodejs derleyicine ihtiyacımız var.

Şu aşamada **nodejs** kullanmayacağız dolayısıyla her yazdığımız javascript kodunu çalıştırabilmek için bir html sayfasına ihtiyaç duyacağız.

Editörümüzde bir **index.html** dosyası oluşturup aşağıdaki **html iskeleti**ni ekleyelim.

**Visual Studio code** editöründe kolay bir şekilde html iskeleti oluşturmak için **ünlem(!)** işaretinden sonra **2 kere tab** tuşuna tıklamanız gerekiyor.

```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <meta http-equiv="X-UA-Compatible" content="ie=edge">

    <title>Document</title>

</head>

<body>    

</body>

</html>
```

Daha sonra index.html dosyanız ile aynı dizinde (klasörde) **script.js** isimli bir başka dosya daha oluşturalım ve ardından index.html dosyamız ile script.js dosyamızı birbirine bağlayalım ki; index.html dosyasını tarayıcıda açtığımızda script.js dosyasına dolaylı olarak çalıştırılmış olsun.

```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <meta http-equiv="X-UA-Compatible" content="ie=edge">

    <title>Modern Javascript Kursu</title>

</head>

<body>



    <h1 id="header">

         Modern Javascript Kursu: ES6/ES7+ (2019)

    </h1>



    <script  src="script.js" type="text/Javascript"></script>

</body>

</html>
```

* yukarıda html sayfamız içerisine bir **h1** etiketi ekledik ve id="header" tanımlamasını yaptık. 

* script etikenin **src** özelliğine **script.js** dosyasını ekledik ve artık index.html dosyası ile script.js dosyası birbirine bağlanmış oldu.

Özetle html sayfasını tarayıcıda açtığımız anda script.js dosyasındaki kodlar da çalıştırılacak ve tarayıcı içinde bulunan Javascript derleyicisi javascript kodlarımız için bir hata denetimi yaptıktan sonra eğer hata yoksa kodları çalıştıracaktır.

Peki script.js dosyamız içerisine bir kaç basit javascript kodu ekleyelim.

```js
console.log("Merhaba")

console.log(5+10)
```

burada console' a Merhaba ve 10+5 sonucunu yazdırıyoruz. Peki console nerede ? Yani program çıktılarını nerede görebilirim.

Chrome tarayıcısını açıp F12 ye bastığımızda geliştirici araçları paneli açılacaktır. Geliştirici araçları panelinin console segmesinde Merhaba ve 15 değerlerini görüyor olmalısınız.

![Chrome geliştirici araçları](chrome-gelistirme-araclari.png)

```js
document.getElementById("header").innerHTML = "Hello JavaScript";
```

Burada ise html dökümanı içinde id değeri header olan etiketi bulup içerisine Hello Javascript kelimelerini ekliyoruz. Yani sayfa yüklendiği anda artık h1 etiketleri içindeki yazı güncellenecektir.

```js
document.getElementById("header").style.fontSize = "35px";
```

Burada ise id' si header olan yani h1 etiketini seçer ve h1 etiketinin font büyüklüğünü 35px yapar.

Özetle Javascript kullanarak html dökümanı içerisindeki her hangi bir etikete ulaşıp içerisindeki içerikleri değiştirip farklı css kodları aktarabiliyoruz.
