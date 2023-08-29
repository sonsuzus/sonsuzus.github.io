---
title: Python Karakter Dizileri Strings ve Metotları
author: sonsuz
date: 2023-08-29 20:16:41 +0300
categories: [Program,Python]
tags: [python,programlama,karakter dizisi,string,dizi,dize,metot]
---

 



## Pythonda String Tanımlama

**Pythonda Karakter Dizileri** yani string veri tipleri **tek tırnak (' ')** ya da **çift tırnak (" ")** ile oluşturulur.

'Hello World' ile "Hello World" tanımlaması aynıdır. Ancak bazen karakter dizileri içerisinde tek tırnak karakterini karakter dizisinin bir elemanı gibi göstermek isteriz.

**"I'm from Turkey"** şeklinde tek tırnak karakterini tanımlayabilmek için mecburen çift tırnak kullanmamız gerekir çünkü **'I'm from Turkey'** bu şekilde bir kullanım hata verecektir.

## Birden Fazla Satırda String Tanımlama

**3 tırnak** ile birden fazla satırda string tanımlaması yapabilirsiniz. 3 tane tek tırnak ya da 3 tane çift tırnak kullanabilirsiniz.

```py
text = """Lorem ipsum dolor sit amet, 

consectetur adipiscing elit, sed do eiusmod 

tempor incididunt ut labore et dolore magna aliqua."""

print(text)


```

## String Birleştirme (String Concatenation)

Tanımladığımız string ifadeleri '+' operatörü ile birleştirebiliriz. Ancak string birleştirmede number değişkenleri str() ile string'e çevirmemiz gerekiyor.

```py
name = 'Sonsuz'

surname = 'Us'

age = 42

greeting = 'My name is '+ name + ' '+ surname + ' and \nI am '+ str(age) + ' years old.'

print(greeting)
```

Bu şekilde değişken içeriklerine göre bir string ifadeyi + operatörü ile oluşturmuş olduk ve age değişkeni number türünde olduğundan dolayı str(age) şeklinde string' e çevirdik.

## String Formatlama

'+' operatörünü kullanarak string birleştirme işlemi bazen zor olabiliyor. Dolayısıyla kullanabileceğimiz **format()** metodu ile **f-string** isminde iki farklı alternatifimiz mevcut.

### String format() Metodu

```py
name = 'Deniz'
surname = 'Şimşek'
age = 14
```

.format() metoduna vereceğimiz her parametre sırasıyla { }' lerin yerine kopyalanır. 

```py
print('My name is {} {}'.format(name, surname)) # My name is Deniz Şimşek
```

Gördüğünüz gibi birinci { }' in yerine Deniz ikinci { }' in yerine ise Şimşek yazdırılır.

```py
print('My name is {1} {0}'.format(name, surname))  
```

{ }' ler için indeks numarası da verebiliriz. Yani format metodu içindeki name, 0 ve surname, 1 değerlerini alır. 

```py
print('My name is {s} {n}'.format(n=name, s=surname))  
```

format() metodu içindeki değişkenlere takma isim de verebiliriz.

```py
print("My name is {} {} and I'm {} years old.".format(name, surname, age))
```

age 3. süslü parantezin yerine gelir ayrıca age number olduğundan dolayı format() metodunda str() fonksiyonunu kullanmamız gerekmez.

```py
print("My name is {} {} and I'm {} years old.".format(name, name, name))
```

format içine eklediğimiz 3 tane name değişkeni sırasıya süslü parantezler yerine gelir. Eğer ki tek name değerini 3 kere yazdırmak istersek, {0} şeklinde kullanabiliriz.

```py
print("My name is {0} {0} and I'm {0} years old.".format(name))
```

### f-String ile String Formatlama

f-string ile kolaylıkla string birleştirme işlemi yapabiliriz. Çünkü string ifadenin içinde süslü parantezler içinde değişkenleri yazabiliriz.

```py
print(f"My name is {name} {surname} and I'm {age} years old.")
```

## String Parçalama (String Slicing)

String veri tipleri bir karakter dizisi olarak anılır yani bir karakter listesi olarak tanımlanırlar. Dizilerin her bir karakterine soldan 0' dan başlayarak bir indeks numarası atanır. Atanan indeks numaraları dizi içerisindeki her bir elemana ulaşırken kullanılır.

```py
result = greeting[0] 

print(result)
```

gördüğünüz gibi greeting karakter dizisinin ilk elemanı soldan sağa doğru 0 indeks numarası ile başlar ve greeting[0] dediğimizde bize 0.indeksteki M karakteri gelir.

```py
result = greeting[3] 

print(result)  # n  
```

Pozitif indeks numarası soldan sağa 0'dan başlar negatif indeks numarası ise -1 ile sağdan başlar.

```py
result = greeting[-1] 

print(result)  # . 
```

greeting karakter dizisinin son elemanı "." karakteridir.

Karakter dizilerinin daha doğrusu dizilerin eleman sayısını **len()** metodu ile bulabiliriz.

```py
result = len(greeting)

print(result)
```

Dolayısıyla son elemanın indeks numarası toplam karakter sayısından 1 eksik olur. 

```py
result = greeting[len(greeting)-1] 

print(result)  # .


```

Bir karakter dizisini başlangıç ve bitiş aralığında istediğimiz şekilde bölebiliriz.

```py
result = greeting[3:7] 

print(result)  # name
```

3 indeksden başlayarak 7. indekse kadar olan karakterleri alıyoruz. Son indeks işin içine katılmıyor.

```py
result = greeting[:7] 

print(result)  # My name
```

Burada ise başlangıç indeksini belirtmediğimizden dolayı en başta başlar ve 7. indekse kadar gider.

```py
result = greeting[3:] 

print(result)
```

Burada ise başlangıç indeksi 3 ve bitiş indeksi belirtilmediğinden dolayı en sona kadar alınır.

```py
result = greeting[0:10:2]

print(result) 
```

Burada ise 0. indeksten 10. indekse kadar alınır ancak adım sayısı 2 olarak belirtildiğinden dolayı bir karakter alınır bir diğeri alınmaz.

**Adım sayısını soldan sağa doğru olduğuna dikkat ediniz.**

```py
result = greeting[0:10:1]

print(result)  # My name is 
```

Adım sayısı 1 olduğundan dolayı [0:10] ile gene aynı sonucu verir. Ancak adım sayısına pozitif değer yerine negatif değer verirsek bu durumda sağdan sola doğru ilerleriz.

Dolayısıyla karakterleri tersten yazdırmak istediğimizde aşağıdaki gibi sonuç alırız. [::] ile tüm karakter dizisini al ancak adım sayısı negatif olduğundan sağdan sola doğru birer birer ilerle. Dolayısıyla yazı tersten yazdırılmış olur.

```py
result = greeting[::-1]

print(result)
```

## Python String Uygulamaları

```py
website = "https://sonsuzus.github.io"

course = "Python Kursu: Baştan Sona Python Programlama"
```

1- 'course' karakter dizisinde kaç karakter bulunmaktadır ?

```py
length = len(course)

length = len(website)
```

2- 'website' içinden https karakterlerini alın.

3- 'website' içinden io karakterlerini alın.

```py
result = website[length-3:length]
```

4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.

```py
result = course[0:15]

result = course[:15]

result = course[-15:]
```

5- 'course' ifadesindeki karakterleri tersten yazdırın.

```py
result = course[::-1]
```

```
name, surname, age, job = 'Ada Su','Tetik', 15, 'öğrenci'
```

6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.

'Benim adım Ada Su Tetik, Yaşım 15 ve mesleğim öğrenci.'

```py
result = "Benim adım "+ name+ " " + surname+ ", Yaşım "+ str(age) + " ve mesleğim "+ job

result = "Benim adım {0} {1}, Yaşım {2} ve mesleğim {3}.".format(name,surname,age,job)

result = f'Benim adım {name} {surname}, Yaşım {age} ve "mesleğim" {job}.'
```

## Pythonda string metotları nelerdir ve nasıl kullanırız?

## Split Metodu

**Split** metodu, karakter dizisinde belirtilen bir karaktere göre parçalama işlemi yapar. 

```py
message = 'Hello, There.'

message = message.split(',')   # ['Hello',' There']
```

Karakter dizisini **','** karakterinden parçalara ayırır ve bize bir liste gönderir.

Split metoduna bir parametre göndermediğimizde ise, boşluk karakterinden parçalama yapılır.

```py
message = 'Hello, There.'

message = message.split()   # ['Hello,', 'There.']
```

## Upper Metodu

Upper metodu, karakterleri büyük harfe çevirir.

```py
message = 'Hello There.'

message = message.upper()  # HELLO THERE.
```

## Lower Metodu

Lower metodu, karakterleri büyük harfe çevirir.

```py
message = 'HELLO THERE.'

message = message.upper()  # Hello There.
```

**title() metodu,** karakter dizisindeki her kelimenin baş harfini büyük harfe çevirir.

**capitalize(),** karakter dizisindeki sadece ilk kelimenin baş harfini büyük harfe çevirir.

## Strip Metodu

Strip metodu, karakter dizisinin baş ve sondaki boşluk karakterlerini siler. 

```py
username = "     sonsuzus     "

x = username.strip()

print("my username is +  x")  # my username is sonsuzus
```

Eğer strip() metodunun belirttiğimiz karakterleri silmesini istersek bu karakteri parametre olarak göndermemiz gerekir.

```py
username = ",,,,...!!sonsuzus***"

x = username.strip(',.!*')

print("my username is +  x")  # my username is sonsuzus
```

## Replace Metodu

Replace metodu karakter güncellemesi için kullanılır. 

```py
message = 'My name is Sonsuz Us'

message = message.replace('Sonsuz','Sessiz')  # My name is Sessiz Us
```

replace() metotlarını ard arda kullanabiliriz. 

```py
url = url.replace(' ','-')
        .replace('@','') 
        .replace('ö','o')
        .replace('ü','u')
        .replace('ş,'s')
        .replace('ü','u')
```

şeklinde türkçe karakterleri, boşluk karakterlerini ve '@' işaretini url içinde güncelleyebiliriz. 

## Find Metodu

Find metodu verilen string ifade içinde arama yapar ve bulduğu ilk indeks numarasını döndürür. Eğer bulamazsa exception döndürür.

```py
txt = "My name is Sonsuz Us."

x = txt.find("name")

print(x)  # x = 3
```

name string içerisinde 3.indeks numarasından itibaren başladığından dolayı 3 değeri yazdırılır.

## Index Metodu

index metodu verilen string ifade içinde arama yapar ve bulduğu ilk indeks numarasını döndürür. Eğer bulamazsa find metodundan farklı olarak geriye -1 değerini döndürür.

```py
txt = "My name is Sonsuz Us."
x = txt.index("name")
print(x)  # x = 3
```

Eğer ki string içinde olmayan bir ifadeyi aratırsak geriye -1 döner.

```py
txt = "My name is Sonsuz Us."
x = txt.index("old")
print(x)  # x = -1
```

old, string içinde bulunmadığından dolayı -1 döner.

> Ayrıca index ve find metodu için bir arama kapsamı belirtebiliriz.

```py
index("aranılacak ifade", "başlangıç indeksi","bitiş indeksi")
```

```py
txt = "My name is Sonsuz Us."

x = txt.index("name",0,10)

print(x)  # x = 3
```

0 ile 10. indeks arasında bir arama yapılır.

## String Metot Uygulamaları

```py
website = "http://www.sadikturan.com"

course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"
```

1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.

```py
result = ' Hello World '.strip()     # baş ve sondaki boşluk karakterleri silinir.

result = ' Hello World '.lstrip()    # baştaki boşluk karakterleri silinir.

result = ' Hello World '.rstrip()    # sondaki boşluk karakterleri silinir.

result =   website.lstrip('/:pth')   # baştan itibaren '/:pth' karakteri silinir. result "www.sadikturan.com" değerini alır.
```

2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.

```py
result = 'www.sadikturan.com'.strip('w.moc')
```

3- 'course' karakter dizisinin tüm karakterlerini küçük harf yapın.

```py
result = course.lower() # küçük harfe çevrilir.

result = course.upper() # büyük harfe çevrilir.

result = course.title() # her kelimenin baş harfe büyük harfe çevrilir.
```

4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))

```py
result = website.count('a')         # a karakteri sayılır.

result = website.count('www')       # www karakterleri sayılır. 

result = website.count('www',0,10)  # 0 ile 10. indeks arasında www ifadesi sayılır.
```

5- 'website' "www" ile başlayıp com ile bitiyor mu?

```py
result = website.startswith('www')    # website www ile başlıyor mu ? False

result = website.startswith('http')   # website http ile başlıyor mu ? True

result = website.endswith('com')      # website com ile bitiyor mu ? True
```

6- 'website' içinde 'com' ifadesi var mı?

```py
result = website.find('com')          # website içerisinde 'com' ifadesini arar ve geriye 22 döner.

result = website.find('com',0,10)     # 0 ile 10 arasında com ifadesini bulamaz ve exception döndürür.

result = course.find('Python')        # 0.indeksten itibaren bulduğu ilk Python için 0 değeri döner.

result = course.rfind('Python')       # Aramaya sağdan başlayacağından dolayı 2. Python' i 26. indekste bulur.

result = website.index('com')         # website içerisinde 'com' ifadesini arar ve geriye 22 döner.

result = website.rindex('com')        # website içerisinde 'com' ifadesini arar ve geriye 22 döner.

result = website.rindex('comm')       # comm bulunamadığından "ValueError: substring not found" hatası gelir.


```

7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)

```py
result = course.isalpha()   # tüm karakterler alfabetik mi diye sorar ve False gelir.

result = 'Hello'.isalpha()  # tüm karakterler alfabetik olduğundan True gelir.

result = course.isdigit()   # tüm karakterler rakam mı diye sorar ve False gelir.

result = '123'.isdigit()    # tüm karakterler rakam mı diye sorar ve True gelir.
```

8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna \* ekleyiniz.

```py
result = 'Contents'.center(50, '*')    # **** Contents **** şeklinde toplam 50 karakter olur.

result = 'Contents'.ljust(50, '*')     # Contents ********* şeklinde toplam 50 karakter olur.

result = 'Contents'.rjust(50, '*')     # ********* Contents şeklinde toplam 50 karakter olur.
```

9- 'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.

```py
result = course.replace(' ', '-')    # tüm boşluk karakterleri '-' ile değiştirilir.

result = course.replace(' ', '-',5)  # ilk 5 boşluk karakterleri '-' ile değiştirilir.

result = course.replace(' ', '')     # tüm boşluk karakteri silinir.
```

10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin

```py
result = 'Hello World'.replace('World','There')
```

11- 'course' karakter dizisini boşluk karakterlerinden ayırın.

```py
result = course.split(' ')  # ['Python', 'Kursu:', 'Baştan', 'Sona', 'Python', 'Programlama', 'Rehberiniz', '(40', 'saat)']

result = result[2]          # 'Baştan'

result = result[5]          # 'Programlama'


```

split metodu ile string ifadeyi her boşluk karakterinden ayırıp bir listeye çevirmiş oluruz ve her bir liste elemanına indeks numarası ile ulaşabiliriz.

---
