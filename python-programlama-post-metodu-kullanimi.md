# Python programlama ile post metodu kullanımı

## HTTP POST Method:

Küçük bilgi parçalarını göndermek istediğimizde sorgu dizeleri kullanışlıdır, ancak verilerimiz daha karmaşık hale geldikçe, onu sorgu dizeleri kullanarak temsil etmek zorlaşabilir. 

Bu durumda bir alternatif,  HTTP POST yöntemini kullanmaktır . Bu yöntem bir web servisine veri veya bir mesaj gönderir, Bir web formunu doldurduğunuzda ve göndermek için bir düğmeye bastığınızda, bu verileri web sunucusuna geri göndermek için POST yöntemini kullanırsınız. Bu yöntem, iletilecek bir sürü veri olduğunda kullanılma eğilimindedir.

Komut dosyalarımızda bir POST isteği bir GET isteğine çok benzer.  Bir sorgu dizesine dönüştürülen ve URL'ye eklenen params özniteliğini ayarlamak yerine   , POST isteğinin bir parçası olarak gönderilecek verileri içeren data özniteliğini kullanırız.

```
>>> p = {"description": "white kitten",
...      "name": "Snowball",
...      "age_months": 6}
>>> response = requests.post("https://example.com/path/to/api", data=p)
```

Bu istek için oluşturulan URL'yi görelim:

```
>>> response.request.url
'https://example.com/path/to/api'
```

Dikkat ettiyseniz tüm parametreler burada URL kısmında oluşmadı. Burada veriler  HTTP mesajının gövdesinin bir parçasıdı durumundadır. Onları body  özelliğini kontrol ederek görebiliriz. 

```
>>> response.request.body
'description=white+kitten&name=Snowball&age_months=6'
```

Bir web servisine veri göndermemiz ve almamız gerekirse, verilerimizi sözlüğe dönüştürebilir ve ardından bunu  bir POST isteğinin veri özelliği olarak aktarabiliriz. Verileri özellikle JSON biçiminde göndermek ve almak yaygındır, bu nedenle Requests modülü, JSON  parametresini kullanarak dönüştürmeyi bizim için doğrudan yapabilir. 

```
>>> response = requests.post("https://example.com/path/to/api", json=p)
>>> response.request.url
'https://example.com/path/to/api'
>>> response.request.body
b'{"description": "white kitten", "name": "Snowball", "age_months": 6}' 
```

Python ile HTTP protokolünde GET ve POST gönderme ve geri bildirim alma olayları bu şekilde olmaktadır.
