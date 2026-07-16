---
layout: post
title: "PHP ile MVC Mimarisi: Temiz, Modüler ve Sürdürülebilir Web Projeleri"
math: true
categories: 
  - Bilgi
tags: 
  - PHP
  - MVC
  - Web Geliştirme
  - Mimari
---

PHP projeleri büyüdükçe en büyük düşman genellikle veritabanı sorgularının, HTML çıktısının ve iş kurallarının aynı dosyada çorba olmasıdır. MVC mimarisi tam da bu noktada sahneye çıkar: Model veriyi, View kullanıcı arayüzünü, Controller ise akışı yönetir. Böylece projeniz “çalışıyor ama dokunmayalım” seviyesinden “geliştirebiliriz, test edebiliriz, bakım yapabiliriz” seviyesine yükselir.
``

## MVC Mantığı Nedir?

MVC, **Model-View-Controller** kelimelerinin kısaltmasıdır. Basit bir denklemle düşünebiliriz: $Uygulama = Veri + Mantık + Arayüz$. MVC bu parçaları birbirinden ayırarak karmaşıklığı azaltır. Yani aynı anda hem SQL yazıp hem HTML basıp hem de kullanıcı yetkisi kontrol etmek yerine, her katmana net bir sorumluluk veririz.

| Katman | Görevi | PHP Projesindeki Örnek |
|---|---|---|
| Model | Veri erişimi ve veri kuralları | Kullanıcıları veritabanından çekmek |
| View | Kullanıcıya gösterilecek çıktı | HTML tablo, form, liste |
| Controller | İstekleri karşılamak ve yönlendirmek | `/users` isteğini işleyip listeyi göstermek |

Buradaki kritik fikir **sorumluluk ayrımıdır**. Bir sınıfın değişmesi için tek bir nedeni olmalıdır. Matematiksel düşünürsek, karmaşıklığı $K$ ile gösterirsek monolitik bir dosyada $K = V * M * C$ gibi büyürken, MVC’de parçalar ayrıldığı için yönetilebilirlik $K = V + M + C$ seviyesine yaklaşır. Elbette bu tam bir bilimsel formül değil; ama zihinde güzel bir alarm yakar: çarpım büyür, toplam daha kolay yönetilir.

## Akış Nasıl Çalışır?

Bir kullanıcı `/users` adresine girdiğinde süreç genellikle şöyledir:

1. Router isteği ilgili Controller metoduna yollar.
2. Controller, Model’den gerekli veriyi ister.
3. Model veritabanı sorgusunu çalıştırır ve sonucu döndürür.
4. Controller sonucu View’e gönderir.
5. View HTML üretir.

Bu akışta Controller patron gibi görünse de aslında “orkestra şefi”dir; kemanı kendi çalmaz, davula kendi vurmaz, sadece doğru parçayı doğru anda çağırır.

## Basit Bir PHP MVC Örneği

Aşağıdaki örnekte kullanıcı listesini çeken bir Model, bunu çağıran bir Controller ve View dosyasını yükleyen küçük bir View yardımcı sınıfı görüyoruz. Kodun amacı tam bir framework yazmak değil; MVC fikrini sade biçimde göstermektir.

```php
final class UserModel
{
    public function __construct(private PDO $db) {}

    public function activeUsers(): array
    {
        $stmt = $this->db->prepare('SELECT id, name, email FROM users WHERE active = :active');
        $stmt->execute(['active' => 1]);

        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }
}

final class UserController
{
    public function __construct(private UserModel $model) {}

    public function index(): void
    {
        $users = $this->model->activeUsers();
        View::render('users/index', ['users' => $users]);
    }
}

final class View
{
    public static function render(string $file, array $data = []): void
    {
        extract($data);
        require __DIR__ . '/views/' . $file . '.php';
    }
}
```

Burada `UserModel` sadece veriye odaklanır. SQL sorgusu Controller içinde değildir; bu harika bir şeydir çünkü yarın MySQL yerine başka bir kaynak kullansanız Controller’ın bozulma ihtimali azalır. `UserController` iş akışını yönetir: kullanıcıları alır ve View’e gönderir. `View::render()` ise ilgili PHP şablonunu yükler.

## Klasik PHP ile MVC Karşılaştırması

| Yaklaşım | Avantaj | Dezavantaj |
|---|---|---|
| Her şey tek dosyada | Başlangıçta hızlıdır | Büyüdükçe bakım kabusa döner |
| MVC | Test edilebilir, okunabilir, modülerdir | İlk kurulum biraz disiplin ister |
| Framework MVC | Router, ORM, güvenlik hazır gelir | Öğrenme eğrisi ve yapı bağımlılığı oluşur |

## Dikkat Edilmesi Gerekenler

MVC kullanırken en yaygın hata, Controller’ı şişirmektir. Controller içine uzun validasyonlar, karmaşık hesaplamalar ve SQL sorguları yazarsanız mimari yine çorbaya döner; sadece adı “MVC çorbası” olur. İş mantığı büyüdüğünde Service katmanı eklemek iyi fikirdir. Örneğin ödeme hesaplama, stok kontrolü veya kampanya kuralları Model ile Controller arasına yerleşen servislerde durabilir.

Ayrıca View dosyalarında mümkün olduğunca az PHP mantığı bulundurun. View’in görevi karar vermek değil, gösterim yapmaktır. `if` ve `foreach` makuldür; ancak indirim hesaplama algoritması View içinde yaşıyorsa küçük bir mimari yangın başlamış demektir.

## Sonuç

PHP ile MVC mimarisi, projeyi daha profesyonel hale getiren güçlü bir düşünme biçimidir. Veritabanı sorgularını Model’e, kullanıcı arayüzünü View’e, istek akışını Controller’a taşıyarak hem bug bulmayı kolaylaştırır hem de yeni özellik eklemeyi daha güvenli hale getirirsiniz. Küçük projelerde bile bu alışkanlığı kazanmak, büyük projelerde sizi ciddi teknik borçtan kurtarır. Kısacası MVC, PHP dünyasında düzenli masa, etiketli çekmece ve kaybolmayan tornavida etkisi yaratır.
