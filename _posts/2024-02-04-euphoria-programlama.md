---
title:  Euphoria Programlama
author: sonsuz
date: 2024-02-04 01:26:15 +0300
categories: [Program]
tags: [euphoria,programlama,farklı,dil]
---


## Değişkenler

### İnteger

Bu değişken tipi değerleri sayı olarak tanımlar. Örnek:

```
 integer x=25
```

### Object

Bu tip değişenler herhangi bir formda tanımlanabilir. Örneğin:

```
 object a,b,c
a={ }
b= a
c= 0
```

### Constant

Bu değişken tipi asla değişemeyen bir başlangıç değeri atar. Örnek:

```
 constant max=100
 constant isimler = {"Tolga", "Ersan", "Polat"}
```

### Enum

Numaralandırılmış değer(enum), ilk değerin varsayılan olarak 1 rakamına ayarlandığı ve bundan sonraki her öğenin varsayılan olarak 1 artırıldığı özel bir sabit türüdür. Artış değerini değiştirmek için isteğe bağlı bir anahtar kelimeye göre sağlanabilir. Örneğin:

```
 enum bir, iki, üç, dört          - “bir”= 1, “iki”= 2, “üç”= 3, “dört”= 4
enum bir, iki, üç, a=10, b, c
    - bir= 1, iki= 2, üç= 3
    - a= 10, c= 11, b= 12
```

## Sequence

Bu değişken tipi içine dizinleriyle ulaşabileceğimiz sıralı değerler atayabildiğimiz bir dizi oluşturur. Sequence kullanılan bir örnek:

```
 procedure baz(sequence s, integer n=length(s))
     ? n     -Soru işareti print gibi çalışır.
 end procedure
 baz("abcd")     - 4 yazdırılır.
```

Bu örnekte dizi fonksiyonun içine gönderilen değeri dizinlere ayırıp, kolayca uzunluğunu ölçmek için kullanılmış.

## Giriş-Çıkış Fonksiyonları

### Print

Euphoriada basit bir print fonksiyonu şu şekildedir:

` print( STUDOUT , ”65” )`

Burada parantezin içindeki ilk parametre bir tamsayı, çıktı alınacak bir dosyanın veya aygıtın tanıtıcısıdır, ikinci parametre de yazdırılacak nesnedir. Çıktı 65 olacaktır. Başka bir örnek:

```
  include std/io.e
 print( STDOUT ,  repeat( {10,20} , 3) )     - Çıktı şu şekilde olacak: {10,20}, {10,20}, {10,20}
```

### Printf

Printf fonksiyonu C’deki printf’e benzer ve print’te gördüğümüz gibi ilk başta bir tamsayı, çıktı alınacak bir dosyanın veya aygıtın tanıtıcısı olan bir parametre yer alır. İkinci parametre olan format bir dizi, yazdırılacak metindir bu parametre format belirleyicileri içerebilir. Üçüncüsü ise genellikle bir değerler dizisidir, bu değerler belirticilerin yerine geçeceğinden, formattaki format belirticilerin sayısı kadar öğeye sahip olmalıdır. Temel format belirteçleri şunlardır: 

```
%d -- bir değeri ondalık tamsayı olarak yazdırır.
%x -- bir değeri onaltılık tamsayı olarak yazdırır. Negatif sayılar ikinin tümleyeni şeklinde yazdırılır; dolayısıyla -1, FFFFFFFF olarak yazdırılır.
%o -- bir değeri sekizlik bir tamsayı olarak yazdırır.
%s -- bir diziyi bir karakter dizisi olarak yazdırır veya bir değeri tek bir karakter olarak yazdırır.
%e -- bir değeri üstel gösterimle ondalık sayı olarak yazdırır.
%f -- bir değeri ondalık sayı ancak üssüz bir ondalık sayı olarak yazdırır.
%g -- sayının büyüklüğü göz önüne alındığında, uygun görünen formatı kullanarak bir ondalık sayı olarak yazdırır.
%% -- '%' karakterinin kendisini yazdırır. Bu tam olarak bir biçim belirtici değildir.
```

Örnek:

```
 include std/io.e
name="Ufuk Aksoy"
printf( STDOUT, "Benim adım %s", {name})     - Çıktı şu şekildedir: Benim adım Ufuk Aksoy
```

Başka bir örnek:

```
 include std/io.e
printf( STDOUT, "%d  %e  %f  %g", repeat(7.75, 4)) 
                  (aynı değer ama farklı formatlarda)

- Çıktı şu şekilde:   7   7.750000e+000   7.750000   7.75
```

### Puts

Puts fonksiyonu bir dosyaya veya aygıta tek bir bayt (atom) veya bayt dizisi çıktısı verir. Aslında her değerin düşük dereceli 8 biti gönderilir. Ekrana çıktı veriyorsanız metin karakterlerinin görüntülendiğini göreceksiniz. 

Puts fonksiyonu iki parametre alır, ilki bir tam sayı, açık bir dosyanın veya aygıtın tanıtıcısıdır, ikincisi ise metin, tek bir karakter veya bir karakter dizisi olan bir nesnedir. Örnekler:

```
 include std/io.e
puts( SCREEN, "Adınızı girin:  ")

A=65
puts( output, 'A')      - Tek baytlık olan “65” çıktıya gönderilir.
```

## Gets

Gets fonksiyonu bir dosya veya aygıttan sonraki karakter dizisini ('\n' dahil bir satır) alır. Tek parametresi vardır, bir tamsayı, okunacak dosyanın veya aygıtın tanıtıcısını alır.

Dönüşler:

Dosyanın sonundaki EOF veya dosyadaki metnin bir sonraki satırı olan bir nesne şeklindedir.

Örnek:

```
object sıra

puts(1, "Adınız nedir?\n")
sıra = gets(0)       - standart girişi oku (klavye)
sıra = sıra[1..$-1]     - sondaki \n karakterinden kurtulun
puts(1, '\n')     - gerekli
puts(1, sıra & " güzel bir ad.\n")

```

## Karşılaştırma İfadeleri

### İf

Bir if ifadesi, bir koşulun doğru mu yanlış mı olduğunu görmek için test eder ve ardından bu testin sonucuna bağlı olarak uygun ifadeler kümesini çalıştırır. Örnekler:

```
 if a < b then          -eğer a, bden küçükse:
    x = 1
end if

if a = 9 and find(0, s) then     -eğer anın değeri dokuzsa ve 0,s bulunuyorsa:
    x = 4
    y = 5
else             -else if ifadelerinde eğer bu if içerisindeki hiçbir şart sağlanmıyorsa çalışır.
    z = 8
end if

if char = 'a' then
    x = 1
elsif char = 'b' or char = 'B' then 
    x = 2
elsif char = 'c' then            -elsif kendinden önceki hiçbir ifade doğru değilse çalışır.
    x = 3
else
    x = -1
end if
```

## Döngüler

### While

While döngüsünde bir koşulun sıfırdan farklı (doğru) olup olmadığını görmek için test edelir ve eğer öyleyse, bir dizi ifade yürütülür. İfadeler çalıştırıldıktan sonra koşul yeniden test edilir ve eğer hala doğruysa ifadeler yeniden çalıştırılır ve bu şekilde devam eder.

Örnek:

```
 while x > 0 do   -x değeri sıfırdan büyük olduğu sürece:
    a = a * 2       -a’yı önceki değerinin iki katına çıkar
    x = x – 1       -x’i öncekinden bir eksilt
end while       -döngüyü bitir.
```

### Loop – until

Bu döngü ifadesi, bir koşulun sıfırdan farklı (doğru) olup olmadığını görmek için test eder ve doğru olana kadar bir döngü yürütülür. Örneğin:

```
 loop do
    a = a * 2
    x = x - 1           -while’daki örneğin aynısının loop-until döngüsüne uyarlanışı.
    until x<=0 
end loop
```

### For

Bir for ifadesi, kendi döngü değişkenine sahip özel bir döngü oluşturur. Döngü değişkeni belirtilen başlangıç değeriyle başlar ve onu belirtilen son değere kadar artırır veya azaltır. For ifadesi, bir dizi ifadeyi belirli sayıda tekrarlamanız gerektiğinde kullanılır. Örnek:

```
   - Ekranda 1'den 6'ya kadar sayıları görüntülemek istiyorsunuz.
puts(1, "1\n")
puts(1, "2\n")
puts(1, "3\n")
puts(1, "4\n")
puts(1, "5\n")
puts(1, "6\n")
```

Bu kod bloğu ilk satırdan başlar ve her birini sırayla çalıştırır. Ancak bir for döngüsü kullanılarak daha basit ve esnek bir şekilde yazılabilir:

```
 for i = 1 to 6 do
     printf(1, "%d\n", i)
 end for
```

### Kaynakça

openeuphoria.org
