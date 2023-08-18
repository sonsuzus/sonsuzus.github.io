---
title: Python Karakter dizileri
author: sonsuz
date: 2023-08-18 16:27:16 +0300
categories: [Program,Python]
tags: [python,programlama,karakter,dizi,dize,string]
---



## Karakter dizileri hakkında

Karakter dizisi sabitleri tırnak işaretleri arasına yerleştirilen karakter dizileri ile oluşturulur. Tek tırnak (' ') veya çift tırnak (" ") işaretleri kullanılabilir.

Bir karakter dizisi sabitini doğrudan veya bir değişkene atadıktan sonra ekrana yazabiliriz.

Şimdi, bu özellikleri bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
print('Bilgisayar') # Karakter dizisini doğrudan ekrana yazma
print('Yazılım') # Karakter dizisini doğrudan ekrana yazma

str1 = 'Python' # Karakter dizisini değişkene atama
str2 = "Programlama" # Karakter dizisini değişkene atama

print(str1) # Karakter dizisini değişkenler yoluyla ekrana yazma
print(str2) # Karakter dizisini değişkenler yoluyla ekrana yazma


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Bilgisayar
Yazılım
Python
Programlama

```

## Çok satırlı karakter dizileri

Bir değişkene birden fazla satırdan oluşan karakter dizisi sabiti atamak için 3 adet tekli veya çiftli tırnak işareti kullanabiliriz. Şimdi, bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
str1 = """Bilgisayar yazılım geliştirme
Python Proglama Dili
Karakter dizisi sabitleri"""

str2 = """Bilgisayar yazılım geliştirme
Python Proglama Dili
Karakter dizisi sabitleri"""

print(str1) 
print(str2) 


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Bilgisayar yazılım geliştirme
Python Proglama Dili
Karakter dizisi sabitleri
Bilgisayar yazılım geliştirme
Python Proglama Dili
Karakter dizisi sabitleri

```

## Tek bir karaktere erişim

Bir karakter dizisi içindeki tek bir karaktere erişim sağlamak için, köşeli parantezler içinde, ilk karakter sıfırdan başlamak üzere, endeks değeri kullanılır. Elde edilecek değer tek karakter uzunluğunda bir karakter dizisi sabiti olacaktır. Şimdi, bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
str = "Bilgisayar"

print(str[0]) # 1.karaktere erişim sağlar. 
print(str[5]) # 6.karaktere erişim sağlar.


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

B
s

```

## Karakter dizisini teker teker yazdırma

Bir karakter dizisi içindeki karakterleri birer birer yazdırmak için döngü kullanabiliriz. Şimdi, bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
str = "Bilgisayar"

# Karakter dizisini tek seferde ekrana yazar.
print(str)

# Karakter dizisi içindeki sabitleri birer birer ekrana yazar.
for deg in str:
    print(deg, end='') # end='' ifadesi yeni satıra geçiş yapmaması için


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

Bilgisayar
Bilgisayar

```

## Karakter dizisinin uzunluğunu alma

Bir karakter dizisinin uzunluğunu ölçmek için len fonksiyonunu kullanabiliriz. Şimdi, bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
str = "Bilgisayar"

print(len(str))


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

10

```

## Karakter dizisi içinde karakter veya karakter dizisi arama

Bir karakter dizisi içinde karakter veya karakter dizisinin bulunup bulunmadığını belirlemek için ve in not in anahtar kelimelerini kullanabiliriz. Şimdi, bu özelliği bir örnek üzerinde incelemeye çalışalım:

Örnek

```py
str = "Bilgisayar yazılım geliştirme"

print("yazılım" in str) # "yazılım" karakter dizisi str içinde olduğundan True değeri verir.
print("programlama" in str) # "programlama" karakter dizisi str içinde olmadığından False değeri verir.

print("")

print("programlama" not in str) # "programlama" karakter dizisi str içinde olmadığından True değeri verir.


```

Yukarıdaki programı derleyip çalıştırdığımızda, aşağıdaki ifadeleri ekrana yazar:

```

True
False

True

```
