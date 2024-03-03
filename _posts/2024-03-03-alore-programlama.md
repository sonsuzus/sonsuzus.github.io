## Alore 

Alore, kullanımı kolay ve hızlı bir dil olup, genel amaçlı bir
programlama dilidir. Bu makalede, Alore programlama dilinin temel
yapılarını, fonksiyonları, döngüleri ve değişkenleri anlamak için
detaylı bir bakış sunacağız. Ayrıca, Alore kodunu nasıl yazacağınızı ve
çalıştıracağınızı adım adım açıklayacağız.

Alora ile nasıl kod yazılacağına başlamadan önce bu kodları nasıl
çalıştırabileceğimize bakalım.

Yazdığınız kodu .alo uzantılı şekilde kaydettikten sonra herhangi bir
kod yazma programına kaydedin. Eğer Alore, PATH'inizde bulunuyorsa:

`$ alore hello.alo `

şeklinde.

Eğer yoksa, windows komut istemine

`C:Work>Alorealore birsey.alo`

(birsey yerine sizin kaydettiğiniz kod adını yazmalısınız) yazarak
kodunuzu çalıştırabilirsiniz.

Kullanıcıdan bilgi almak için Read Line'dan gelen "readLn" ve "WriteLn"
fonksiyonları kullanılır. Yazının devamındaki bilgileri de göz önünde
bulundurarak anlayacağınız bir kod dizini örneği yapalım:

```
var reply 
while True
 reply = ReadLn()
 if reply == 'yes' or reply == 'no'
 break
 end
 WriteLn('Type "yes" or "no".')
end
```

Fonksiyonlar, belirli bir işlevi yerine getiren kod bloklarıdır. "Def"
fonksiyonları, "var" değişkenleri(variables'dan gelir) tanımlamak için
kullanılır.

```
def Main()
 def hello()
 print("hello, world!")
 end
 hello()
end
```

Bu kod diziniyle ekrana hello world yazdırmış olduk. Kodumuzu
inceleyelim:

"Main()" ifadesi, bir programın başlangıcında otomatik olarak çağrılan
başlangıç noktasını belirtir. Programın yürütmesi, main fonksiyonu
içindeki kodla başlar. Bu nedenle ilk satırda def Main() yazdık. Kodda
dikkat çeken nokta fonksiyonları tanımladıktan sonra iki nokta olmaması.
Bu dil bir Python benzeri olsa da kullanımı kolaylaştırma amacıyla bu
tarz değişiklikleri mevcut.

Değişkenleri tanımlamadan önce değişken isimlerinin harf(a-z, A-Z),
sayı(0-9) ve alt tire içerebildiğini ancak sayı ile başlayamadığını
belirtmekte fayda var. Ayrıca Alore'da değişkenler
türsüzdür(integer/string gibi türler) - yalnızca değerlerin (veya
nesnelerin) türleri vardır. Genellikle, global kapsama sahip
fonksiyonlar ve diğer tanımlamalar (örneğin, Main) büyük harfle başlar.
Yerel değişkenler (örneğin local, two, first ve second) ise küçük harfle
başlar.

```
def Main()
 var local
 var two = 'two'
 -- 2 değişken tanımlandı.
 end
```

Şimdi bu kod satırlarını teker teker inceleyelim. Yukarıda bahsettiğimiz
gibi Alore programlarında başa Main fonksiyonu tanımlanır. İlk
değişkenimiz olan "local"ın değeri atanmamış. Bunu Python'daki boş
değişkenlerle bağdaştırabiliriz. Ancak Alore dilinde var olduğunu
belirtmek için başa kısaca "var" yazılır. Diğer değişkenimiz olan two'ta
ise "two" değeri atanmış. - - ile başlayan satır ise bir yorum satırı.
Bu satır koda dahil edilmez ancak kodunuzu daha iyi anlamanız gibi
amaçlarla koda eklenebilir. Kodumuz son parçası olan "end" ise main
fonksiyonu içinde tanımlanan işlemlerin sona erdiğini belirtmek için
kullanıldı. Bu ifade, bir fonksiyon, döngü veya başka bir kontrol yapısı
gibi belirli bir bloğun sona erdiğini gösterir.

Döngüler, belirli bir işlemi tekrarlamak için kullanılır. Alore
dilindeki for döngüsüne bakalım:

```
def Main()

for i in 0 to 5
 Print(i)
end
```

Pythonla ilişki kuracak olursak Python'daki range fonksiyonu yerine

ilk sayı to son sayı + 1 mantığının kullanıldığını görebiliriz. Ayrıca
değişken tanımlamadan sonra kullanılmadığı gibi for döngüsünün ilk
satırından sonra da iki nokta(:) kullanılmamış. Bu kod dizinlerinin
çıktısı:

```
0
1
2
3
4
```

olacaktır. Yani 2. sırada yazılan sayı çıktıya dahil olmaz. Şimdiyse bu
for döngüsüne çıktı olarak eşdeğer ancak boolean ifadesiyle kontrolünü
sağlayabileceğimiz while döngüsüne bakalım:

```
def Main()

 var i = 0
 while i < 5
 Print(i)
 i += 1

end
```

Bu kodda i adında bir değişken belirleyip 0'a eşitledik. Alt satırında
ise i değişkeni 5'ten küçük olduğu sürece sürecek olan bir while döngüsü
başlattık. Her döngüde sayının değeri 1 arttı ve 5'e eşitlendiğinde
döngüden çıktı.

Alore dilinde matematiksel işlemleri nasıl uygulayabileceğimize bakalım:

+---------------+----------------------+--------------------+
| Operatörler   | Tanım                | Örnek              |
+---------------+----------------------+--------------------+
| mod           | kalan                | 7 mod 3 == 1       |
+---------------+----------------------+--------------------+
| \*\*          | üs                   | 2\*\*2 == 4        |
+---------------+----------------------+--------------------+
| ==            | eşitlik              | 5 == 5             |
+---------------+----------------------+--------------------+
| !=            | eşitsizlik           | 'cat' != 'CAT' |
+---------------+----------------------+--------------------+
| < <= >= > | karşılaştırma        | 2.3 < 3           |
+---------------+----------------------+--------------------+
| and or not    | boolean operatörleri | a >= 2 and b < 5 |
+---------------+----------------------+--------------------+
| +            | toplama              | 5 + 3 == 8         |
+---------------+----------------------+--------------------+
| -            | çıkarma              | 6 - 3 == 3         |
+---------------+----------------------+--------------------+
| \*            | çarpma               | 6 \* 3 == 18       |
+---------------+----------------------+--------------------+
| /             | bölme                | 6 / 3 == 2         |
+---------------+----------------------+--------------------+

Matematiksel işlemlerin kodda kullanımlarına bakalım:

```
var i = 1
i += 1 --2 olarak çıkar
```

- i = 1 +1 şeklinde uzunca yazmak yerine += diyerek kodu kısaltmış olduk

- Aynı kısaltmayı diğer matematiksel işlemler için de kullanabiliriz:

```
var x = 6
x -= 2* -- 4*
x *= 3* -- 12*
x **= 2* -- 144 (12 * 12)*
i = 2 + 3 * 4* -- 2 + 12 == 14*
i = (2 + 3) * 4* -- 5 * 4 == 20*
3 / 2* -- 1.5*
```

- Alore dilinde de python'da olduğu gibi matematiksel işlemler işlem önceliğine göre yapılır.

Bu matematiksel ifadelerin yalnız rakamlarla kullanılmak zorunda
olmadıklarını ifade etmek de fayda var. Örneğin == ifadesi değerleri
stringe eşitlemek için kullanılabilir:

'foo' + 'bar' == 'foobar'

3 * 'a' == 'aaa'

İf Koşulunun Alore'daki kullanımına bakalım.

```
if i < 5
 Print('i less than 5')
elif i > 10
 Print('i greater than 10')
else
 Print('i between 5 and 10')
end
```

Bu koddan önce i'nin değerinin belirtildiğini varsayarsak bilgisayar
önce i'nin 5'ten küçük olma durumunu kontrol edecektir. Eğer küçükse i
less than 5'i ekrana yazdıracak, değilse elif ifadesiyle devam
edecektir.

Tabii ki elif ve else ifadeleri isteğe bağlı ve elif birden fazla
kullanılabilir. Ayrıca if, elif ve else koşul kalıplarından sonra iki
nokta(:) kullanılmadığı ve else'den sonra bir karşılaştırma durumu
olmadığının farkında olmalısınız.