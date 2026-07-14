---
layout: post
title: "Python ile Konteyner Yönetimi API'leri: Minik Sanal Kafeslerin Otomasyonu"
math: true
categories: 
  - Bilgi
tags: 
  - python
  - docker
  - konteyner
  - api
  - devops
---

Bir uygulamayı çalıştırırken “benim bilgisayarımda çalışıyordu” cümlesini tarihe gömmek istiyorsak, konteynerler en eğlenceli araçlardan biridir. Python ile konteyner yönetimi API’leri ise bu küçük, izole çalışma ortamlarını elle komut yazmadan oluşturmayı, başlatmayı, durdurmayı ve gözlemlemeyi sağlar. Yani terminalde tek tek `docker run` yazmak yerine, orkestrayı Python şefliğinde yönetiriz.
``

Konteyner mantığını anlamak için önce şu fikri netleştirelim: Konteyner, tam bir sanal makine değildir. İşletim sisteminin çekirdeğini paylaşır; fakat dosya sistemi, ağ, süreçler ve ortam değişkenleri açısından izole davranır. Bu yüzden hızlı başlar, az kaynak tüketir ve taşınabilirdir. Basitçe kaynak maliyetini şöyle düşünebiliriz: $M_{toplam}=M_{imaj}+M_{runtime}+M_{veri}$. Sanal makinelerde buna çoğu zaman ayrı bir işletim sistemi maliyeti de eklenir.

| Özellik | Sanal Makine | Konteyner |
|---|---|---|
| Başlama süresi | Dakikalar olabilir | Genellikle saniyeler |
| İzolasyon | Çok güçlü, ayrı OS | Güçlü, paylaşılan kernel |
| Kaynak kullanımı | Daha yüksek | Daha düşük |
| Taşınabilirlik | Orta | Çok yüksek |
| Tipik kullanım | Tam sistem simülasyonu | Uygulama dağıtımı |

Python tarafında en yaygın yaklaşım Docker Engine API ile konuşmaktır. Docker aslında arka planda bir HTTP API sunar; `docker` komutu da bu API’ye istek atan bir istemcidir. Python’da `docker` SDK kullanarak bu API’ye zarifçe bağlanırız. Böylece uygulama konteyneri, PostgreSQL konteyneri, test veritabanı veya geçici worker süreçleri kodla yönetilebilir.

```python
import docker

client = docker.from_env()

container = client.containers.run(
    'nginx:alpine',
    name='mini-web',
    ports={'80/tcp': 8080},
    detach=True
)

print('Konteyner başladı:', container.id[:12])
```

Bu kod, yerel Docker ortamına bağlanır, `nginx:alpine` imajından bir konteyner başlatır ve konteynerin 80 portunu makinedeki 8080 portuna bağlar. `detach=True`, sürecin arka planda çalışmasını sağlar. Buradaki kritik düşünce şudur: Python kodu artık altyapıyı tarif eden küçük bir otomasyon robotudur.

Veritabanı senaryosu daha da ilginçtir. Diyelim ki her test çalışmasında temiz bir PostgreSQL istiyorsunuz. Konteyner API’siyle test başlamadan veritabanını ayağa kaldırır, test bitince yok edersiniz. Bu yaklaşım özellikle CI/CD hatlarında çok değerlidir.

```python
import docker
import time

client = docker.from_env()

db = client.containers.run(
    'postgres:16-alpine',
    name='test-postgres',
    environment={
        'POSTGRES_PASSWORD': 'secret',
        'POSTGRES_DB': 'appdb'
    },
    ports={'5432/tcp': 55432},
    detach=True,
    remove=True
)

time.sleep(5)
print('Test veritabanı hazır:', db.name)
```

Burada `environment` parametresi konteyner içindeki ortam değişkenlerini belirler. `remove=True`, konteyner durunca otomatik temizlenmesini sağlar. Elbette gerçek projede `sleep` yerine sağlık kontrolü yapmak daha doğru olur; çünkü veritabanının hazır olma süresi makineye göre değişebilir.

Konteyner yönetiminde yaşam döngüsü genellikle şu adımlardan oluşur:

| Aşama | API işlemi | Amaç |
|---|---|---|
| Oluşturma | `containers.run` veya `create` | İmajdan yeni ortam üretmek |
| Başlatma | `start` | Süreci çalıştırmak |
| İzleme | `logs`, `stats` | Çıktı ve kaynak takibi |
| Durdurma | `stop` | Kontrollü kapatma |
| Temizleme | `remove` | Artıkları silmek |

Kaynak tüketimini izlemek de otomasyonun önemli parçasıdır. Örneğin bir konteynerin CPU kullanımını yaklaşık olarak $CPU\%=\frac{container\_delta}{system\_delta}\times cores\times100$ mantığıyla yorumlarız. Docker SDK, ham istatistikleri verir; siz bu verilerden alarm, rapor veya otomatik ölçekleme kararları üretebilirsiniz.

```python
container = client.containers.get('mini-web')

for line in container.logs(stream=True, tail=5):
    print(line.decode('utf-8').strip())
```

Bu örnek, çalışan bir konteynerin loglarını akış halinde okur. Log okuma; hata ayıklama, canlı izleme ve otomatik analiz için temel bir tekniktir. Bir uygulama 500 hatası üretmeye başladığında Python betiğiniz bunu yakalayıp Slack mesajı atabilir, yeni konteyner başlatabilir veya sorunlu olanı yeniden başlatabilir.

Tabii güç arttıkça sorumluluk da artar. Konteyner API’lerine erişen Python kodu, sistemde ciddi yetkilere sahip olabilir. Bu yüzden socket erişimini sınırlamak, gizli bilgileri koda gömmemek, imajları güvenilir kaynaklardan çekmek ve ağ yapılandırmasını bilinçli yapmak gerekir.

Sonuç olarak Python ile konteyner yönetimi API’leri, uygulama ve veritabanlarını küçük sanal odalara yerleştirip bu odaların ışığını, kapısını, havalandırmasını kodla kontrol etmeye benzer. Geliştirme ortamı kurma, entegrasyon testi, geçici servis çalıştırma ve mini DevOps otomasyonları için oldukça güçlü bir yaklaşımdır. Birkaç satır Python ile altyapıya dokunmak hem pratik hem de biraz sihirli hissettirir.
