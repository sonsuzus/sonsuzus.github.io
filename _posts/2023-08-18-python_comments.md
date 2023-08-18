---
title:  Python Yorum satırları
author: sonsuz
date: 2023-08-18 15:53:42 +0300
categories: [Program,Python]
tags: [programlama,python,yorum]
---


Python'da, kodların açıklanması için yapılan yorumlar programın çalışmasına herhangi bir etki yapmaz ve hiç yazılmamış gibi işlem görür.

Yorum oluşturmak için, yorumun başında `#` işareti kullanılır. Bu işaret bir satır başında veya bir satırın sonunda kullanılabilir.

Tek ve çok satırdan oluşan yorum satırlarının kullanılmasını bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
# Program kodlarının başlangıcı

deg1 = 21 # Değişken bildirimi
deg2 = 17 # Değişken bildirimi

print(deg1+deg2) # değişkenleri toplama işlemi

str = "Bilgisayar"

# Karakter dizisi içindeki sabitleri
# birer birer ekrana yazar.
for deg in str:
    print(deg, end='') # end='' ifadesi yeni satıra geçiş yapmaması için


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

38
Bilgisayar

```
